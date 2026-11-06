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

def inspect_spec(path: Path) -> tuple[str, str]:
    try:
        spec = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        return "invalid_spec", str(exc)
    cards = spec.get("cards")
    if not isinstance(cards, list) or len(cards) != 4:
        return "unsupported_template", "La plantilla actual només admet quatre blocs."
    required = ("title",)
    if any(not spec.get(key) for key in required):
        return "invalid_spec", "Falta el camp obligatori title."
    for index, card in enumerate(cards):
        if not all(card.get(key) for key in ("letter", "heading")) or not isinstance(card.get("body"), list):
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
            status, detail = inspect_spec(spec_path)
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
