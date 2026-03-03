from resume_parser import (extract_text)
from enhancer import enhance_resume, edit_resume
from matcher import display_top_matches
from embed import process_and_store_resume
from dotenv import load_dotenv
from fileutils import save_as_docx, save_as_pdf
import os

load_dotenv()

resume_dir = os.getenv("RESUME_DIR")
job_desc_file = os.getenv("JOB_REQ_FILE")
keep_running = True
resume_txt = None

while keep_running:
    
    print("📜AI Powered Resume Engine📜")
    print("1. Enhance CV")
    print("2. Resume Matcher")
    print("3. Resume from Scratch")
    print("4. Exit Program")

    choice = input("Enter choice(1-4): ")

    if choice == '1':
        if resume_txt is None:
            file_path = input("Resume file name: ")
            file_path = f"{resume_dir}/{file_path}"
            print(f"Parsing resume: {file_path}\n")
            resume_txt = extract_text(file_path)
        else:
            print("Resume already parsed\n")

        print
        with open(job_desc_file, "r", encoding="utf-8") as file:
            job_requirements = file.read()
            job_requirements = job_requirements.strip()
        print("\n Enhancing Resume...")
        updated_resume = enhance_resume(resume_txt,job_requirements)
        print("\n Resume Enhanced")
        editResume = True
        while editResume:
            print("1. Edit")
            print("2. Confirm")
            user_choice = input("Enter choice: ")
            if user_choice == "1":
                user_changes= input("Enter changes: ")
                updated_resume = edit_resume(updated_resume, user_changes)
            elif user_choice == "2":
                editResume = False
                markdown_path = input("Enhanced markdown resume name: ") 
                markdown_path = f"{resume_dir}/{markdown_path}.md"
                with open(markdown_path, "w", encoding="utf-8") as md_file:
                    md_file.write(updated_resume)
                print(f"\n Enhanced Resume saved as markdown file: {markdown_path}")
                structured_resume = process_and_store_resume(markdown_path)
        print("\n 1.Save PDF")
        print("2.Save Docx") 
        print("3.Main Menu")
        export_choice = input("\n Export choice: ")
        if export_choice == "1":
            pdf_name = input("PDF file name: ")
            save_as_pdf(structured_resume, pdf_name, resume_dir)
        if export_choice == "2":
            docx_name = input("Docx File name: ")
            save_as_docx(structured_resume,docx_name, resume_dir)
    elif choice == '2':
        keep_matcher_running = True
        while keep_matcher_running:
            print("1. Add Resume")
            print("2. Match Resume")
            print("3. Main App")
            matcher_choice = input("Enter Choice(1-3): ")
            if matcher_choice == '1':
                add_resume_filename = input("Resume file: ")
                file_path = f"{resume_dir}/{add_resume_filename}"
                process_and_store_resume(file_path=file_path)
            elif matcher_choice == '2':
                job_requirements = input("Enter Job Requirements: ")
                top_n = int(input("Top matches #: "))
                display_top_matches(job_requirements, top_n)
            elif matcher_choice == '3':
                keep_matcher_running = False
            else:
                print("Invalid Choice")
    elif choice == '3':
        title = input("Enter resume title: ")
        print("1. Summary")
        print("2. Skills")
        section = input("Enter choice: ")
    elif choice == '4':
        keep_running = False      
    else:
        print("Invalid Input")
            
print("Thank you! Have a nice day")
    