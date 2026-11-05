#!/usr/bin/env python3
"""Refresh Word indexes/fields with LibreOffice UNO and export the F9 PDF."""
from pathlib import Path
import sys
import time
import uno
from com.sun.star.beans import PropertyValue

def prop(name, value):
    p = PropertyValue()
    p.Name = name
    p.Value = value
    return p

def main():
    if len(sys.argv) != 3:
        raise SystemExit("usage: export_f9_pdf.py input.docx output.pdf")
    source = Path(sys.argv[1]).resolve()
    target = Path(sys.argv[2]).resolve()
    if not source.is_file():
        raise SystemExit(f"Missing DOCX: {source}")
    target.parent.mkdir(parents=True, exist_ok=True)

    local_ctx = uno.getComponentContext()
    resolver = local_ctx.ServiceManager.createInstanceWithContext(
        "com.sun.star.bridge.UnoUrlResolver", local_ctx
    )
    ctx = None
    for _ in range(30):
        try:
            ctx = resolver.resolve(
                "uno:socket,host=localhost,port=2002;urp;StarOffice.ComponentContext"
            )
            break
        except Exception:
            time.sleep(1)
    if ctx is None:
        raise RuntimeError("Could not connect to LibreOffice UNO listener")

    desktop = ctx.ServiceManager.createInstanceWithContext(
        "com.sun.star.frame.Desktop", ctx
    )
    doc = desktop.loadComponentFromURL(
        uno.systemPathToFileUrl(str(source)),
        "_blank",
        0,
        (prop("Hidden", True), prop("ReadOnly", False), prop("UpdateDocMode", 3)),
    )
    if doc is None:
        raise RuntimeError("LibreOffice could not open the generated DOCX")

    try:
        indexes = doc.getDocumentIndexes()
        for i in range(indexes.getCount()):
            indexes.getByIndex(i).update()
        doc.refresh()
        fields = doc.getTextFields()
        fields.refresh()
        doc.store()
        doc.storeToURL(
            uno.systemPathToFileUrl(str(target)),
            (prop("FilterName", "writer_pdf_Export"), prop("Overwrite", True)),
        )
    finally:
        doc.close(True)

    if not target.is_file() or target.stat().st_size == 0:
        raise RuntimeError("PDF export produced no file")
    print(f"PDF_EXPORTED={target}")
    print(f"PDF_BYTES={target.stat().st_size}")

if __name__ == "__main__":
    main()
