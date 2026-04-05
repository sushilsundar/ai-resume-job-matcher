from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
with open("resume.txt", "r") as file:
    resume_text = file.read()

prompt = f"""
You are a career coach.

Analyze this resume for software/data roles.

Give:
1. Strengths
2. Missing skills
3. Specific improvements

Resume:
{resume_text}
"""

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {"role": "user", "content": prompt}
    ]
)

print(response.choices[0].message.content)