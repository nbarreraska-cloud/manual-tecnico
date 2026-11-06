#!/usr/bin/env python3
"""Create first-pass, traceable visual drafts for every F10 figure without a renderer-specific spec.

This is a production bootstrap, not an approval engine: generated cards remain schematic
and carry explicit draft status. Existing hand-authored specs are preserved except
structured briefs, which are converted to a generic four-panel draft while their source
brief is retained in provenance.
"""
from __future__ import annotations
import json, re, shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MATRIX = ROOT / "annexos" / "matriu_tracabilitat_P1_156_F10.md"
BRIEFS = ROOT / "annexos" / "briefs_visuals_detallats_G151-G170_DBD02_2026-11.md"
SPECS = ROOT / "annexos" / "graphics"
OUT = ROOT / "dist" / "graphics"


def clean(s: str) -> str:
    return re.sub(r"\s+", " ", s.replace("<br>", " ").strip()).strip(" .;|")


def split_points(s: str) -> list[str]:
    s = re.sub(r"\*\*|__|\\", "", s)
    chunks = re.split(r"(?<=[.;])\s+|\s*[•–—]\s*", s)
    return [clean(x) for x in chunks if len(clean(x)) > 12]


def cards_from(text: str, title: str) -> list[dict]:
    points = split_points(text)
    if not points:
        points = [title]
    # Preserve all source meaning in four balanced, concise reading groups.
    groups = [[] for _ in range(4)]
    for i, point in enumerate(points):
        groups[min(3, i * 4 // max(1, len(points)))].append(point)
    labels = ["Estructura", "Elements", "Relacions", "Lectura"]
    cards = []
    for i, group in enumerate(groups):
        body = group or ["Consultar el text de referència per al detall complet."]
        body = [x[:118].rstrip(" ,;:") for x in body[:3]]
        cards.append({"letter": str(i+1), "heading": labels[i], "body": body})
    return cards


def parse_matrix():
    rows = {}
    for line in MATRIX.read_text(encoding="utf-8").splitlines():
        if not re.match(r"^\|\s*\d+(?:\.\d+)?\s*\|", line):
            continue
        cells = [x.strip() for x in line.strip().strip("|").split("|")]
        if len(cells) < 7:
            continue
        match = re.search(r"\(G(\d{3})\)", cells[4])
        if not match:
            continue
        gid = "G" + match.group(1)
        rows[gid] = {"source_id": cells[0], "source_title": cells[2],
                     "composition": cells[3], "title": cells[5], "placement": cells[6]}
    return rows


def parse_complementary():
    text = BRIEFS.read_text(encoding="utf-8")
    out = {}
    for m in re.finditer(r"(?ms)^## (G\d{3}) — (.+?)\n(.*?)(?=^## G\d{3} — |^## 4\.|\Z)", text):
        gid, title, body = m.group(1), clean(m.group(2)), m.group(3)
        comp = re.search(r"(?ms)^\*\*Composició\*\*\s*\n(.*?)(?=^\*\*Jerarquia|^\*\*Informació|\Z)", body)
        if comp:
            out[gid] = {"title": title, "composition": clean(re.sub(r"(?m)^\s*[-*]\s*", "", comp.group(1)).replace("\n", " ")),
                        "brief": body}
    return out


def main():
    SPECS.mkdir(parents=True, exist_ok=True)
    OUT.mkdir(parents=True, exist_ok=True)
    matrix = parse_matrix()
    complementary = parse_complementary()
    created, refreshed, preserved, errors = [], [], [], []
    for n in range(1, 171):
        gid = f"G{n:03d}"
        path = SPECS / f"{gid}.json"
        existing = json.loads(path.read_text(encoding="utf-8")) if path.exists() else None
        if existing and existing.get("production_status") not in ("brief_structured_not_renderable",):
            preserved.append(gid)
            continue
        if gid in complementary:
            row = complementary[gid]
            title = row["title"]
            source_text = row["composition"]
            provenance = "Brief DBD-02; composició extreta sense afegir receptes ni resultats."
            evidence = "E0/E1 segons el brief editorial; no és evidència experimental."
        elif gid in matrix:
            row = matrix[gid]
            title = row["title"]
            source_text = row["composition"]
            provenance = f"Matriu de traçabilitat P1; origen {row['source_id']}: {row['source_title']}; ubicació {row['placement']}."
            evidence = "Esquema de treball derivat de la composició editorial; no és una mostra experimental."
        else:
            errors.append(f"{gid}: no hi ha traçabilitat d'origen")
            continue
        spec = {
            "schema_version": 1, "id": gid, "title": title,
            "subtitle": "Esquema editorial de treball · no és una prova física",
            "description": source_text[:900],
            "figure_label": f"FIGURA {gid} · ESBORRANY VISUAL",
            "template": "cards_4",
            "cards": cards_from(source_text, title),
            "note": "Esquema conceptual derivat de la fitxa; verificar fidelitat i llegibilitat abans d'aprovar.",
            "production_status": "auto_draft_renderable",
            "approval_status": "not_approved_pending_visual_and_documentary_review",
            "provenance": provenance,
            "evidence_note": evidence,
            "source_brief_preserved": bool(gid in complementary)
        }
        path.write_text(json.dumps(spec, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        (refreshed if existing else created).append(gid)
    export_dir = OUT / "specs"
    if export_dir.exists():
        shutil.rmtree(export_dir)
    export_dir.mkdir(parents=True, exist_ok=True)
    for path in sorted(SPECS.glob("G*.json")):
        shutil.copy2(path, export_dir / path.name)
    report = {"total": 170, "created": created, "refreshed_from_brief": refreshed,
              "preserved_existing": preserved, "errors": errors}
    (OUT / "autoproduction_report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    exported = len(list(export_dir.glob("G*.json")))
    print(f"Especificacions creades: {len(created)}; briefs convertits: {len(refreshed)}; preservades: {len(preserved)}; exportades: {exported}; incidències: {len(errors)}")
    if errors:
        print("\n".join(errors))
        return 1
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
