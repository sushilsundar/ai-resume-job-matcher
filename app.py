import os
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

Give:
1. Match score (out of 100)
2. Key matching strengths
3. Missing skills (important)
4. Specific improvements to increase match


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

print(response.choices[0].message.content)