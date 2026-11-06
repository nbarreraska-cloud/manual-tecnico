#!/usr/bin/env python3
"""Build a validated production manifest from the F10-R1 Markdown table."""
from __future__ import annotations
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_SOURCE = ROOT / "annexos" / "llista_definitiva_produccio_grafica_F10.md"
DEFAULT_OUTPUT = ROOT / "dist" / "graphics" / "manifest.json"

def cells(line: str) -> list[str]:
    return [part.strip() for part in line.strip().strip("|").split("|")]

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    text = args.source.read_text(encoding="utf-8")
    rows = []
    for line in text.splitlines():
        if not re.match(r"^\|\s*G\d{3}\s*\|", line):
            continue
        c = cells(line)
        if len(c) < 6:
            raise SystemExit(f"Fila incompleta: {line}")
        figure_id = c[0]
        if not re.fullmatch(r"G\d{3}", figure_id):
            raise SystemExit(f"Identificador invàlid: {figure_id}")
        rows.append({
            "id": figure_id,
            "editorial_number": c[1],
            "source_id": c[2],
            "chapter": c[3],
            "title": c[4],
            "placement": c[5],
        })
    ids = [row["id"] for row in rows]
    expected = [f"G{i:03d}" for i in range(1, 171)]
    if ids != expected:
        missing = sorted(set(expected) - set(ids))
        duplicates = sorted({x for x in ids if ids.count(x) > 1})
        raise SystemExit(f"F10-R1 no supera validació: files={len(ids)}, absents={missing}, duplicats={duplicates}")
    payload = {
        "source": str(args.source.relative_to(ROOT)),
        "branch": "auditoria-cobertura-visual-incidencies-2026-11",
        "count": len(rows),
        "figures": rows,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Manifest validat: {len(rows)} figures ({ids[0]}–{ids[-1]})")
    print(f"Fitxer: {args.output.relative_to(ROOT)}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
