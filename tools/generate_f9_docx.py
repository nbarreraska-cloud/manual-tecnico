#!/usr/bin/env python3
"""Build the F9 text-only Word master from approved Markdown sources."""
from pathlib import Path
import re
from docx import Document
from docx.shared import Cm, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.section import WD_SECTION
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
FICHE_BOOKMARKS = {}

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
    instr.text = ' TOC \\o "1-2" \\h \\z \\u '
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
            mm = re.match(r"\[([^\]]+)\]\(([^)]+)\)", s)
            if mm:
                label, target = mm.group(1), mm.group(2)
                bookmark = FICHE_BOOKMARKS.get(Path(target).name)
                if bookmark:
                    hyperlink = OxmlElement("w:hyperlink")
                    hyperlink.set(qn("w:anchor"), bookmark[0])
                    hyperlink.set(qn("w:history"), "1")
                    run = OxmlElement("w:r")
                    rpr = OxmlElement("w:rPr")
                    color = OxmlElement("w:color"); color.set(qn("w:val"), "235382")
                    underline = OxmlElement("w:u"); underline.set(qn("w:val"), "single")
                    rpr.extend([color, underline])
                    run.append(rpr)
                    text_node = OxmlElement("w:t"); text_node.text = label
                    run.append(text_node); hyperlink.append(run)
                    paragraph._p.append(hyperlink)
                else:
                    r = paragraph.add_run(label)
                    r.font.color.rgb = RGBColor(35, 83, 130)
                    r.underline = True
            else:
                paragraph.add_run(s)
        pos = m.end()
    if pos < len(text):
        paragraph.add_run(text[pos:])

def set_repeat_table_header(row):
    trPr = row._tr.get_or_add_trPr()
    tblHeader = OxmlElement("w:tblHeader")
    tblHeader.set(qn("w:val"), "true")
    trPr.append(tblHeader)

def add_markdown_block(doc, lines, compact=False, first_heading_level=1, page_break_before_first_heading=False, first_heading_bookmark=None):
    i = 0
    first_heading_seen = False
    add_markdown_block._bookmark_added = False
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
                    # Keep each table row intact across page breaks; split rows
                    # can detach a cell fragment from the row label and harm reading.
                    trPr = row._tr.get_or_add_trPr()
                    trPr.append(OxmlElement("w:cantSplit"))
                    if ri == 0: set_repeat_table_header(row)
                    for ci in range(cols):
                        cell = row.cells[ci]
                        cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
                        set_cell_margins(cell, 25 if compact else 55, 45, 25 if compact else 55, 45)
                        p = cell.paragraphs[0]
                        p.paragraph_format.space_after = Pt(0)
                        p.paragraph_format.line_spacing = 0.98 if compact else 1.0
                        add_inline(p, cells[ci] if ci < len(cells) else "")
                        for run in p.runs:
                            run.font.size = Pt(7.0 if compact else 8.2)
                            if ri == 0: run.bold = True
                doc.add_paragraph().paragraph_format.space_after = Pt(0)
            continue
        hm = re.match(r'^(#{1,6})\s+(.*)$', raw)
        if hm:
            level = len(hm.group(1))
            style_level = min(4, max(3, level + 2)) if compact else min(3, max(1, level + first_heading_level - 1))
            p = doc.add_paragraph(style=f"Heading {style_level}")
            if page_break_before_first_heading and not first_heading_seen:
                p.paragraph_format.page_break_before = True
            first_heading_seen = True
            p.paragraph_format.keep_with_next = True
            p.paragraph_format.space_before = Pt(3 if compact else 9)
            p.paragraph_format.space_after = Pt(1 if compact else 4)
            add_inline(p, hm.group(2).strip())
            if first_heading_bookmark and not add_markdown_block._bookmark_added:
                bookmark_start = OxmlElement("w:bookmarkStart")
                bookmark_start.set(qn("w:id"), str(first_heading_bookmark[1]))
                bookmark_start.set(qn("w:name"), first_heading_bookmark[0])
                bookmark_end = OxmlElement("w:bookmarkEnd")
                bookmark_end.set(qn("w:id"), str(first_heading_bookmark[1]))
                p._p.insert(0, bookmark_start)
                p._p.append(bookmark_end)
                add_markdown_block._bookmark_added = True
            i += 1
            continue
        if re.match(r'^\s*[-*]\s+', raw):
            p = doc.add_paragraph(style="List Bullet")
            p.paragraph_format.left_indent = Cm(0.4 if compact else 0.65)
            p.paragraph_format.first_line_indent = Cm(-0.18)
            p.paragraph_format.space_after = Pt(0.2 if compact else 2)
            add_inline(p, re.sub(r'^\s*[-*]\s+', '', raw))
            if compact:
                for run in p.runs: run.font.size = Pt(8.2)
            i += 1
            continue
        if re.match(r'^\s*\d+[.)]\s+', raw):
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Cm(0.4 if compact else 0.65)
            p.paragraph_format.first_line_indent = Cm(-0.18)
            p.paragraph_format.space_after = Pt(0.5 if compact else 2)
            number = re.match(r'^\s*(\d+[.)])\s+', raw).group(1)
            p.add_run(number + " ")
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
        p.paragraph_format.space_after = Pt(0.5 if compact else 4)
        p.paragraph_format.line_spacing = 0.98 if compact else 1.06
        add_inline(p, " ".join(para))
        if compact:
            for run in p.runs: run.font.size = Pt(8.2)

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
    for bookmark_id, fiche_path in enumerate(fiche_paths, start=100):
        paint_code = re.match(r"([0-9]+)-", fiche_path.name)
        if not paint_code:
            raise SystemExit(f"Cannot derive paint code for bookmark: {fiche_path.name}")
        FICHE_BOOKMARKS[fiche_path.name] = (f"fiche_{paint_code.group(1)}", bookmark_id)
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
    part_map = {
        1: "PART I · FONAMENTS",
        7: "PART II · TÈCNIQUES I PROCEDIMENTS",
        19: "PART III · RECEPTARI DE MATERIALS I EFECTES",
        35: "PART IV · ACABATS I CORRECCIÓ",
    }
    for n, st in enumerate(starts):
        en = starts[n+1] if n+1 < len(starts) else len(chapter_lines)
        match = re.match(r'^#\s+(0?[1-9]|[1-3][0-9])\.\s+', chapter_lines[st])
        chapter_number = int(match.group(1))
        if chapter_number in part_map:
            doc.add_section(WD_SECTION.CONTINUOUS if chapter_number == 1 else WD_SECTION.NEW_PAGE)
            first_heading_break = False
        else:
            first_heading_break = (n > 0)
        add_markdown_block(doc, chapter_lines[st:en], compact=False, first_heading_level=1, page_break_before_first_heading=first_heading_break)

    # Part V begins with Annex A and continues through Annex F.
    doc.add_section(WD_SECTION.NEW_PAGE)
    for annex_index, path in enumerate(annex_paths):
        add_markdown_block(doc, path.read_text(encoding="utf-8").splitlines(), compact=False, first_heading_level=1, page_break_before_first_heading=(annex_index > 0))

    p = doc.add_heading("ANNEX F. FITXES INDIVIDUALS DE LES 48 PINTURES", level=1)
    p.paragraph_format.page_break_before = True
    idx_lines = index.splitlines()
    intro_end = next((i for i, line in enumerate(idx_lines) if line.startswith("## Essential")), len(idx_lines))
    add_markdown_block(doc, idx_lines[:intro_end], compact=True, first_heading_level=1)
    current_group = None
    for path in fiche_paths:
        fiche_text = path.read_text(encoding="utf-8")
        group_match = re.search(r'\|\s*Conjunt Squidmar\s*[×x]\s*Vallejo\s*\|\s*\*{0,2}(.*?)\*{0,2}\s*\(', fiche_text)
        group_name = group_match.group(1).strip() if group_match else None
        if group_name and group_name != current_group:
            doc.add_heading(group_name, level=2)
            current_group = group_name
        add_markdown_block(
            doc, fiche_text.splitlines(), compact=True, first_heading_level=1,
            first_heading_bookmark=FICHE_BOOKMARKS[path.name],
        )

    # Ask Word to refresh the automatic table of contents when the file is opened.
    settings = doc.settings.element
    update_fields = OxmlElement("w:updateFields")
    update_fields.set(qn("w:val"), "true")
    settings.append(update_fields)

    # Each part has its own page header; page numbering remains continuous.
    header_labels = [
        "MANUAL TÈCNIC DE PINTURA DE MINIATURES",
        "PART I · FONAMENTS",
        "PART II · TÈCNIQUES I PROCEDIMENTS",
        "PART III · RECEPTARI DE MATERIALS I EFECTES",
        "PART IV · ACABATS I CORRECCIÓ",
        "PART V · ANNEXOS I EINES DE CONSULTA",
    ]
    for section_index, section in enumerate(doc.sections):
        section.header.is_linked_to_previous = False
        section.footer.is_linked_to_previous = False
        header = section.header.paragraphs[0]
        header.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        rr = header.add_run(header_labels[min(section_index, len(header_labels)-1)])
        rr.font.size = Pt(7); rr.font.color.rgb = RGBColor(110, 110, 110)
        footer = section.footer.paragraphs[0]
        footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
        add_page_field(footer)
    doc.core_properties.title = "Manual tècnic de pintura de miniatures — F9"
    doc.core_properties.subject = "Maquetació textual completa, sense imatges"
    doc.core_properties.comments = "Generat sense modificar el contingut tècnic de les fonts aprovades."
    doc.save(OUTPUT)
    print(f"Created {OUTPUT}")
    print(f"Validated: {len(chapter_heads)} chapters, 6 annexes A-F, {len(fiche_paths)} fiches x 7 sections.")

if __name__ == "__main__":
    main()
