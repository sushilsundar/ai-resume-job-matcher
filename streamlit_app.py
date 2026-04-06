import streamlit as st
import os
import json
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("AI Resume Job Matcher")
st.markdown("### Analyze your resume against a job description")

col1, col2 = st.columns(2)

with col1:
    resume = st.text_area("Resume", height=300)

with col2:
    job_description = st.text_area("Job Description", height=300)
    
st.markdown("---")

if st.button("Analyze"):
    
    if not resume or not job_description:
        st.warning("Please provide both resume and job description")
        
    else:
        
        prompt = f"""
        You are a senior recruiter and ATS system.

        Compare the candidate's resume with the job description.

        Return ONLY valid JSON in this format:
        
        {{
            "match_score" : number,
            "strengths" : [list],
            "missing_skills" : [list],
            "improvements" : [list] 
            
        }}
        
        Rules:
        - match_score must be between 0 and 100
        - max 5 items per list
        - Nothing beyond JSON
        
        Resume:
        {resume}
        
        Job Description:
        (job_description)
        """
        
        
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        output = response.choices[0].message.content

        # Clean markdown
        if "```" in output:
            output = output.split("```")[1]

        try:
            data = json.loads(output)

            st.subheader("Match Score")
            st.write(data["match_score"])

            st.subheader("Strengths")
            for item in data.get("strengths", []):
                st.success(f"✔ {item}")

            st.subheader("Missing Skills")
            for item in data.get("missing_skills", []):
                st.error(f"✘ {item}")

            st.subheader("Improvements")
            for item in data.get("improvements", []):
                st.info(f"➤ {item}")

        except:
            st.error("Error parsing response")
            st.write(output)