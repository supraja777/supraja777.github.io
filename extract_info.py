import os
from pypdf import PdfReader

def extract_text_from_pdf(pdf_path):
    """
    Extracts all text from a PDF file manually using pypdf.
    """
    if not os.path.exists(pdf_path):
        return f"Error: {pdf_path} not found."
    
    try:
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            content = page.extract_text()
            if content:
                text += content + "\n"
        return text
    except Exception as e:
        return f"Error parsing PDF: {str(e)}"

# 1. Path to your resume
PDF_FILE = "my_resume.pdf"

# 2. Extract the text
print(f"Reading {PDF_FILE}...")
resume_text = extract_text_from_pdf(PDF_FILE)

# 3. Handle token limits (Slicing to first 8000 characters)
input_text = resume_text[:8000]

# 4. Write the extracted text into a file
output_file = "resume_content.txt"
with open(output_file, "w", encoding="utf-8") as f:
    f.write(input_text)

print(f"✅ Success! Raw resume text has been written to: {output_file}")
