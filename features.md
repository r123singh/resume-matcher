Features
Input File Handling:
Supports PDF and DOCX file formats for text extraction.
AI-Powered Parsing:
Sends the extracted text to OpenAI to structure it into JSON.
JSON Output:
Organized resume content with key sections like name, contact info, skills, work experience, education, and certifications.


Details
Flattening Data:

Converts structured JSON into a single block of text to generate embeddings. This helps capture the context and relationships between sections (e.g., skills, experience).
Database Design:

Stores both raw structured data and the corresponding embeddings for efficient matching.
JSON Storage:

Complex fields like skills, work experience, education, and certifications are stored as JSON strings for easy retrieval.

Next Steps
Integration:
Combine all steps into a single pipeline for end-to-end processing.
Batch Processing:
Optimize to handle multiple job descriptions and resumes simultaneously.
Deployment:
Build a REST API or integrate with a UI for user interaction.


- Leveraging your local deepseek-r1 model on your local machine
- Run resume matcher againts resumes fro  any job desription using the model from your local machine itself
- No need to pay any charges for the chatgpts, or llm models
- Without paying any usage fees for other models in the market
- No high costs pay to these resume creation apps which charge you month to month basis
- Full control in your hands
