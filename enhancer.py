import openai
import json
from mdtemplates import template
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPEN_API_KEY")
linkedin = os.getenv("LINKEDIN_URL")
github = os.getenv("GITHUB_URL")

def enhance_resume(resume_txt, job_requirements):
    prompt = f"""
    Role:
    You are a highly skilled resume expert specializing in enhancing and tailoring resumes to align with specific job requirements. Your expertise lies in refining resumes to highlight the most relevant skills, achievements, and experiences, ensuring they align with the target role's expectations.

    Task:
    You will be provided with:
    - An existing resume.
    - A set of job requirements for a specific role.
    - Your goal is to generate a refined resume in Markdown format as per output format.

    Enhancements to Apply:
        - Alignment with Job Requirements: Modify and emphasize skills, experiences, and accomplishments that best match the job description.
        - Bullet Points for Impact: Ensure each work experience entry contains exactly five compelling bullet points, highlighting key contributions and quantifiable achievements.
        - Invented/Expanded Content: If necessary, infer or creatively enhance project descriptions, job tasks, or impact statements to better fit the target role.
        - Consistency & Readability: Maintain professional formatting, clarity, and readability. Ensure the resume is concise yet detailed.
        - Additional Sections: Include LinkedIn URL: {linkedin} and GitHub URL: {github} if applicable or available, ensuring a comprehensive and well-rounded professional profile.
        - Output Format: The final output must be structured in Markdown format as per {template}.
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
                "role": "user",
                "content": f"Create a new resume using the provided resume data: {resume_txt}. Here is the job description to tailor the resume to: {job_requirements}."
            }
        ]
    )
    
    updated_resume = response.choices[0].message.content
    print("Below is the enhanced resume")
    print(updated_resume)
    return updated_resume

def edit_resume(resume_markdown, user_changes):
    prompt = f"""You are resume assistant tasked with editing the resume provided as per user changes input and finally return the updated resume.
    
    Below is resume:
    {resume_markdown}
    
    Changes suggested by user:
    {user_changes}
    
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
                "role": "user",
                "content": f"Edit the resume"
            }
        ]
    )

    updated_resume = response.choices[0].message.content
    print("Below is Edited version of the enhanced resume")
    print(updated_resume)
    return updated_resume
    