#!/usr/bin/env python3
"""Build the F9 text-only Word master from approved Markdown sources."""
from pathlib import Path
import re
from docx import Document
from docx.shared import Cm, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_CELL_VERTICAL_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
DIST.mkdir(exist_ok=True)
CONSOLIDATED = ROOT / "TERCERA_SINTESI_CONSOLIDADA_C01-C39.md"
ANNEX_DIR = ROOT / "annexos"
FICHE_DIR = ROOT / "fitxes-pintures"
FICHE_INDEX = FICHE_DIR / "INDEX.md"
OUTPUT = DIST / "Manual_tecnic_pintura_miniatures_F9.docx"

def set_cell_margins(cell, top=45, start=65, bottom=45, end=65):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = tcPr.first_child_found_in("w:tcMar")
    if tcMar is None:
        tcMar = OxmlElement("w:tcMar")
        tcPr.append(tcMar)
    for m, v in (("top", top), ("start", start), ("bottom", bottom), ("end", end)):
        node = tcMar.find(qn("w:" + m))
        if node is None:
            node = OxmlElement("w:" + m)
            tcMar.append(node)
        node.set(qn("w:w"), str(v))
        node.set(qn("w:type"), "dxa")

def add_page_field(paragraph):
    fld = OxmlElement("w:fldSimple")
    fld.set(qn("w:instr"), "PAGE")
    paragraph._p.append(fld)

def add_toc_field(paragraph):
    run = paragraph.add_run()
    begin = OxmlElement("w:fldChar"); begin.set(qn("w:fldCharType"), "begin")
    instr = OxmlElement("w:instrText"); instr.set(qn("xml:space"), "preserve")
    instr.text = ' TOC \\o "1-3" \\h \\z \\u '
    separate = OxmlElement("w:fldChar"); separate.set(qn("w:fldCharType"), "separate")
    text = OxmlElement("w:t"); text.text = "Actualitzeu la taula de continguts en obrir el document a Word."
    end = OxmlElement("w:fldChar"); end.set(qn("w:fldCharType"), "end")
    run._r.extend([begin, instr, separate, text, end])

def add_inline(paragraph, text):
    token = re.compile(r'(\*\*.*?\*\*|(?<!\*)\*[^*]+\*|\x60[^\x60]+\x60|\[[^\]]+\]\([^)]+\))')
    pos = 0
    for m in token.finditer(text):
        if m.start() > pos:
            paragraph.add_run(text[pos:m.start()])
        s = m.group(0)
        if s.startswith("**"):
            r = paragraph.add_run(s[2:-2]); r.bold = True
        elif s.startswith("*"):
            r = paragraph.add_run(s[1:-1]); r.italic = True
        elif s.startswith("\x60"):
            r = paragraph.add_run(s[1:-1]); r.font.name = "Consolas"; r.font.size = Pt(8)
        else:
            mm = re.match(r'\[([^\]]+)\]\(([^)]+)\)', s)
            r = paragraph.add_run(mm.group(1) if mm else s)
            if mm:
                r.font.color.rgb = RGBColor(35, 83, 130)
                r.underline = True
        pos = m.end()
    if pos < len(text):
        paragraph.add_run(text[pos:])

def set_repeat_table_header(row):
    trPr = row._tr.get_or_add_trPr()
    tblHeader = OxmlElement("w:tblHeader")
    tblHeader.set(qn("w:val"), "true")
    trPr.append(tblHeader)

def add_markdown_block(doc, lines, compact=False, first_heading_level=1):
    i = 0
    while i < len(lines):
        raw = lines[i].rstrip()
        if not raw.strip() or raw.strip() == "---":
            i += 1
            continue
        if raw.lstrip().startswith("|") and i + 1 < len(lines) and re.match(r'^\s*\|?\s*:?-{3,}', lines[i+1]):
            rows = []
            while i < len(lines) and lines[i].lstrip().startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                if not all(re.fullmatch(r':?-{3,}:?', c or "-") for c in cells):
                    rows.append(cells)
                i += 1
            if rows:
                cols = max(len(r) for r in rows)
                table = doc.add_table(rows=0, cols=cols)
                table.alignment = WD_TABLE_ALIGNMENT.CENTER
                table.style = "Table Grid"
                for ri, cells in enumerate(rows):
                    row = table.add_row()
                    if ri == 0: set_repeat_table_header(row)
                    for ci in range(cols):
                        cell = row.cells[ci]
                        cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
                        set_cell_margins(cell, 30 if compact else 55, 45, 30 if compact else 55, 45)
                        p = cell.paragraphs[0]
                        p.paragraph_format.space_after = Pt(0)
                        p.paragraph_format.line_spacing = 0.98 if compact else 1.0
                        add_inline(p, cells[ci] if ci < len(cells) else "")
                        for run in p.runs:
                            run.font.size = Pt(7.2 if compact else 8.2)
                            if ri == 0: run.bold = True
                doc.add_paragraph().paragraph_format.space_after = Pt(0)
            continue
        hm = re.match(r'^(#{1,6})\s+(.*)$', raw)
        if hm:
            level = len(hm.group(1))
            style_level = min(3, max(2, level + 1)) if compact else min(3, max(1, level + first_heading_level - 1))
            p = doc.add_paragraph(style=f"Heading {style_level}")
            p.paragraph_format.keep_with_next = True
            p.paragraph_format.space_before = Pt(4 if compact else 9)
            p.paragraph_format.space_after = Pt(1.5 if compact else 4)
            add_inline(p, hm.group(2).strip())
            i += 1
            continue
        if re.match(r'^\s*[-*]\s+', raw):
            p = doc.add_paragraph(style="List Bullet")
            p.paragraph_format.left_indent = Cm(0.4 if compact else 0.65)
            p.paragraph_format.first_line_indent = Cm(-0.18)
            p.paragraph_format.space_after = Pt(0.5 if compact else 2)
            add_inline(p, re.sub(r'^\s*[-*]\s+', '', raw))
            i += 1
            continue
        if re.match(r'^\s*\d+[.)]\s+', raw):
            p = doc.add_paragraph(style="List Number")
            p.paragraph_format.left_indent = Cm(0.4 if compact else 0.65)
            p.paragraph_format.first_line_indent = Cm(-0.18)
            p.paragraph_format.space_after = Pt(0.5 if compact else 2)
            add_inline(p, re.sub(r'^\s*\d+[.)]\s+', '', raw))
            i += 1
            continue
        if raw.startswith(">"):
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Cm(0.5)
            add_inline(p, raw.lstrip("> ").strip())
            i += 1
            continue
        para = [raw.strip()]
        i += 1
        while i < len(lines):
            nxt = lines[i].rstrip()
            if not nxt.strip() or nxt.strip() == "---" or re.match(r'^(#{1,6})\s+', nxt) or nxt.lstrip().startswith("|") or re.match(r'^\s*[-*]\s+|\s*\d+[.)]\s+|>', nxt):
                break
            para.append(nxt.strip())
            i += 1
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(1.5 if compact else 4)
        p.paragraph_format.line_spacing = 1.0 if compact else 1.06
        add_inline(p, " ".join(para))

def configure_styles(doc):
    for name in ("Normal", "Body Text", "List Bullet", "List Number"):
        st = doc.styles[name]
        st.font.name = "Aptos"
        st.font.size = Pt(8.5 if name == "Normal" else 8.2)
        st.paragraph_format.space_after = Pt(3)
        st.paragraph_format.line_spacing = 1.04
    for name, size in (("Heading 1", 17), ("Heading 2", 12), ("Heading 3", 9.5)):
        st = doc.styles[name]
        st.font.name = "Aptos Display"
        st.font.size = Pt(size)
        st.font.bold = True
        st.font.color.rgb = RGBColor(35, 55, 76)
        st.paragraph_format.keep_with_next = True

def main():
    consolidated = CONSOLIDATED.read_text(encoding="utf-8")
    index = FICHE_INDEX.read_text(encoding="utf-8")
    chapter_heads = re.findall(r'^#\s+(?:0?[1-9]|[1-3][0-9])\.\s+', consolidated, flags=re.M)
    if len(chapter_heads) != 39:
        raise SystemExit(f"Expected 39 chapter headings; found {len(chapter_heads)}")
    fiche_paths = [FICHE_DIR / p for p in re.findall(r'\]\(([^)]+\.md)\)', index)]
    fiche_paths = [p for p in fiche_paths if p.is_file()]
    if len(fiche_paths) != 48:
        raise SystemExit(f"Expected 48 fiche links; found {len(fiche_paths)}")
    annex_paths = [ANNEX_DIR / f"annex-{letter}.md" for letter in "abcde"]
    if not all(p.is_file() for p in annex_paths):
        raise SystemExit("One or more annexes A-E are missing")
    for path in fiche_paths:
        sections = re.findall(r'^##\s+[1-7]\.\s+', path.read_text(encoding="utf-8"), flags=re.M)
        if len(sections) != 7:
            raise SystemExit(f"{path.name}: expected seven sections; found {len(sections)}")

    doc = Document()
    sec = doc.sections[0]
    sec.page_width, sec.page_height = Cm(21), Cm(29.7)
    sec.top_margin, sec.bottom_margin = Cm(1.65), Cm(1.65)
    sec.left_margin, sec.right_margin = Cm(1.8), Cm(1.65)
    configure_styles(doc)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(105)
    r = p.add_run("MANUAL TÈCNIC DE PINTURA DE MINIATURES")
    r.bold = True; r.font.size = Pt(25); r.font.name = "Aptos Display"
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("Versió textual maquetada · F9")
    r.font.size = Pt(15); r.font.color.rgb = RGBColor(80, 95, 110)
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(35)
    p.add_run("39 capítols · Annexos A–F · 48 fitxes individuals")
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(120)
    p.add_run("Branca de treball: intervencion-editorial-2026-11\n").italic = True
    p.add_run("Maquetació textual sense imatges · 05/11/2026").italic = True

    doc.add_page_break()
    doc.add_heading("Índex general", level=1)
    add_toc_field(doc.add_paragraph())
    doc.add_page_break()

    lines = consolidated.splitlines()
    start = next((i for i, line in enumerate(lines) if re.match(r'^#\s+0?1\.\s+', line)), None)
    if start is None:
        raise SystemExit("Chapter 1 heading not found")
    chapter_lines = lines[start:]
    starts = [i for i, line in enumerate(chapter_lines) if re.match(r'^#\s+(?:0?[1-9]|[1-3][0-9])\.\s+', line)]
    for n, st in enumerate(starts):
        en = starts[n+1] if n+1 < len(starts) else len(chapter_lines)
        if n: doc.add_page_break()
        add_markdown_block(doc, chapter_lines[st:en], compact=False, first_heading_level=1)

    for path in annex_paths:
        doc.add_page_break()
        add_markdown_block(doc, path.read_text(encoding="utf-8").splitlines(), compact=False, first_heading_level=1)

    doc.add_page_break()
    doc.add_heading("ANNEX F. FITXES INDIVIDUALS DE LES 48 PINTURES", level=1)
    idx_lines = index.splitlines()
    intro_end = next((i for i, line in enumerate(idx_lines) if line.startswith("## Essential")), len(idx_lines))
    add_markdown_block(doc, idx_lines[:intro_end], compact=True, first_heading_level=1)
    for path in fiche_paths:
        add_markdown_block(doc, path.read_text(encoding="utf-8").splitlines(), compact=True, first_heading_level=1)

    for section in doc.sections:
        header = section.header.paragraphs[0]
        header.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        rr = header.add_run("MANUAL TÈCNIC DE PINTURA DE MINIATURES")
        rr.font.size = Pt(7); rr.font.color.rgb = RGBColor(110, 110, 110)
        footer = section.footer.paragraphs[0]
        footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
        add_page_field(footer)
    doc.core_properties.title = "Manual tècnic de pintura de miniatures — F9"
    doc.core_properties.subject = "Maquetació textual completa, sense imatges"
    doc.core_properties.comments = "Generat sense modificar el contingut tècnic de les fonts aprovades."
    doc.save(OUTPUT)
    print(f"Created {OUTPUT}")
    print(f"Validated: {len(chapter_heads)} chapters, 5 annexes A-E, {len(fiche_paths)} fiches x 7 sections.")

if __name__ == "__main__":
    main()
