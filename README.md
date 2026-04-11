# AI Resume Job Matcher

## Overview

AI Resume Job Matcher is a Python-based application that analyzes a candidate’s resume against a specific job description.
It provides structured insights to help job seekers understand their alignment with a role and identify areas for improvement.

---

## Problem Statement

Job applicants often receive little to no feedback on why their applications are unsuccessful.
This project addresses that gap by offering a clear comparison between a resume and a job description, highlighting mismatches and actionable improvements.

---

## Demo

![App Screenshot](screenshot.png)

## Features

* Resume analysis based on industry expectations
* Job description comparison
* Match score estimation
* Identification of missing or weak skill areas
* Targeted suggestions to improve alignment
* User-friendly display of results optimised JSON output
* Interactive UI using Streamlit

---

## Tech Stack

* Python
* OpenAI API
* File-based input handling (`.txt`)

---

## Architecture Evolution

The system is evolving from a purely LLM-based approach to a hybrid architecture:

### Phase 1 (Completed)
- LLM-based resume-job matching
- Structured JSON outputs
- Streamlit UI

### Phase 2 (In Progress)
- Feature Extraction Layer (deterministic)
- Rule-Based Scoring
- Hybrid scoring (LLM + rules)

This evolution improves:
- Consistency across runs
- Explainability of scores
- Production readiness

---

## Project Structure

```
ai-resume-job-matcher/
├── app.py
├── resume.txt
├── job_description.txt
├── requirements.txt
└── README.md
```

---

## Feature Extraction Layer

This module extracts structured information from resumes and job descriptions.

### Extracted Features:
- Skills (predefined tech stack matching)
- Years of experience (regex-based heuristic)
- Keywords (basic text extraction)

This layer enables deterministic scoring and supports hybrid evaluation.

---

## Rule-Based Scoring

Introduced a deterministic scoring mechanism based on:

- Skill overlap (primary signal)
- Keyword similarity (supporting signal)
- Experience match

A weighted score is computed to provide a consistent baseline independent of LLM responses.

---

## How It Works

The system follows a multi-stage pipeline:

1. **Input Processing**
   - Reads resume and job description from text files

2. **Feature Extraction Layer**
   - Extracts structured data:
     - Skills
     - Years of experience (heuristic)
     - Keywords

3. **LLM-Based Analysis**
   - Uses OpenAI API to generate:
     - Match score
     - Strengths
     - Gaps
     - Improvements

4. **(New) Rule-Based Scoring**
   - Computes deterministic scores using:
     - Skill overlap
     - Keyword similarity
     - Experience match

5. **(Upcoming) Hybrid Scoring**
   - Combines LLM + rule-based scores for improved reliability and consistency

6. **Output**
   - Structured JSON response displayed via Streamlit UI

---

## Setup & Run

1. Clone the repository

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set your OpenAI API key as an environment variable:

```bash
export OPENAI_API_KEY="your_api_key_here"
```

4. Add your input files:

* `resume.txt`
* `job_description.txt`

5. Run the CLI version:

```bash
python app.py
```

6. Run the UI (recommended):

```bash
streamlit run streamlit_app.py
```

---

## Current Status

This project is actively evolving into a production-grade system.

Recent updates:
- Feature extraction layer implemented
- Rule-based scoring introduced
- Hybrid scoring architecture in progress

Next steps:
- Embedding-based similarity
- Improved explainability
- Deployment readiness

---

## Future Enhancements

- Embedding-based similarity scoring
- Advanced NLP-based feature extraction (NER, skill parsing)
- Weight tuning and evaluation metrics
- Support for PDF/DOCX resumes
- Full-stack deployment

---

## Sample Output

```json
{
  "match_score": 85,
  "strengths": [
    "Strong Python skills with Pandas, NumPy, and Scikit-learn",
    "Experience in machine learning including classification and regression models",
    "Proficient in SQL including SAP HANA and query optimization"
  ],
  "missing_skills": [
    "Experience with cloud platforms (AWS, Azure, GCP)",
    "Big data technologies such as Hadoop or Spark",
    "Dashboarding tools like Power BI or Tableau"
  ],
  "improvements": [
    "Add measurable impact metrics to projects",
    "Highlight team collaboration and Agile experience",
    "Include relevant certifications"
  ]
}
```



---

## Author

Sushil Sundar
