#!/usr/bin/env python3
"""Audit and optionally render every figure listed in the validated manifest."""
from __future__ import annotations
import argparse
import csv
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SPEC_DIR = ROOT / "annexos" / "graphics"
MANIFEST = ROOT / "dist" / "graphics" / "manifest.json"
REPORT_DIR = ROOT / "dist" / "graphics"


def inspect_spec(path: Path, expected_id: str) -> tuple[str, str]:
    try:
        spec = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        return "invalid_spec", str(exc)

    if spec.get("id") != expected_id:
        return "invalid_spec", f"Identificador absent o inconsistent: s'esperava {expected_id}."

    # A structured brief is a valid editorial specification, but it is not
    # yet a finished layout and must never be sent to the generic renderer.
    if spec.get("production_status") == "brief_structured_not_renderable":
        if not isinstance(spec.get("composition"), str) or not spec["composition"].strip():
            return "invalid_spec", "El brief estructurat no conté una composició textual vàlida."
        if not spec.get("source") or not spec.get("rendering_note"):
            return "invalid_spec", "El brief estructurat no conserva la font o la nota de renderització."
        return "brief_structured_not_renderable", "Brief estructurat i traçable; pendent de disseny visual i plantilla específica."

    if spec.get("template") == "layer_sequence_4":
        stages = spec.get("stages")
        if not spec.get("title") or not isinstance(stages, list) or len(stages) != 4:
            return "invalid_spec", "La seqüència de quatre fases és incompleta."
        for stage in stages:
            if not isinstance(stage, dict) or not stage.get("heading") or not stage.get("caption") or not isinstance(stage.get("detail_lines"), list):
                return "invalid_spec", "Una fase de la seqüència és incompleta."
        return "ready", "Plantilla específica de seqüència de capes."

    if spec.get("template") == "light_orientation":
        if not spec.get("title") or not spec.get("description"):
            return "invalid_spec", "L’esquema geomètric necessita títol i descripció."
        return "ready", "Plantilla específica d’orientació de plans respecte d’una font comuna."

    if spec.get("template") == "biological_material_atlas":
        if not spec.get("title") or not spec.get("description") or not spec.get("provenance"):
            return "invalid_spec", "L’atles morfològic necessita títol, descripció i traçabilitat."
        return "ready", "Atles morfològic específic de materials biològics."

    cards = spec.get("cards")
    if not isinstance(cards, list) or len(cards) != 4:
        return "unsupported_template", "Hi ha especificació individual, però encara no correspon a una plantilla de renderització disponible."
    if not spec.get("title"):
        return "invalid_spec", "Falta el camp obligatori title."
    for index, card in enumerate(cards):
        if not isinstance(card, dict) or not all(card.get(key) for key in ("letter", "heading")) or not isinstance(card.get("body"), list):
            return "invalid_spec", f"Bloc {index + 1}: estructura incompleta."
    return "ready", "Especificació compatible amb la plantilla de quatre blocs."


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, default=MANIFEST)
    parser.add_argument("--render", action="store_true", help="Renderitza les especificacions compatibles.")
    args = parser.parse_args()
    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    results = []
    for figure in manifest["figures"]:
        figure_id = figure["id"]
        spec_path = SPEC_DIR / f"{figure_id}.json"
        result = {**figure, "status": "", "detail": ""}
        if not spec_path.is_file():
            result.update(status="missing_spec", detail="No hi ha especificació JSON individual.")
        else:
            status, detail = inspect_spec(spec_path, figure_id)
            if status == "ready" and args.render:
                proc = subprocess.run(
                    [sys.executable, str(ROOT / "tools" / "graphics" / "render_figure.py"), "--figure", figure_id],
                    cwd=ROOT, text=True, capture_output=True,
                )
                if proc.returncode == 0:
                    result.update(status="rendered", detail=proc.stdout.strip())
                else:
                    result.update(status="render_error", detail=(proc.stderr or proc.stdout).strip())
            else:
                result.update(status=status, detail=detail)
        results.append(result)
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    json_path = REPORT_DIR / "batch_report.json"
    csv_path = REPORT_DIR / "batch_report.csv"
    json_path.write_text(json.dumps(results, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    with csv_path.open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(results[0].keys()))
        writer.writeheader()
        writer.writerows(results)
    counts = {}
    for item in results:
        counts[item["status"]] = counts.get(item["status"], 0) + 1
    print("Resultat del lot:")
    for status, count in sorted(counts.items()):
        print(f"  {status}: {count}")
    print(f"Informes: {json_path.relative_to(ROOT)} i {csv_path.relative_to(ROOT)}")
    return 1 if counts.get("render_error") or counts.get("invalid_spec") else 0


if __name__ == "__main__":
    raise SystemExit(main())
