import pandas as pd

def load_jobs(file_path):
    jobs = pd.read_csv(file_path, header=None)
    return jobs


def match_jobs(found_skills, jobs_df):
    job_results = []

    for index, row in jobs_df.iterrows():
        job_title = row[0]
        job_skills = [skill.strip() for skill in row[1].split(",")]

        match_count = 0
        for skill in found_skills:
            if skill in job_skills:
                match_count += 1

        if len(job_skills) > 0:
            match_percentage = (match_count / len(job_skills)) * 100
        else:
            match_percentage = 0

        job_results.append((job_title, round(match_percentage, 2)))

    job_results.sort(key=lambda x: x[1], reverse=True)

    return job_results