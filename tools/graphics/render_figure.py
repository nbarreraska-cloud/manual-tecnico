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



def render_layer_sequence(spec: dict) -> str:
    """Render a four-stage schematic on one repeated, unchanged geometry."""
    width, height = 1600, 900
    margin = 72
    panel_w, panel_h, gap = 346, 500, 24
    top = 250
    dark, muted = "#263746", "#5B6872"
    base = "#B8C5CE"
    stages = spec["stages"]
    if len(stages) != 4:
        raise ValueError("La seqüència de capes requereix exactament quatre fases.")
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
        f'<title id="title">{escape(spec["title"])}</title>',
        f'<desc id="desc">{escape(spec.get("description", spec["title"]))}</desc>',
        f'<rect width="{width}" height="{height}" fill="#FAF9F6"/>',
        f'<text x="{margin}" y="86" font-family="DejaVu Sans, Arial, sans-serif" font-size="23" font-weight="700" letter-spacing="2" fill="{muted}">FIGURA {escape(spec["id"])}</text>',
        f'<text x="{margin}" y="148" font-family="DejaVu Sans, Arial, sans-serif" font-size="43" font-weight="700" fill="{dark}">{escape(spec["title"])}</text>',
        f'<text x="{margin}" y="190" font-family="DejaVu Sans, Arial, sans-serif" font-size="21" fill="{muted}">{escape(spec.get("subtitle", ""))}</text>',
    ]
    for i, stage in enumerate(stages):
        x = margin + i * (panel_w + gap)
        y = top
        parts.extend([
            f'<rect x="{x}" y="{y}" width="{panel_w}" height="{panel_h}" rx="18" fill="#FFFFFF" stroke="#D8DEE3" stroke-width="2"/>',
            f'<circle cx="{x+34}" cy="{y+38}" r="20" fill="#E8EEF2"/>',
            f'<text x="{x+34}" y="{y+46}" text-anchor="middle" font-family="DejaVu Sans, Arial, sans-serif" font-size="22" font-weight="700" fill="{dark}">{i+1}</text>',
            f'<text x="{x+66}" y="{y+45}" font-family="DejaVu Sans, Arial, sans-serif" font-size="20" font-weight="700" fill="{dark}">{escape(stage["heading"])}</text>',
        ])
        ox, oy = x+34, y+105
        points = f"{ox+18},{oy+24} {ox+254},{oy+24} {ox+278},{oy+100} {ox+238},{oy+190} {ox+42},{oy+190} {ox+2},{oy+100}"
        parts.append(f'<polygon points="{points}" fill="{base}" stroke="#344654" stroke-width="5" stroke-linejoin="round"/>')
        if i >= 2:
            parts.extend([
                f'<polygon points="{ox+18},{oy+24} {ox+136},{oy+24} {ox+146},{oy+190} {ox+42},{oy+190} {ox+2},{oy+100}" fill="#9EAFB9"/>',
                f'<polygon points="{ox+136},{oy+24} {ox+254},{oy+24} {ox+278},{oy+100} {ox+238},{oy+190} {ox+146},{oy+190}" fill="#D4DDE2"/>',
            ])
        # Keep the later application visible above the differentiated planes.
        if i >= 1:
            parts.append(f'<polygon points="{ox+18},{oy+24} {ox+254},{oy+24} {ox+266},{oy+62} {ox+8},{oy+62}" fill="#829EAE" opacity="0.92"/>')
        if i == 3:
            parts.extend([
                f'<path d="M {ox+136} {oy+24} L {ox+146} {oy+190}" fill="none" stroke="#344654" stroke-width="5"/>',
                f'<path d="M {ox+18} {oy+24} L {ox+254} {oy+24} L {ox+278} {oy+100} L {ox+238} {oy+190} L {ox+42} {oy+190} L {ox+2} {oy+100} Z" fill="none" stroke="#263746" stroke-width="5" stroke-linejoin="round"/>',
            ])
        detail_y = y+350
        parts.append(f'<text x="{x+24}" y="{detail_y}" font-family="DejaVu Sans, Arial, sans-serif" font-size="19" font-weight="700" fill="{dark}">{escape(stage["caption"])}</text>')
        for j, line in enumerate(stage.get("detail_lines", [])):
            parts.append(f'<text x="{x+24}" y="{detail_y+38+j*28}" font-family="DejaVu Sans, Arial, sans-serif" font-size="16" fill="{muted}">{escape(line)}</text>')
    note = escape(spec.get("note", ""))
    parts.append(f'<text x="{margin}" y="820" font-family="DejaVu Sans, Arial, sans-serif" font-size="18" fill="{muted}">{note}</text>')
    parts.append("</svg>")
    svg = "\n".join(parts)
    ET.fromstring(svg)
    return svg



def render_light_orientation(spec: dict) -> str:
    """Compare differently oriented planes under one shared light source."""
    width, height = 1600, 900
    dark, muted = "#263746", "#5B6872"
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
        f'<title id="title">{escape(spec["title"])}</title>',
        f'<desc id="desc">{escape(spec.get("description", spec["title"]))}</desc>',
        '<defs><marker id="ray" markerWidth="10" markerHeight="10" refX="7" refY="3" orient="auto"><path d="M0,0 L0,6 L8,3 z" fill="#D69A36"/></marker></defs>',
        '<rect width="1600" height="900" fill="#FAF9F6"/>',
        f'<text x="82" y="86" font-family="DejaVu Sans, Arial" font-size="23" font-weight="700" letter-spacing="2" fill="{muted}">FIGURA {escape(spec["id"])} · ESQUEMA GEOMÈTRIC</text>',
        f'<text x="82" y="150" font-family="DejaVu Sans, Arial" font-size="43" font-weight="700" fill="{dark}">{escape(spec["title"])}</text>',
        f'<text x="82" y="194" font-family="DejaVu Sans, Arial" font-size="22" fill="{muted}">{escape(spec.get("subtitle", ""))}</text>',
        '<circle cx="190" cy="430" r="62" fill="#F6D88F" stroke="#9B6A1E" stroke-width="4"/>',
        '<g stroke="#D69A36" stroke-width="4" stroke-linecap="round"><path d="M190 335 V310"/><path d="M190 525 V550"/><path d="M95 430 H70"/><path d="M285 430 H310"/><path d="M123 363 L105 345"/><path d="M257 497 L275 515"/><path d="M257 363 L275 345"/><path d="M123 497 L105 515"/></g>',
        f'<text x="190" y="535" text-anchor="middle" font-family="DejaVu Sans, Arial" font-size="20" font-weight="700" fill="{dark}">Font comuna</text>',
    ]
    planes = [
        {"x": 590, "y": 340, "dx": 0, "dy": 220, "label": "Pla vertical"},
        {"x": 930, "y": 340, "dx": 150, "dy": 180, "label": "Pla inclinat"},
        {"x": 1270, "y": 340, "dx": 220, "dy": 0, "label": "Pla horitzontal"},
    ]
    for i, p in enumerate(planes):
        ex, ey = p["x"] + p["dx"], p["y"] + p["dy"]
        parts.append(f'<path d="M 285 430 L {p["x"]} {p["y"] + p["dy"]/2}" fill="none" stroke="#D69A36" stroke-width="4" marker-end="url(#ray)"/>')
        parts.append(f'<path d="M {p["x"]} {p["y"]} L {ex} {ey}" stroke="#344654" stroke-width="13" stroke-linecap="round"/>')
        # A dashed normal is illustrative and perpendicular to each plane.
        cx, cy = (p["x"]+ex)/2, (p["y"]+ey)/2
        nx, ny = -p["dy"], p["dx"]
        norm = max((nx*nx+ny*ny)**0.5, 1)
        nx, ny = nx/norm*82, ny/norm*82
        parts.append(f'<path d="M {cx-nx} {cy-ny} L {cx+nx} {cy+ny}" stroke="#6B8797" stroke-width="3" stroke-dasharray="9 8"/>')
        parts.append(f'<text x="{cx}" y="690" text-anchor="middle" font-family="DejaVu Sans, Arial" font-size="22" font-weight="700" fill="{dark}">{escape(p["label"])}</text>')
        parts.append(f'<text x="{cx}" y="728" text-anchor="middle" font-family="DejaVu Sans, Arial" font-size="17" fill="{muted}">Orientació {i+1}</text>')
    parts.extend([
        '<path d="M 430 795 H 510" stroke="#D69A36" stroke-width="4" marker-end="url(#ray)"/>',
        f'<text x="530" y="802" font-family="DejaVu Sans, Arial" font-size="18" fill="{muted}">Direcció de la llum</text>',
        '<path d="M 850 795 H 930" stroke="#6B8797" stroke-width="3" stroke-dasharray="9 8"/>',
        f'<text x="950" y="802" font-family="DejaVu Sans, Arial" font-size="18" fill="{muted}">Normal geomètrica</text>',
        f'<text x="82" y="858" font-family="DejaVu Sans, Arial" font-size="18" fill="{muted}">{escape(spec.get("note", ""))}</text>',
        '</svg>'
    ])
    svg = "\\n".join(parts)
    ET.fromstring(svg)
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
    if spec.get("template") == "layer_sequence_4":
        svg_content = render_layer_sequence(spec)
    elif spec.get("template") == "light_orientation":
        svg_content = render_light_orientation(spec)
    else:
        svg_content = render(spec)
    svg_path.write_text(svg_content, encoding="utf-8")
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
