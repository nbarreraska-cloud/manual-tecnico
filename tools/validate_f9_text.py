#!/usr/bin/env python3
"""Audit source-word fidelity and order in the generated F9 DOCX."""
from pathlib import Path
import re
from docx import Document
from docx.oxml.table import CT_Tbl
from docx.oxml.text.paragraph import CT_P
from docx.table import Table
from docx.text.paragraph import Paragraph

ROOT = Path(__file__).resolve().parents[1]
DOCX = ROOT / "dist" / "Manual_tecnic_pintura_miniatures_F9.docx"
CONSOLIDATED = ROOT / "TERCERA_SINTESI_CONSOLIDADA_C01-C39.md"
ANNEX_DIR = ROOT / "annexos"
FICHE_DIR = ROOT / "fitxes-pintures"


def visible_text(markdown):
    out = []
    for raw in markdown.splitlines():
        line = raw.strip()
        if not line or line == "---":
            continue
        if re.fullmatch(r"\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?", line):
            continue
        line = re.sub(r"!\[([^\]]*)\]\([^)]+\)", r"\1", line)
        line = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", line)
        line = re.sub(r"^#{1,6}\s+", "", line)
        line = re.sub(r"^\s*[-*]\s+", "", line)
        line = re.sub(r"^\s*\d+[.)]\s+", lambda m: m.group(0).strip() + " ", line)
        line = re.sub(r"^>\s?", "", line)
        line = line.replace("|", " ")
        line = line.replace("**", "").replace("__", "").replace("*", "").replace("_", "").replace(chr(96), "")
        out.append(line)
    return "\n".join(out)


def words(text):
    return re.findall(r"[^\W_]+", text.casefold(), flags=re.UNICODE)


def iter_body_blocks(document):
    for child in document.element.body.iterchildren():
        if isinstance(child, CT_P):
            yield Paragraph(child, document)
        elif isinstance(child, CT_Tbl):
            yield Table(child, document)


def docx_words(path):
    document = Document(path)
    result = []
    for block in iter_body_blocks(document):
        if isinstance(block, Paragraph):
            result.extend(words(block.text))
        else:
            for row in block.rows:
                for cell in row.cells:
                    for paragraph in cell.paragraphs:
                        result.extend(words(paragraph.text))
    return result


def main():
    lines = CONSOLIDATED.read_text(encoding="utf-8").splitlines()
    start = next((i for i, line in enumerate(lines)
                  if re.match(r"^#\s+0?1\.\s+", line)), None)
    if start is None:
        raise SystemExit("FAIL: chapter 1 heading not found")
    sources = [visible_text("\n".join(lines[start:]))]
    for letter in "abcde":
        path = ANNEX_DIR / f"annex-{letter}.md"
        if not path.is_file():
            raise SystemExit(f"FAIL: missing {path}")
        sources.append(visible_text(path.read_text(encoding="utf-8")))

    index = (FICHE_DIR / "INDEX.md").read_text(encoding="utf-8")
    index_lines = index.splitlines()
    intro_end = next((i for i, line in enumerate(index_lines)
                      if line.startswith("## Essential")), len(index_lines))
    sources.append(visible_text("\n".join(index_lines[:intro_end])))
    fiche_paths = [FICHE_DIR / p for p in re.findall(r"\]\(([^)]+\.md)\)", index)]
    fiche_paths = [p for p in fiche_paths if p.is_file()]
    if len(fiche_paths) != 48:
        raise SystemExit(f"FAIL: expected 48 linked fiches; found {len(fiche_paths)}")
    for path in fiche_paths:
        sources.append(visible_text(path.read_text(encoding="utf-8")))

    expected = [token for source in sources for token in words(source)]
    actual = docx_words(DOCX)
    if not expected:
        raise SystemExit("FAIL: no source words collected")
    try:
        cursor = actual.index(expected[0])
    except ValueError:
        raise SystemExit(f"FAIL: first source word {expected[0]!r} not found in DOCX")

    for position, token in enumerate(expected):
        while cursor < len(actual) and actual[cursor] != token:
            cursor += 1
        if cursor >= len(actual):
            context = " ".join(expected[max(0, position-8):position+9])
            raise SystemExit(
                f"FAIL: source sequence diverges at word {position} ({token!r}); "
                f"context: {context}"
            )
        cursor += 1

    print("F9 SOURCE-TO-DOCX TEXT AUDIT")
    print(f"Source files checked: {1 + 5 + 1 + len(fiche_paths)}")
    print(f"Source words: {len(expected)}")
    print(f"DOCX body words: {len(actual)}")
    print("PASS: every source word survives in the DOCX in the same order.")
    print("NOTE: punctuation, formatting, and visual layout require separate review.")


if __name__ == "__main__":
    main()
