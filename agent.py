import json
import os
from typing import List, Dict, Optional
from pydantic import BaseModel
from dotenv import load_dotenv
from pypdf import PdfReader

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

# External File Import
from html_template import HTML_TEMPLATE

# ==================================================
# 1. SETUP & PDF PARSING
# ==================================================
load_dotenv()

def extract_text_from_pdf(pdf_path):
    """Extracts text from PDF manually."""
    if not os.path.exists(pdf_path):
        raise FileNotFoundError(f"Missing file: {pdf_path}")
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        content = page.extract_text()
        if content:
            text += content + "\n"
    return text

# Initialize Groq LLM
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.1,
    max_tokens=4096
)

# ==================================================
# 2. DATA SCHEMA
# ==================================================
class Experience(BaseModel):
    role: str
    company: str
    duration: str
    description: str

class Project(BaseModel):
    title: str
    description: str
    tech: List[str]
    link: Optional[str] = ""

class Education(BaseModel):
    degree: str
    institution: str
    year: str
    cgpa: Optional[str] = ""
    coursework: List[str] = []

class PortfolioData(BaseModel):
    name: str
    role: str
    meta_description: str
    site_url: str
    og_image: str
    profile_image: str
    intro_description: str
    typing_strings: List[str]
    about_text: str
    about_bullets: List[str]
    socials: Dict[str, str]
    experience: List[Experience]
    projects: List[Project]
    skills: Dict[str, List[str]]
    education: List[Education]
    resume_url: str
    contact_email: str
    contact_location: str

# ==================================================
# 3. EXTRACTION LOGIC
# ==================================================
parser = PydanticOutputParser(pydantic_object=PortfolioData)

prompt = PromptTemplate(
    template="""
    Transform the following resume text into a professional portfolio data structure.
    Rewrite descriptions using the X-Y-Z formula (Accomplished [X] as measured by [Y], by doing [Z]).
    Extract GPA/CGPA and technical coursework (4-8 items).
    Create 4 distinct roles for the Typing.js section.
    
    {format_instructions}
    
    RESUME TEXT:
    {resume}
    """,
    input_variables=["resume"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

def main():
    print("📄 Reading PDF...")
    resume_text = extract_text_from_pdf("my_resume.pdf")

    print("🤖 AI is curating your content...")
    chain = prompt | llm | parser
    data = chain.invoke({"resume": resume_text[:8000]})

    # ==================================================
    # 4. BUILDING COMPONENTS (Varad's Style)
    # ==================================================
    print("🎨 Generating Materialize UI components...")

    # Social Icons Map
    icon_map = {"github": "fa-github", "linkedin": "fa-linkedin", "twitter": "fa-twitter", "portfolio": "fa-globe"}
    
    SOCIAL_BUTTONS = "".join([
        f'<a href="{url}" target="_blank" class="btn-floating btn-large waves-effect waves-light teal" style="margin-right:15px;"><i class="fa {icon_map.get(k.lower(), "fa-link")}"></i></a>'
        for k, url in data.socials.items() if url
    ])

    ABOUT_BULLETS = "<ul>" + "".join([f"<li><i class='fa fa-check teal-text'></i> {b}</li>" for b in data.about_bullets]) + "</ul>"

    EXPERIENCE_BLOCKS = "".join([
        f"""
        <div class="card">
            <div class="card-content">
                <span class="card-title teal-text" style="font-weight:400;">{e.role} @ {e.company}</span>
                <p><em>{e.duration}</em></p>
                <p style="margin-top:10px; font-size:1.05rem;">{e.description}</p>
            </div>
        </div>
        """ for e in data.experience
    ])

    PROJECT_CARDS = "".join([
        f"""
        <div class="col s12 m6">
            <div class="card hoverable">
                <div class="card-content" style="min-height:220px;">
                    <span class="card-title teal-text" style="font-weight:500;">{p.title}</span>
                    <p>{p.description}</p>
                    <div style="margin-top:15px;">
                        {" ".join([f'<span class="skill-tag">{t}</span>' for t in p.tech])}
                    </div>
                </div>
                <div class="card-action">
                    <a href="{p.link or '#'}" target="_blank" class="teal-text">View Code</a>
                </div>
            </div>
        </div>
        """ for p in data.projects
    ])

    EDUCATION_BLOCKS = "".join([
        f"""
        <div class="card">
            <div class="card-content">
                <span class="card-title teal-text" style="font-weight:400;">{edu.degree}</span>
                <p>{edu.institution} | {edu.year}</p>
                {f'<p class="teal-text"><b>CGPA: {edu.cgpa}</b></p>' if edu.cgpa else ''}
                <div style="margin-top:10px;">
                    {" ".join([f'<span class="skill-tag" style="background:#f5f5f5; color:#757575;">{c}</span>' for c in edu.coursework])}
                </div>
            </div>
        </div>
        """ for edu in data.education
    ])

    # ==================================================
    # 5. TEMPLATE INJECTION
    # ==================================================
    replacements = {
        "{{NAME}}": data.name,
        "{{ROLE}}": data.role,
        "{{INTRO_DESCRIPTION}}": data.intro_description,
        "{{PROFILE_IMAGE}}": data.profile_image,
        "{{TYPING_STRINGS}}": json.dumps(data.typing_strings),
        "{{SOCIAL_BUTTONS}}": SOCIAL_BUTTONS,
        "{{ABOUT_TEXT}}": data.about_text,
        "{{ABOUT_BULLETS}}": ABOUT_BULLETS,
        "{{EXPERIENCE_BLOCKS}}": EXPERIENCE_BLOCKS,
        "{{PROJECT_CARDS}}": PROJECT_CARDS,
        "{{EDUCATION_BLOCKS}}": EDUCATION_BLOCKS,
        "{{RESUME_URL}}": data.resume_url,
        "{{CONTACT_EMAIL}}": data.contact_email
    }

    final_html = HTML_TEMPLATE
    for key, val in replacements.items():
        final_html = final_html.replace(key, str(val))

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(final_html)

    print("✨ index.html generated successfully!")

if __name__ == "__main__":
    main()