# Resume Matcher

**AI-powered resume–job matching and enhancement tool.**  
Parse resumes (PDF, DOCX), structure their data, generate embeddings, and match candidates to job descriptions—all with OpenAI or your own local DeepSeek model.

---

## Overview

Resume Matcher is an AI-driven system to help you analyze, structure, and enhance resumes for better job matching:

- **Parse**: Extracts and structures resumes from PDF and DOCX formats.
- **Embed**: Flattens structured data and creates vector embeddings for context-rich similarity scoring.
- **Match**: Compares resume embeddings to job description embeddings to provide fit scores and highlight improvement suggestions.
- **Local/Cloud AI**: Supports both OpenAI API (default) and *local LLM* (DeepSeek) for cost-free, privacy-friendly operation.
- **Database**: Saves both the structured resume information and vector embeddings for efficient querying and reuse.

---

## Features

- **Resume Parsing**: Handles PDF and DOCX inputs; extracts text and key fields automatically.
- **AI-Powered Structuring**: Sends extracted text to OpenAI/DeepSeek to create structured JSON (name, contact info, skills, work experience, education, certifications).
- **Embeddings & Matching**: Uses OpenAI embeddings (or local LLM) to perform similarity matching against job descriptions.
- **Enhancement Suggestions**: Flags missing/weak sections and suggests targeted improvements for better job alignment.
- **No Cloud Fees (optional)**: Run everything locally with DeepSeek; no OpenAI or third-party costs.
- **Batch Processing**: (Planned) Efficiently handle multiple resumes and JD files in one go.
- **REST API & UI**: (Planned) Deploy as an API, or integrate into your own UI.

For detailed features, see [`features.md`](my-resume-matcher/features.md).

---

## Quick Start

1. **Clone the repo**

    ```bash
    git clone https://github.com/r123singh/resume-matcher.git
    cd resume-matcher
    ```

2. **Install dependencies**

    ```bash
    pip install -r requirements.txt
    ```

3. **Set your OpenAI API Key**

    - Add your key to the environment:
      ```bash
      export OPENAI_API_KEY='your-key-here'
      ```

    - Or configure for local DeepSeek model (see below)

4. **Run the script**

    ```bash
    python embed.py
    ```

    You'll be prompted to provide paths to resumes and job descriptions.

---

## Local Model (DeepSeek) Support

No OpenAI key?  
You can run DeepSeek locally and plug it into the pipeline.

- Download and run [DeepSeek](https://github.com/deepseek-ai/DeepSeek-V2).
- Update your code to call the local DeepSeek model for parsing and/or embeddings.

**Note:** Local support requires sufficient compute and configuration.
See the `features.md` and relevant scripts for integration steps.

---

## File Structure

- `embed.py` – Main logic: resume parsing, structuring, embedding, and database storage
- `resume_parser.py` – OpenAI/LLM-driven resume extraction and structuring
- `features.md` – Complete feature list and technical details
- `requirements.txt` – Python dependencies

---

## Roadmap

- [ ] End-to-end pipeline for parsing, structuring, embedding, and matching
- [ ] Batch processing for multiple resumes/JDs
- [ ] RESTful API and/or Streamlit user interface
- [ ] Enhanced job description parser
- [ ] Visual analytics/reporting

---

## Portfolio & Media

- **Product Page**: [Resume Matcher on Gumroad](https://helloitsraman.gumroad.com/l/resumaxai)
- **Demo Video**: [YouTube Demo](https://youtu.be/ADIUy38-ORg)
- **Blog**: [Introducing NextGenResume: Your AI-powered Resume Companion](https://dev.to/buildandcodewithraman/nextgenresume-your-ai-powered-resume-companion-42fn)
- **Live Demo (Streamlit)**: [NextgenCV-Builder](https://nextgencv-builder.streamlit.app/)
---

_See the `features.md` for technical workflow and planned improvements._

For questions, open an issue or reach out via [@ramandeepsingh2972 on YouTube](https://www.youtube.com/@ramandeepsingh2972).