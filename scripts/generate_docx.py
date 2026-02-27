from pathlib import Path

from docx import Document
from docx.enum.text import WD_BREAK
from docx.shared import Pt

SRC = Path("docs/FINAL_SUBMISSION_DOCUMENT.md")
OUT = Path("docs/FINAL_SUBMISSION_DOCUMENT.docx")


def add_code_paragraph(doc: Document, text: str):
    p = doc.add_paragraph(text)
    for run in p.runs:
        run.font.name = "Courier New"
        run.font.size = Pt(10)


def main():
    if not SRC.exists():
        raise FileNotFoundError(f"Missing source markdown: {SRC}")

    doc = Document()
    style = doc.styles["Normal"]
    style.font.name = "Times New Roman"
    style.font.size = Pt(12)

    lines = SRC.read_text(encoding="utf-8").splitlines()
    in_code = False
    first_h1 = True

    for raw in lines:
        line = raw.rstrip()

        if line.strip().startswith("```"):
            in_code = not in_code
            continue

        if in_code:
            if line.strip():
                add_code_paragraph(doc, line)
            else:
                doc.add_paragraph("")
            continue

        if not line.strip():
            doc.add_paragraph("")
            continue

        if line.startswith("# "):
            if not first_h1:
                doc.add_page_break()
            first_h1 = False
            doc.add_heading(line[2:].strip(), level=1)
            continue

        if line.startswith("## "):
            doc.add_heading(line[3:].strip(), level=2)
            continue

        if line.startswith("### "):
            doc.add_heading(line[4:].strip(), level=3)
            continue

        if line.startswith("- ") or line.startswith("1. ") or line.startswith("2. ") or line.startswith("3. "):
            p = doc.add_paragraph(line)
            continue

        if line.startswith("|"):
            add_code_paragraph(doc, line)
            continue

        doc.add_paragraph(line)

    doc.save(OUT)
    print(f"Created: {OUT}")


if __name__ == "__main__":
    main()
