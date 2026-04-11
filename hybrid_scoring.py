from scoring import compute_rule_score
from feature_extraction import extract_features

def read_text_file(file_path):
    with open(file_path, "r") as file:
        return file.read()

def compute_hybrid_score(resume_text, job_description, llm_score):
    resume_features = extract_features(resume_text)
    job_features = extract_features(job_description)

    rule_scores = compute_rule_score(resume_features, job_features)
    rule_score = rule_scores["final_rule_score"]

    final_score = 0.6 * llm_score + 0.4 * rule_score

    return {
        "llm_score": llm_score,
        "rule_score": rule_score,
        "final_score": final_score,
        "breakdown": rule_scores
    }
    
def normalize_llm_score(llm_score):
    # If score is > 1, assume it's percentage
    if llm_score > 1:
        return llm_score / 100
    return llm_score


# ---- TEST ----
if __name__ == "__main__":

    # Read from files
    resume_text = read_text_file("resume.txt")
    job_description = read_text_file("job_description.txt")

    # From your LLM output
    llm_score = 66  
    llm_score = normalize_llm_score(llm_score)

    result = compute_hybrid_score(resume_text, job_description, llm_score)

    print("Hybrid Score Output:", result)