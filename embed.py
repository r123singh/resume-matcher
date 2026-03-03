import os
import json
import numpy as np
import sqlite3
import openai
from resume_parser import process_resume

openai.api_key = os.getenv("OPENAI_API_KEY")

conn = sqlite3.connect('resumes.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS resumes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ref TEXT,
    name TEXT,
    email TEXT,
    phone TEXT,
    linkedin TEXT,
    github TEXT,
    skills TEXT,
    work_experience TEXT,
    education TEXT,
    certifications TEXT,
    embedding BLOB
)       
''')

conn.commit()

# Function to generate embeddings for structured data
def generate_embedding(text, model = "text-embedding-3-small"):
    response = openai.embeddings.create(
        input=text,
        model=model
    )
    return np.array(response.data[0].embedding)
    
# Function to store structured data and embeddings
def store_resume_data(structured_data, file_name):
    file_name.replace("_", "").replace(" ", "").replace("-", "")
    flattened_text = (
        f"Name: {structured_data['name']}\n"
        f"Contact Information: {structured_data['contact_information']}\n"
        f"Skills: {','.join(structured_data['skills'])}\n"
        f"Work Experience: {structured_data['work_experience']}\n"
        f"Education: {structured_data['education']}\n"
        f"Certifications: {structured_data['certifications']}\n"
    )
    
    try:
        # Generate embedding for the flattened text 
        embedding = generate_embedding(flattened_text) 
        # Insert data into the database
        cursor.execute('''
            INSERT INTO resumes (
                ref,name, email, phone, linkedin, github, skills, work_experience, education, certifications, embedding
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            file_name,
            structured_data['name'],
            structured_data['contact_information'].get('email'),
            structured_data['contact_information'].get('phone'),
            structured_data['contact_information'].get('linkedin'),
            structured_data['contact_information'].get('github'),
            json.dumps(structured_data['skills']),
            json.dumps(structured_data['work_experience']),
            json.dumps(structured_data['education']),
            json.dumps(structured_data['certifications']),
            json.dumps(embedding.tolist())
        ))
        conn.commit()
        print(f"Resume named {file_name} for {structured_data['name']} stored successfully.")
    except Exception as e:
        print(f"Error storing resume: {e}")
    

def process_and_store_resume(file_path):
    # Extract and structure resume
    cleaned_response = process_resume(file_path=file_path).strip("```json").strip("```").strip()
    structured_data = json.loads(cleaned_response)
   
    file_name = os.path.splitext(os.path.basename(file_path))[0]
    # Store resume and embeddings
    store_resume_data(structured_data, file_name)
    return structured_data