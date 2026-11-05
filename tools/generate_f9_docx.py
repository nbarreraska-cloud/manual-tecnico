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
                pPr = p._p.pPr
                p._p.insert(1 if pPr is not None else 0, bookmark_start)
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


def shade_cell(cell, fill="F3F6F8"):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = tcPr.find(qn("w:shd"))
    if shd is None:
        shd = OxmlElement("w:shd")
        tcPr.append(shd)
    shd.set(qn("w:fill"), fill)

def set_table_borders(table, color="D5DDE4", size="6"):
    tblPr = table._tbl.tblPr
    borders = tblPr.first_child_found_in("w:tblBorders")
    if borders is None:
        borders = OxmlElement("w:tblBorders")
        tblPr.append(borders)
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        element = borders.find(qn("w:" + edge))
        if element is None:
            element = OxmlElement("w:" + edge)
            borders.append(element)
        element.set(qn("w:val"), "single")
        element.set(qn("w:sz"), size)
        element.set(qn("w:color"), color)

def parse_fiche(path):
    text = path.read_text(encoding="utf-8")
    title = re.search(r"^#\s+(.+?)\s+—\s+([0-9.]+)\s*$", text, re.M)
    if not title:
        raise SystemExit(f"{path.name}: fiche title/reference not found")
    data = {"name": title.group(1), "code": title.group(2), "file": path.name}
    meta = re.search(r"## 1\.\s+Identificació(.*?)(?=^## 2\.)", text, re.S | re.M)
    meta_text = meta.group(1) if meta else ""
    for label, key in (("Conjunt Squidmar × Vallejo", "set"),
                       ("Família comercial identificada", "family"),
                       ("Número dins de l'inventari", "inventory")):
        m = re.search(r"\|\s*" + re.escape(label) + r"\s*\|\s*\*\*(.*?)\*\*\s*\|", meta_text)
        if not m:
            m = re.search(r"\|\s*" + re.escape(label) + r"\s*\|\s*(.*?)\s*\|", meta_text)
        data[key] = m.group(1).strip() if m else "No especificat"
    alias = re.search(r"(La denominació conservada a l'inventari.*?)(?=^## 2\.)", text, re.S | re.M)
    data["alias"] = " ".join(alias.group(1).split()) if alias else ""
    tech = re.search(r"\*\*Informació disponible per família.*?:\*\*\s*(.*?)(?=\n\n\*\*Límit individual|\n\n## 4\.)", text, re.S)
    data["family_note"] = " ".join(tech.group(1).split()) if tech else ""
    section = re.search(r"## 4\.\s+Presència i funció dins del manual(.*?)(?=^## 5\.)", text, re.S | re.M)
    body = section.group(1) if section else ""
    entries = []
    for chapter, raw_value in re.findall(r"^\s*-\s+\*\*Capítol\s+(\d+):\*\*\s*(.*?)\s*$", body, re.M):
        value = raw_value.strip()
        contextual = "menció contextual" in value.lower()
        value = re.sub(r"\s*\(funció indicada a la taula\)\.?", "", value, flags=re.I)
        value = value.replace("\x60", "").strip()
        if value.lower() == "undefined":
            value = "Funció no especificada a la fitxa font"
        if "|" in value:
            cells = [x.strip() for x in value.strip("|").split("|")]
            if len(cells) >= 3 and cells[1].replace(".", "") == data["code"].replace(".", ""):
                value = cells[2] or "Funció no especificada a la fitxa font"
            elif len(cells) >= 2:
                value = "Taula de síntesi: " + cells[0]
            else:
                value = "Aparició en taula; funció no especificada"
        else:
            value = re.sub(r";\s*no és una fila de recepta", "", value, flags=re.I)
            value = re.sub(r"^menció contextual de .*? al text del capítol", "Menció contextual al text", value, flags=re.I)
            value = value.strip(" .")
        entries.append((int(chapter), value, contextual))
    data["uses"] = entries
    data["no_rows"] = bool(re.search(r"No s'ha localitzat una fila de taula de recepta", body))
    return data

def add_bookmark(paragraph, bookmark):
    start = OxmlElement("w:bookmarkStart")
    start.set(qn("w:id"), str(bookmark[1]))
    start.set(qn("w:name"), bookmark[0])
    end = OxmlElement("w:bookmarkEnd")
    end.set(qn("w:id"), str(bookmark[1]))
    pPr = paragraph._p.pPr
    paragraph._p.insert(1 if pPr is not None else 0, start)
    paragraph._p.append(end)

def add_card_content(cell, data):
    cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.TOP
    set_cell_margins(cell, top=75, start=100, bottom=75, end=100)
    shade_cell(cell)
    p = cell.paragraphs[0]
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.keep_with_next = True
    r = p.add_run(data["name"])
    r.bold = True; r.font.name = "Aptos Display"; r.font.size = Pt(10)
    r.font.color.rgb = RGBColor(35, 55, 76)
    code = p.add_run("  ·  " + data["code"])
    code.bold = True; code.font.size = Pt(8.5)
    add_bookmark(p, FICHE_BOOKMARKS[data["file"]])

    def line(label, value, size=7.5):
        q = cell.add_paragraph()
        q.paragraph_format.space_after = Pt(1)
        q.paragraph_format.line_spacing = 0.96
        a = q.add_run(label + " "); a.bold = True; a.font.size = Pt(size)
        b = q.add_run(value); b.font.size = Pt(size)
    line("Set:", data["set"] + "  ·  Família: " + data["family"])
    if data["alias"]:
        line("Denominació:", data["alias"], 7.0)
    if data["family_note"]:
        line("Dada de gamma:", data["family_note"], 7.0)
    if data["uses"]:
        q = cell.add_paragraph()
        q.paragraph_format.space_before = Pt(1); q.paragraph_format.space_after = Pt(0)
        rr = q.add_run("Presència al manual"); rr.bold = True; rr.font.size = Pt(7.5)
        for chapter, description, contextual in data["uses"]:
            q = cell.add_paragraph()
            q.paragraph_format.left_indent = Cm(0.12)
            q.paragraph_format.first_line_indent = Cm(-0.12)
            q.paragraph_format.space_after = Pt(0)
            q.paragraph_format.line_spacing = 0.93
            rr = q.add_run(f"C{chapter}: "); rr.bold = True; rr.font.size = Pt(7.0)
            rr = q.add_run(description + (" [menció contextual]" if contextual else ""))
            rr.font.size = Pt(7.0)
    elif data["no_rows"]:
        line("Presència:", "Sense fila de recepta identificada als capítols 19–34; no exclou mencions al text.", 7.0)
    else:
        line("Presència:", "No consignada a la fitxa font.", 7.0)
    q = cell.add_paragraph()
    q.paragraph_format.space_before = Pt(2); q.paragraph_format.space_after = Pt(0)
    rr = q.add_run("Sense prova física individual registrada")
    rr.italic = True; rr.font.size = Pt(6.7); rr.font.color.rgb = RGBColor(95, 105, 115)

def add_annex_f(doc, index_text):
    p = doc.add_heading("ANNEX F. FITXES DE CONSULTA DE LES 48 PINTURES", level=1)
    p.paragraph_format.page_break_before = True
    intro = [
        ("Finalitat", "Consulta sintètica de les 48 referències dels quatre sets Squidmar × Vallejo. Cada fitxa recull identificació, família comercial i aparicions documentades als capítols del manual."),
        ("Lectura de les dades", "Les descripcions del fabricant corresponen a famílies comercials, no a mesures de cada pintura. Les mostres de carta són orientatives. No s'han realitzat proves físiques comparables ni s'atribueixen valors instrumentals individuals."),
        ("Traçabilitat", "Es conserven les denominacions de l'inventari quan difereixen de la carta actual. Les files de recepta es distingeixen de les mencions contextuals. Una funció consignada no equival a validació experimental ni implica ús exclusiu."),
        ("Fonts", "Vallejo Catalogue 2026; documentació oficial de Game Color (incloses les famílies Ink, Metallic i Fluo) i pàgina oficial de Xpress Color. Les referències particulars es conserven als registres de fitxa i als capítols citats.")
    ]
    for label, value in intro:
        q = doc.add_paragraph()
        q.paragraph_format.space_after = Pt(3)
        a = q.add_run(label + ". "); a.bold = True; a.font.size = Pt(8.5)
        b = q.add_run(value); b.font.size = Pt(8.5)
    q = doc.add_paragraph()
    q.paragraph_format.space_after = Pt(5)
    rr = q.add_run("Aquestes fitxes són una síntesi documental regenerada a partir de l'inventari i les fonts disponibles; no reprodueixen assajos de laboratori.")
    rr.italic = True; rr.font.size = Pt(8)
    groups = {}
    active = None
    for line_text in index_text.splitlines():
        m = re.match(r"^##\s+(Essential|Dark Future|Fantasy|Special FX)\s*$", line_text)
        if m:
            active = m.group(1); groups[active] = []
        elif active:
            m = re.search(r"\]\(([^)]+\.md)\)", line_text)
            if m:
                groups[active].append(FICHE_DIR / m.group(1))
    for group_no, group_name in enumerate(("Essential", "Dark Future", "Fantasy", "Special FX")):
        paths = groups.get(group_name, [])
        if len(paths) != 12:
            raise SystemExit(f"Annex F group {group_name}: expected 12 fiches; found {len(paths)}")
        if group_no:
            doc.add_page_break()
        for page_no in range(3):
            if page_no:
                doc.add_page_break()
            heading = doc.add_heading(group_name, level=2)
            heading.paragraph_format.space_after = Pt(4)
            batch = [parse_fiche(path) for path in paths[page_no*4:(page_no+1)*4]]
            table = doc.add_table(rows=2, cols=2)
            table.alignment = WD_TABLE_ALIGNMENT.CENTER
            table.autofit = False
            set_table_borders(table)
            for row in table.rows:
                trPr = row._tr.get_or_add_trPr()
                trPr.append(OxmlElement("w:cantSplit"))
                for cell in row.cells:
                    cell.width = Cm(8.55)
            for i, data in enumerate(batch):
                add_card_content(table.cell(i//2, i%2), data)

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
        paint_code = re.match(r"([0-9]+)-([0-9]+)-", fiche_path.name)
        if not paint_code:
            raise SystemExit(f"Cannot derive paint code for bookmark: {fiche_path.name}")
        FICHE_BOOKMARKS[fiche_path.name] = (f"fiche_{paint_code.group(1)}{paint_code.group(2)}", bookmark_id)
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

    add_annex_f(doc, index)

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
