import streamlit as st
import os
import json
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("AI Resume Job Matcher")

resume = st.text_area("Paste Resume here")
job_description = st.text_area("Paste Job Description here")

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
            st.write(data["strengths"])

            st.subheader("Missing Skills")
            st.write(data["missing_skills"])

            st.subheader("Improvements")
            st.write(data["improvements"])

        except:
            st.error("Error parsing response")
            st.write(output)