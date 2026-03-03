from sklearn.metrics.pairwise import cosine_similarity
from embed import generate_embedding
import numpy as np
import json
import sqlite3

conn = sqlite3.connect('resumes.db')
cursor = conn.cursor()

# Function to fetch all resumes and their embeddings from the database
def fetch_all_resumes():
    cursor.execute('SELECT id, ref, name, embedding FROM resumes')
    results = cursor.fetchall()
    resumes = []
    for res in results:
        res_id, name, embeddings_json = res
        
        # Handle empty or invalid JSON
        if not embeddings_json:
            print(f"Warning: Empty embedding for resume ID {res_id}")
            continue
        
        try:
            # Decode JSON into a NumPy array
            embedding = np.array(json.loads(embeddings_json))
            resumes.append({"id": res_id, "name": name, "embedding": embedding})
        except json.JSONDecodeError as e:
            print(f"Error decoding embedding for resume ID {res_id}: {e}")
    return resumes

def generate_job_description_embedding(job_description):
    return generate_embedding(job_description)

def match_resumes(job_description, top_n=5):
    # Generate embedding for the job description
    job_embedding = generate_job_description_embedding(job_description)
    
    # Fetch all resumes and their embeddings
    resumes = fetch_all_resumes()
    
    # Compute similarity scores
    scores = []
    for resume in resumes:
        similarity = cosine_similarity([job_embedding], [resume['embedding']])[0][0]
        scores.append({"id": resume["id"], "name": resume["name"], "score": similarity, "file": resume["ref"]})
        
    # Sort resumes by their similarity scores
    scores= sorted(scores, key=lambda x:x["score"], reverse=True)
    
    # return the top N matches
    return scores[:top_n]

# Display the best matches for a job description
def display_top_matches(job_description, top_n=5):
    matches = match_resumes(job_description, top_n=top_n)
    print(f"\nTop {top_n} Matches for a Job Description:\n")
    for match in matches:
        print(f"Resumes ID: {match['id']}, Name: {match['name']}, Similarity Score: {match['score']:.2f}, File Ref: {match['file']}")
    return matches
        