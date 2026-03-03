import openai
import os
import pdfplumber
import docx
from dotenv import load_dotenv

load_dotenv()

openai.api_key =os.getenv("OPENAI_API_KEY") 

# Extract text from PDF
def extract_text_from_pdf(file_path):
    with pdfplumber.open(file_path) as pdf:
        text = "\n".join(page.extract_text() for page in pdf.pages if page.extract_text())
    return text

# Extract text from DOCx
def extract_text_from_docx(file_path):
    doc = docx.Document(file_path)
    text = "\n".join(para.text for para in doc.paragraphs if para.text)
    return text

# Identify the file type and extract text
def extract_text(file_path):
    file_ext = os.path.splitext(file_path)[-1].lower()
    if file_ext == ".pdf":
        return extract_text_from_pdf(file_path)
    elif file_ext == ".docx":
        return extract_text_from_docx(file_path)
    elif file_ext == ".md":
        print(file_path)
        with open(file_path, "r", encoding="utf-8") as mdfile:
            mdtext = mdfile.read()
            print("mdfile found")
            print(mdtext)
        return mdtext
    else:
        raise ValueError("Unsupported file format. Only MARKDOWN, PDF and DOCX are supported.")

# OpenAI based processing text into structured JSON
def parse_resume(resume_text):
    
    prompt = f"""
    The following is a resume text extracted from a document: {resume_text}. Your task is to structure it into a JSON format with the following sections:  
    1. name
    2. contact_information (location,email,phone,linkedIn,github)
    3. summary
    4. skills (core_competencies, technical_skills)
    5. work_experience (list each role with title, company,location, duration, main_description and points_description)
    6. education (list each degree with institution, degree type, and year)
    7. certifications (if any)
    8. achievements (if any)
    """
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": prompt
            },
            {
                "role":'user',
                "content": f"Provide structured JSON for this resume"
            }
        ]
    )
    
    return response.choices[0].message.content

# Main func to process resume
def process_resume(file_path):
    try:
        # step1: Extract text from file
        resume_text= extract_text(file_path)
        print("Resume text extracted successfully")
        # Step 2: Open AI to parse and structure the resume
        structured_data = parse_resume(resume_text=resume_text)
        
        # Step 3: Display or save the structured data
        print("Structured Resume JSON:")
        print(structured_data)
        return structured_data
    except Exception as e:
        print(f"Error processing resume: {e}")
