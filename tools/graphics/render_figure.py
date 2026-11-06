#!/usr/bin/env python3
"""Render editorial SVG figures from small, versioned JSON specifications."""
from __future__ import annotations

import argparse
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parents[2]
SPEC_DIR = ROOT / "annexos" / "graphics"
OUT_DIR = ROOT / "dist" / "graphics"


def safe_id(value: str) -> str:
    if not re.fullmatch(r"G\d{3}", value):
        raise ValueError("L'identificador ha de tenir el format G001.")
    return value


def render(spec: dict) -> str:
    width = int(spec.get("width", 1600))
    height = int(spec.get("height", 900))
    title = escape(spec["title"])
    subtitle = escape(spec.get("subtitle", ""))
    cards = spec["cards"]
    if len(cards) != 4:
        raise ValueError("Aquesta plantilla inicial requereix exactament quatre blocs.")
    margin, gap = 96, 28
    card_w = (width - 2 * margin - gap) // 2
    card_h = 260
    top = 250
    palette = spec.get("palette", ["#E8EEF4", "#E8F0E9", "#F4EDE1", "#EEE9F3"])
    dark = spec.get("ink", "#202A33")
    muted = spec.get("muted", "#596773")
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
        f'<title id="title">{title}</title>',
        f'<desc id="desc">{escape(spec.get("description", title))}</desc>',
        f'<rect width="{width}" height="{height}" fill="#FAF9F6"/>',
        f'<text x="{margin}" y="105" font-family="DejaVu Sans, Arial, sans-serif" font-size="26" font-weight="700" letter-spacing="3" fill="{muted}">{escape(spec.get("figure_label", ""))}</text>',
        f'<text x="{margin}" y="165" font-family="DejaVu Sans, Arial, sans-serif" font-size="48" font-weight="700" fill="{dark}">{title}</text>',
    ]
    if subtitle:
        parts.append(f'<text x="{margin}" y="207" font-family="DejaVu Sans, Arial, sans-serif" font-size="23" fill="{muted}">{subtitle}</text>')
    for i, card in enumerate(cards):
        col, row = i % 2, i // 2
        x, y = margin + col * (card_w + gap), top + row * (card_h + gap)
        fill = palette[i % len(palette)]
        letter = escape(card["letter"])
        heading = escape(card["heading"])
        body_lines = card["body"]
        parts.extend([
            f'<rect x="{x}" y="{y}" width="{card_w}" height="{card_h}" rx="20" fill="{fill}"/>',
            f'<circle cx="{x + 66}" cy="{y + 67}" r="34" fill="#FFFFFF" fill-opacity="0.78"/>',
            f'<text x="{x + 66}" y="{y + 78}" text-anchor="middle" font-family="DejaVu Sans, Arial, sans-serif" font-size="30" font-weight="700" fill="{dark}">{letter}</text>',
            f'<text x="{x + 120}" y="{y + 78}" font-family="DejaVu Sans, Arial, sans-serif" font-size="30" font-weight="700" fill="{dark}">{heading}</text>',
        ])
        for j, line in enumerate(body_lines):
            parts.append(f'<text x="{x + 120}" y="{y + 132 + j * 36}" font-family="DejaVu Sans, Arial, sans-serif" font-size="22" fill="{dark}">{escape(line)}</text>')
    note = escape(spec.get("note", ""))
    if note:
        parts.append(f'<text x="{margin}" y="{height - 64}" font-family="DejaVu Sans, Arial, sans-serif" font-size="19" fill="{muted}">{note}</text>')
    parts.append("</svg>")
    svg = "\n".join(parts)
    ET.fromstring(svg)  # Fail early if the generated SVG is malformed.
    return svg


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--figure", required=True, help="Figure identifier, e.g. G001")
    args = parser.parse_args()
    figure_id = safe_id(args.figure)
    spec_path = SPEC_DIR / f"{figure_id}.json"
    if not spec_path.is_file():
        print(f"No s'ha trobat l'especificació: {spec_path}", file=sys.stderr)
        return 2
    spec = json.loads(spec_path.read_text(encoding="utf-8"))
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    svg_path = OUT_DIR / f"{figure_id}.svg"
    svg_path.write_text(render(spec), encoding="utf-8")
    print(f"SVG generat: {svg_path.relative_to(ROOT)}")
    try:
        import cairosvg
        png_path = OUT_DIR / f"{figure_id}.png"
        cairosvg.svg2png(url=str(svg_path), write_to=str(png_path), output_width=1600)
        print(f"PNG generat: {png_path.relative_to(ROOT)}")
    except ImportError:
        print("CairoSVG no està instal·lat; s'ha generat només el SVG.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
