import os
import json
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Read resume
with open("resume.txt", "r") as file:
    resume_text = file.read()
    
# Read job description
with open("job_description.txt", "r") as file:
    job_description = file.read()

prompt = f"""
You are a senior recruiter and ATS system.

Compare the candidate's resume with the job description.

Return ONLY valid JSON in this format:

{{
  "match_score": number,
  "strengths": [list],
  "missing_skills": [list],
  "improvements": [list]
}}

Rules:
- match_score must be between 0 and 100
- strengths: max 5 points
- missing_skills: max 5 points
- improvements: max 5 points
- No explanations outside JSON


Resume:
{resume_text}

Job Description:
{job_description}
"""

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {"role": "user", "content": prompt}
    ]
)

output = response.choices[0].message.content

# Clean markdown formatting if present
if output.startswith("```"):
    output = output.strip("```json").strip("```").strip()

# Parse JSON safely
try:
    data = json.loads(output)
    print(json.dumps(data, indent=2))
except:
    print("Error parsing JSON. Raw output:\n")
    print(output)