from resume_parser import extract_text_from_pdf
from skill_extractor import load_skills, extract_skills_from_text
from job_matcher import load_jobs, match_jobs

# Step 1: Extract resume text
text = extract_text_from_pdf("sample_resume.pdf")

# Step 2: Load skills
skills_list = load_skills("../data/skills.csv")

# Step 3: Extract skills from resume
found_skills = extract_skills_from_text(text, skills_list)

print("Extracted Skills:", found_skills)

# Step 4: Load jobs
jobs_df = load_jobs("../data/jobs.csv")

# Step 5: Match jobs
ranked_jobs = match_jobs(found_skills, jobs_df)

print("\nJob Ranking:")
for job, score in ranked_jobs:
    print(f"{job} → {score}% match")