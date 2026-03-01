from __future__ import annotations

import argparse
from datetime import datetime
import os

from bob_the_resume_builder.file_conversion_helper import convert_pdf_to_markdown

def main() -> int:
    parser = argparse.ArgumentParser(description="Bob the Resume Builder")
    parser.add_argument("--input", "-i", required=True, help="Path to the input resume file")
    # parser.add_argument("--job-description", "-j", required=True, help="Path to the job description file")
    
    args = parser.parse_args()
    output_md_path = f"generated/{datetime.now().strftime('%Y-%m-%d')}/{os.path.basename(args.input).replace('.pdf', '.md')}"
    if not os.path.exists(os.path.dirname(output_md_path)):
        os.makedirs(os.path.dirname(output_md_path))        

    md_resume = convert_pdf_to_markdown(args.input, output_md_path)
    print(f"Converted Markdown Resume:\n{md_resume}")

    #brain.build_resume(args.input, args.output, args.job_description)
    
    return 0