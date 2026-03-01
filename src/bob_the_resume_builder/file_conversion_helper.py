import pymupdf4llm
from typing import List, Dict


def convert_pdf_to_markdown(pdf_path: str, output_md_path: str) -> List[Dict]:
    """
    Converts a PDF file to Markdown format and saves it to the specified output path.
    """

    md_text = pymupdf4llm.to_markdown(pdf_path)

    with open(output_md_path, "w", encoding="utf-8") as f:
        f.write(md_text)

    return md_text