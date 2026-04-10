import re

# Example skill list (can expand later or externalize)
SKILL_SET = [
    "python", "sql", "machine learning", "data analysis",
    "pandas", "numpy", "tensorflow", "pytorch",
    "excel", "tableau", "power bi", "aws"
]


def extract_skills(text):
    text = text.lower()
    found_skills = []

    for skill in SKILL_SET:
        if skill in text:
            found_skills.append(skill)

    return list(set(found_skills))


def extract_experience(text):
    """
    Very basic heuristic:
    Looks for patterns like '3 years', '5+ years'
    """
    matches = re.findall(r'(\d+)\+?\s+years', text.lower())

    if matches:
        return max([int(x) for x in matches])
    
    return 0


def extract_keywords(text):
    """
    Simple keyword extraction:
    - Split words
    - Remove short words
    """
    words = re.findall(r'\b[a-zA-Z]{4,}\b', text.lower())
    return list(set(words))


def extract_features(text):
    return {
        "skills": extract_skills(text),
        "experience_years": extract_experience(text),
        "keywords": extract_keywords(text)
    }


# ---- TEST ----

if __name__ == "__main__":
    resume_text = """
    I have 3 years of experience in Python, SQL, and Machine Learning.
    Worked with Pandas and Tableau for data analysis.
    """

    job_description = """
    Looking for a Data Scientist with experience in Python, SQL, AWS, and Machine Learning.
    Minimum 2 years of experience required.
    """

    resume_features = extract_features(resume_text)
    job_features = extract_features(job_description)

    print("Resume Features:", resume_features)
    print("Job Features:", job_features)