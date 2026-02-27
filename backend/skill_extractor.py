import pandas as pd

def load_skills(file_path):
    skills = pd.read_csv(file_path, header=None)
    return skills[0].tolist()

def extract_skills_from_text(text, skills_list):
    found_skills = []

    text_lower = text.lower()

    for skill in skills_list:
        if skill.lower() in text_lower:
            found_skills.append(skill)

    return found_skills
