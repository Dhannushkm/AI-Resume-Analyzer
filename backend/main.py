from fastapi import FastAPI, UploadFile, File
import shutil
import os

from resume_parser import extract_text_from_pdf
from skill_extractor import load_skills, extract_skills_from_text
from job_matcher import load_jobs, match_jobs
from semantic_matcher import semantic_job_match


app = FastAPI()

@app.get("/")
def home():
    return {"message": "Backend is working!"}


@app.post("/analyze")
async def analyze_resume(file: UploadFile = File(...)):

    # Save uploaded file temporarily
    file_location = f"temp_{file.filename}"
    
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Extract text
    text = extract_text_from_pdf(file_location)
    text = text.lower()

    # Extract skills
    skills_list = load_skills("../data/skills.csv")
    found_skills = extract_skills_from_text(text, skills_list)

    # Match jobs
    jobs_df = load_jobs("../data/jobs.csv")
    ranked_jobs = semantic_job_match(text, jobs_df)


    # Remove temporary file
    os.remove(file_location)

    return {
        "skills": found_skills,
        "job_ranking": [
            {"title": job, "score": score}
            for job, score in ranked_jobs
        ]
    }
