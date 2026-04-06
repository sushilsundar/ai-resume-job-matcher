# AI Resume Job Matcher

## Overview

AI Resume Job Matcher is a Python-based application that analyzes a candidate’s resume against a specific job description.
It provides structured insights to help job seekers understand their alignment with a role and identify areas for improvement.

---

## Problem Statement

Job applicants often receive little to no feedback on why their applications are unsuccessful.
This project addresses that gap by offering a clear comparison between a resume and a job description, highlighting mismatches and actionable improvements.

---

## Features

* Resume analysis based on industry expectations
* Job description comparison
* Match score estimation
* Identification of missing or weak skill areas
* Targeted suggestions to improve alignment

---

## Tech Stack

* Python
* OpenAI API
* File-based input handling (`.txt`)

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

## How It Works

1. The application reads resume content from a text file
2. It reads a job description provided by the user
3. Both inputs are sent to an AI model for analysis
4. The system returns:

   * Match score
   * Key strengths
   * Missing skills
   * Suggested improvements

---

## Setup & Run

1. Clone the repository
2. Set your OpenAI API key as an environment variable:

```bash
export OPENAI_API_KEY="your_api_key_here"
```

3. Add your files:

* `resume.txt`
* `job_description.txt`

4. Run the application:

```bash
python app.py
```

---

## Current Status

This project is under active development.
Upcoming improvements include structured scoring logic, enhanced prompt design, and a user interface.

---

## Future Enhancements

* Streamlit-based UI
* Support for PDF/DOCX resumes
* Improved ATS-style scoring system
* Deployment as a web application

---

## Sample Output

Match Score: 75/100

Key Strengths:
- Strong Python and data analysis skills
- Experience with machine learning models

Missing Skills:
- Agile methodologies
- BI tools (Power BI, Tableau)

Improvements:
- Add project experience with dashboards
- Highlight Agile workflow exposure

---

## Author

Sushil Sundar
