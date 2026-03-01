#from libformdtopdf import convert_md_to_pdf
from .file_conversion_helper import convert_pdf_to_markdown

def build_resume(input_resume_path: str, output_resume_path: str, job_description_path: str):
    """
    Builds a resume by adapting the input resume to match the job description.
    """
    # Step 1: Convert the input PDF resume to Markdown
    temp_md_path = "temp_resume.md"
    convert_pdf_to_markdown(input_resume_path, temp_md_path)

    # Step 2: Read the job description
    with open(job_description_path, "r", encoding="utf-8") as f:
        job_description = f.read()

    # Step 3: Adapt the Markdown resume based on the job description
    # logic to adapt the resume goes here (e.g., using NLP techniques to match keywords, reordering sections, etc.)
    with open(temp_md_path, "r", encoding="utf-8") as f:
        md_content = f.read()
    
    print("Job Description:")
    print(job_description)
    
    print("\nMarkdown Resume Content:")
    print(md_content)

    # Step 4: Convert the adapted Markdown back to PDF
    # convert_md_to_pdf(temp_md_path, output_resume_path)