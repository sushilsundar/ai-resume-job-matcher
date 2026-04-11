def skill_overlap_score(resume_skills, job_skills):
    if not job_skills:
        return 0
    
    matched = set(resume_skills).intersection(set(job_skills))
    return len(matched) / len(job_skills)


def keyword_match_score(resume_keywords, job_keywords):
    if not job_keywords:
        return 0

    matched = set(resume_keywords).intersection(set(job_keywords))
    return len(matched) / len(job_keywords)


def experience_score(resume_exp, job_exp):
    if job_exp == 0:
        return 1  # no requirement
    
    return min(resume_exp / job_exp, 1)


def compute_rule_score(resume_features, job_features):
    skill_score = skill_overlap_score(
        resume_features["skills"], job_features["skills"]
    )

    keyword_score = keyword_match_score(
        resume_features["keywords"], job_features["keywords"]
    )

    exp_score = experience_score(
        resume_features["experience_years"],
        job_features["experience_years"]
    )

    # Weighted scoring (you can tune later)
    final_score = (
        0.5 * skill_score +
        0.3 * keyword_score +
        0.2 * exp_score
    )

    return {
        "skill_score": skill_score,
        "keyword_score": keyword_score,
        "experience_score": exp_score,
        "final_rule_score": final_score
    }


# ---- TEST ----
if __name__ == "__main__":
    from feature_extraction import extract_features

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

    scores = compute_rule_score(resume_features, job_features)

    print("Rule-Based Scores:", scores)