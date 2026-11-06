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
    """Compare differently oriented planes with independent rays from one source."""
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
    # Three diverging rays reach spatially separated planes: no ray crosses
    # another opaque plane on its way from the common source.
    planes = [
        {"x1": 510, "y1": 330, "x2": 630, "y2": 330, "tx": 570, "ty": 330, "label": "Pla horitzontal"},
        {"x1": 920, "y1": 365, "x2": 920, "y2": 495, "tx": 920, "ty": 430, "label": "Pla vertical"},
        {"x1": 1200, "y1": 565, "x2": 1300, "y2": 675, "tx": 1250, "ty": 620, "label": "Pla inclinat"},
    ]
    for i, p in enumerate(planes):
        parts.append(f'<path d="M 285 430 L {p["tx"]} {p["ty"]}" fill="none" stroke="#D69A36" stroke-width="4" marker-end="url(#ray)"/>')
        parts.append(f'<path d="M {p["x1"]} {p["y1"]} L {p["x2"]} {p["y2"]}" stroke="#344654" stroke-width="13" stroke-linecap="round"/>')
        cx, cy = (p["x1"]+p["x2"])/2, (p["y1"]+p["y2"])/2
        dx, dy = p["x2"]-p["x1"], p["y2"]-p["y1"]
        nx, ny = -dy, dx
        norm = max((nx*nx+ny*ny)**0.5, 1)
        nx, ny = nx/norm*82, ny/norm*82
        parts.append(f'<path d="M {cx-nx} {cy-ny} L {cx+nx} {cy+ny}" stroke="#6B8797" stroke-width="3" stroke-dasharray="9 8"/>')
        label_x = cx
        parts.append(f'<text x="{label_x}" y="735" text-anchor="middle" font-family="DejaVu Sans, Arial" font-size="22" font-weight="700" fill="{dark}">{escape(p["label"])}</text>')
        parts.append(f'<text x="{label_x}" y="770" text-anchor="middle" font-family="DejaVu Sans, Arial" font-size="17" fill="{muted}">Orientació {i+1}</text>')
    parts.extend([
        '<path d="M 430 795 H 510" stroke="#D69A36" stroke-width="4" marker-end="url(#ray)"/>',
        f'<text x="530" y="802" font-family="DejaVu Sans, Arial" font-size="18" fill="{muted}">Direcció de la llum</text>',
        '<path d="M 850 795 H 930" stroke="#6B8797" stroke-width="3" stroke-dasharray="9 8"/>',
        f'<text x="950" y="802" font-family="DejaVu Sans, Arial" font-size="18" fill="{muted}">Normal geomètrica</text>',
        f'<text x="82" y="858" font-family="DejaVu Sans, Arial" font-size="18" fill="{muted}">{escape(spec.get("note", ""))}</text>',
        '</svg>'
    ])
    svg = "\n".join(parts)
    ET.fromstring(svg)
    return svg


def render_biological_material_atlas(spec: dict) -> str:
    """Three-way morphology comparison; deliberately not a histological plate."""
    width, height = 1600, 900
    dark, muted = "#263746", "#5B6872"
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
        f'<title id="title">{escape(spec["title"])}</title>',
        f'<desc id="desc">{escape(spec["description"])}</desc>',
        '<rect width="1600" height="900" fill="#FAF9F6"/>',
        f'<text x="72" y="76" font-family="DejaVu Sans, Arial" font-size="22" font-weight="700" letter-spacing="2" fill="{muted}">FIGURA G158 · ATLES MORFOLÒGIC</text>',
        f'<text x="72" y="132" font-family="DejaVu Sans, Arial" font-size="39" font-weight="700" fill="{dark}">{escape(spec["title"])}</text>',
        f'<text x="72" y="174" font-family="DejaVu Sans, Arial" font-size="20" fill="{muted}">{escape(spec["subtitle"])}</text>',
    ]
    cols = [(72, "TEIXIT OSSI", "Relleus, cavitats i porositat localitzada"),
            (584, "TEIXITS DENTALS", "Superfície generalment més contínua"),
            (1096, "ESTRUCTURES QUERATÍNIQUES", "Estructures compactes i marques direccionals")]
    for x, heading, sub in cols:
        parts.extend([
            f'<rect x="{x}" y="225" width="432" height="510" rx="18" fill="#FFFFFF" stroke="#D8DEE3" stroke-width="2"/>',
            f'<text x="{x+24}" y="270" font-family="DejaVu Sans, Arial" font-size="23" font-weight="700" fill="{dark}">{heading}</text>',
            f'<text x="{x+24}" y="304" font-family="DejaVu Sans, Arial" font-size="16" fill="{muted}">{sub}</text>'
        ])
    # Bone: simplified long-bone silhouette with localized porous marks.
    parts.extend([
        '<path d="M165 410 C130 375 100 395 112 432 C120 454 145 459 157 449 L274 560 C264 581 280 605 303 607 C338 610 351 578 329 557 C319 548 306 547 295 553 L180 433 C192 420 184 399 165 410 Z" fill="#D9C9A7" stroke="#75654E" stroke-width="5"/>',
        '<g fill="#9B8766"><circle cx="159" cy="428" r="5"/><circle cx="176" cy="441" r="4"/><circle cx="286" cy="565" r="4"/><circle cx="303" cy="580" r="5"/></g>',
        '<path d="M135 492 L214 566" stroke="#F0E5D1" stroke-width="10" stroke-linecap="round" opacity=".8"/>',
        '<text x="288" y="390" font-family="DejaVu Sans, Arial" font-size="17" fill="#5B6872">Os compacte</text>',
        '<path d="M270 398 L236 445" stroke="#8296A3" stroke-width="2"/>',
        '<circle cx="385" cy="470" r="58" fill="#EFE6D5" stroke="#75654E" stroke-width="3"/>',
        '<g fill="#A38F6D"><circle cx="360" cy="451" r="5"/><circle cx="390" cy="443" r="7"/><circle cx="407" cy="473" r="5"/><circle cx="374" cy="489" r="6"/><circle cx="399" cy="502" r="4"/></g>',
        '<text x="385" y="555" text-anchor="middle" font-family="DejaVu Sans, Arial" font-size="16" fill="#5B6872">Detall porós</text>'
    ])
    # Tooth: recognizable crown and root, with external enamel and inner dentin as schematic zones.
    parts.extend([
        '<path d="M730 390 C685 360 650 395 660 442 C667 476 687 489 695 530 C702 566 719 584 733 548 L752 496 L772 548 C786 584 803 566 810 530 C818 489 838 476 845 442 C855 395 820 360 775 390 C758 401 747 401 730 390 Z" fill="#F0E4C7" stroke="#8A785C" stroke-width="5"/>',
        '<path d="M730 390 C685 360 650 395 660 442 C667 476 687 489 695 530 C704 544 716 524 729 485 L752 436 L775 485 C788 524 800 544 810 530 C818 489 838 476 845 442 C855 395 820 360 775 390 C758 401 747 401 730 390 Z" fill="#FFF8E8" stroke="#B39E79" stroke-width="2"/>',
        '<path d="M730 408 C704 400 690 424 698 451 C705 473 722 482 733 512 L752 465 L772 512 C783 482 800 473 807 451 C815 424 801 400 775 408 C758 416 747 416 730 408 Z" fill="#D9B986" opacity=".75"/>',
        '<path d="M675 370 L704 390" stroke="#8296A3" stroke-width="2"/><text x="624" y="360" font-family="DejaVu Sans, Arial" font-size="16" fill="#5B6872">Esmalt</text>',
        '<path d="M812 510 L840 535" stroke="#8296A3" stroke-width="2"/><text x="818" y="558" font-family="DejaVu Sans, Arial" font-size="16" fill="#5B6872">Dentina</text>',
        '<text x="800" y="625" text-anchor="middle" font-family="DejaVu Sans, Arial" font-size="16" fill="#5B6872">Forma i continuïtat superficial</text>'
    ])
    # Bovid horn cutaway: keratin sheath surrounding a bony core.
    parts.extend([
        '<path d="M1218 555 C1192 493 1202 424 1251 382 C1302 338 1370 356 1402 317 C1392 384 1334 414 1297 452 C1265 485 1260 525 1268 566 Z" fill="#C6A77A" stroke="#6F5B43" stroke-width="5"/>',
        '<path d="M1238 544 C1226 493 1238 440 1278 405 C1304 382 1340 389 1370 360 C1352 401 1316 427 1287 462 C1264 490 1257 520 1264 550 Z" fill="#D9C9A7" stroke="#8A785C" stroke-width="3"/>',
        '<g fill="none" stroke="#8B704F" stroke-width="3" stroke-linecap="round"><path d="M1229 536 C1216 478 1230 424 1271 390"/><path d="M1248 548 C1237 491 1251 443 1290 408"/><path d="M1268 553 C1260 506 1275 462 1310 428"/></g>',
        '<text x="1380" y="470" font-family="DejaVu Sans, Arial" font-size="16" fill="#5B6872">Beina de queratina</text>',
        '<path d="M1370 476 L1325 484" stroke="#8296A3" stroke-width="2"/>',
        '<text x="1120" y="600" font-family="DejaVu Sans, Arial" font-size="16" fill="#5B6872">Nucli ossi</text>',
        '<path d="M1208 594 L1250 532" stroke="#8296A3" stroke-width="2"/>',
        '<rect x="1120" y="655" width="384" height="52" rx="10" fill="#F2EEE5"/>',
        '<text x="1136" y="677" font-family="DejaVu Sans, Arial" font-size="15" font-weight="700" fill="#263746">Banya de bòvid: nucli ossi</text>',
        '<text x="1136" y="697" font-family="DejaVu Sans, Arial" font-size="14" fill="#5B6872">recobert per una beina de queratina.</text>'
    ])
    parts.extend([
        '<rect x="72" y="765" width="1432" height="64" rx="12" fill="#E9EEF0"/>',
        f'<text x="96" y="804" font-family="DejaVu Sans, Arial" font-size="19" font-weight="700" fill="{dark}">La semblança de color no implica la mateixa estructura ni el mateix tractament pictòric.</text>',
        f'<text x="72" y="870" font-family="DejaVu Sans, Arial" font-size="16" fill="{muted}">{escape(spec.get("note", ""))}</text>',
        '</svg>'
    ])
    svg = "\n".join(parts)
    ET.fromstring(svg)
    return svg


def render_rock_family_atlas(spec: dict) -> str:
    """Compare representative visual patterns across three rock families."""
    width, height = 1600, 900
    dark, muted = "#263746", "#5B6872"
    cards = [
        {"x":72,"name":"ROQUES ÍGNIES","desc":"Solidificació de material fos",
         "rows":[("Granit","granite"),("Basalt","basalt")]},
        {"x":584,"name":"ROQUES SEDIMENTÀRIES","desc":"Acumulació, compactació o precipitació",
         "rows":[("Gres","sandstone"),("Calcària","limestone")]},
        {"x":1096,"name":"ROQUES METAMÒRFIQUES","desc":"Transformació per pressió, temperatura i fluids",
         "rows":[("Pissarra","slate"),("Marbre","marble"),("Gneis","gneiss")]}
    ]
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
        f'<title id="title">{escape(spec["title"])}</title>',
        f'<desc id="desc">{escape(spec["description"])}</desc>',
        '<rect width="1600" height="900" fill="#FAF9F6"/>',
        f'<text x="72" y="76" font-family="DejaVu Sans, Arial" font-size="22" font-weight="700" letter-spacing="2" fill="{muted}">FIGURA G161 · ATLES COMPARATIU</text>',
        f'<text x="72" y="132" font-family="DejaVu Sans, Arial" font-size="42" font-weight="700" fill="{dark}">{escape(spec["title"])}</text>',
        f'<text x="72" y="174" font-family="DejaVu Sans, Arial" font-size="21" fill="{muted}">{escape(spec["subtitle"])}</text>',
    ]
    for card in cards:
        x=card["x"]
        parts.extend([
            f'<rect x="{x}" y="215" width="432" height="545" rx="18" fill="#FFFFFF" stroke="#D8DEE3" stroke-width="2"/>',
            f'<text x="{x+22}" y="258" font-family="DejaVu Sans, Arial" font-size="22" font-weight="700" fill="{dark}">{card["name"]}</text>',
            f'<text x="{x+22}" y="288" font-family="DejaVu Sans, Arial" font-size="15" fill="{muted}">{card["desc"]}</text>'
        ])
        n=len(card["rows"])
        row_h=190 if n==2 else 145
        for idx,(label,kind) in enumerate(card["rows"]):
            y=310+idx*row_h
            parts.append(f'<text x="{x+22}" y="{y+22}" font-family="DejaVu Sans, Arial" font-size="18" font-weight="700" fill="{dark}">{label}</text>')
            sx,sy,sw,sh=x+22,y+35,230,76
            base={"granite":"#AFA99B","basalt":"#454A4D","sandstone":"#C6A77A","limestone":"#D9D1BF","slate":"#687985","marble":"#D9D7D0","gneiss":"#A9A39A"}[kind]
            parts.append(f'<rect x="{sx}" y="{sy}" width="{sw}" height="{sh}" rx="8" fill="{base}" stroke="#7A858C" stroke-width="2"/>')
            if kind=="granite":
                for j in range(36):
                    px=sx+8+((j*47+13)%210); py=sy+7+((j*29+9)%61)
                    rr=2+(j%4)
                    col=["#E6DFD0","#4E5356","#D0BDA0","#7A7770"][j%4]
                    parts.append(f'<circle cx="{px}" cy="{py}" r="{rr}" fill="{col}" opacity=".9"/>')
            elif kind=="basalt":
                for j in range(64):
                    px=sx+5+((j*37+11)%220); py=sy+5+((j*43+17)%66)
                    parts.append(f'<circle cx="{px}" cy="{py}" r="{1+(j%2)}" fill="#9CA2A3" opacity=".48"/>')
            elif kind in ("sandstone","limestone"):
                for j in range(4 if kind=="sandstone" else 2):
                    yy=sy+14+j*16
                    col=["#9E7955","#D9B987","#A77E59","#E0C99F"][j%4] if kind=="sandstone" else "#B5AC9B"
                    parts.append(f'<path d="M {sx+2} {yy} C {sx+55} {yy-5} {sx+130} {yy+5} {sx+sw-2} {yy-1}" stroke="{col}" stroke-width="{3 if kind=="sandstone" else 1.5}" fill="none"/>')
                if kind=="limestone":
                    parts.append(f'<ellipse cx="{sx+165}" cy="{sy+40}" rx="22" ry="12" fill="none" stroke="#9C927F" stroke-width="3"/>')
                    parts.append(f'<circle cx="{sx+70}" cy="{sy+24}" r="5" fill="#9C927F"/>')
            elif kind=="slate":
                for j in range(5):
                    yy=sy+12+j*13
                    parts.append(f'<path d="M {sx+4} {yy} L {sx+sw-4} {yy-7}" stroke="#B9C3C7" stroke-width="3" opacity=".9"/>')
            elif kind=="marble":
                for j in range(4):
                    parts.append(f'<path d="M {sx+10+j*38} {sy+5} C {sx+45+j*34} {sy+30} {sx+5+j*42} {sy+48} {sx+65+j*34} {sy+72}" stroke="{["#8B9297","#A58E7A","#B7B1A6","#727E88"][j]}" stroke-width="2.5" fill="none"/>')
            elif kind=="gneiss":
                for j in range(5):
                    yy=sy+8+j*14
                    parts.append(f'<path d="M {sx+3} {yy} C {sx+55} {yy-10} {sx+105} {yy+10} {sx+sw-3} {yy-3}" stroke="{["#E5DED0","#4B5053"][j%2]}" stroke-width="7" fill="none"/>')
            # Enlarged pattern sample, explicitly a schematic detail.
            cx,cy=x+333,sy+38
            parts.append(f'<circle cx="{cx}" cy="{cy}" r="43" fill="{base}" stroke="#6F7B83" stroke-width="3"/>')
            if kind=="granite":
                for j in range(18):
                    px=cx-31+((j*17+5)%62); py=cy-30+((j*29+7)%60)
                    parts.append(f'<circle cx="{px}" cy="{py}" r="{2+(j%3)}" fill="{["#E9E2D5","#55595B","#B79E7D"][j%3]}" opacity=".9"/>')
            elif kind=="basalt":
                for j in range(26):
                    px=cx-32+((j*23+3)%64); py=cy-31+((j*41+9)%62)
                    parts.append(f'<circle cx="{px}" cy="{py}" r="{1+(j%2)}" fill="#C2C8C8" opacity=".7"/>')
            elif kind=="sandstone":
                for j in range(5):
                    yy=cy-28+j*14
                    parts.append(f'<path d="M {cx-34} {yy} Q {cx} {yy-5} {cx+34} {yy}" stroke="{["#9E7955","#E0C99F"][j%2]}" stroke-width="5" fill="none"/>')
            elif kind=="limestone":
                parts.append(f'<ellipse cx="{cx}" cy="{cy}" rx="23" ry="14" fill="none" stroke="#9C927F" stroke-width="4"/>')
                parts.append(f'<ellipse cx="{cx-13}" cy="{cy+4}" rx="8" ry="5" fill="none" stroke="#B0A58F" stroke-width="2"/>')
                parts.append(f'<circle cx="{cx+20}" cy="{cy-17}" r="4" fill="#A79B85"/>')
            elif kind=="slate":
                for j in range(5):
                    yy=cy-27+j*13
                    parts.append(f'<path d="M {cx-34} {yy} L {cx+34} {yy-5}" stroke="#C3CDD1" stroke-width="4" fill="none"/>')
            elif kind=="marble":
                for j in range(3):
                    parts.append(f'<path d="M {cx-25+j*20} {cy-33} C {cx+10+j*9} {cy-8} {cx-18+j*17} {cy+9} {cx+25-j*8} {cy+33}" stroke="{["#7B858D","#A58E7A","#B7B1A6"][j]}" stroke-width="3" fill="none"/>')
            elif kind=="gneiss":
                for j in range(5):
                    yy=cy-28+j*14
                    col="#4B5053" if j%2 else "#E5DED0"
                    parts.append(f'<path d="M {cx-34} {yy} Q {cx} {yy-7} {cx+34} {yy}" stroke="{col}" stroke-width="7" fill="none"/>')
            parts.append(f'<text x="{cx}" y="{sy+100}" text-anchor="middle" font-family="DejaVu Sans, Arial" font-size="13" fill="{muted}">Detall</text>')
    parts.extend([
        '<rect x="72" y="785" width="1432" height="48" rx="10" fill="#E9EEF0"/>',
        f'<text x="94" y="815" font-family="DejaVu Sans, Arial" font-size="17" font-weight="700" fill="{dark}">Patrons representatius per orientar la pintura; no són una taxonomia completa ni una identificació basada només en el color.</text>',
        f'<text x="72" y="870" font-family="DejaVu Sans, Arial" font-size="16" fill="{muted}">{escape(spec.get("note", ""))}</text>',
        '</svg>'
    ])
    svg="\n".join(parts)
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
    elif spec.get("template") == "biological_material_atlas":
        svg_content = render_biological_material_atlas(spec)
    elif spec.get("template") == "rock_family_atlas":
        svg_content = render_rock_family_atlas(spec)
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
