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
        You are a senior hiring manager + ATS system with experience hiring across consulting firms, product companies, and enterprise environments.

        Evaluate the candidate like a real hiring decision-maker.

        Return ONLY valid JSON in this format:
        
        {{
            "match_score": number,
            "decision": "Strong Fit" | "Moderate Fit" | "Weak Fit",
            "seniority_level": "Junior" | "Mid" | "Senior",
            "shortlist_confidence": "High" | "Medium" | "Low",

            "strengths": [list],
            "critical_gaps": [list],
            "nice_to_have_gaps": [list],

            "keyword_match": {{
            "matched": [list],
            "missing": [list]
            }},

        "risk_flags": [list],

        "improvement_plan": [list],

        "recommended_roles": [list]
        }}
        
        Evaluation Rules:

        1. Use weighted scoring:
        - Core Skills Match (40%)
        - Relevant Experience (25%)
        - Domain Fit (15%)
        - Tools & Technologies (10%)
        - Impact & Communication (10%)

        2. Be strict and realistic (simulate actual recruiter filtering)

        3. Evidence-based evaluation:
        - Every strength or gap must reference resume evidence or say "Not Found"

        4. Critical gaps = likely rejection reasons
        5. Nice-to-have gaps = can be learned on job

        6. Improvement plan must:
        - Be specific
        - Include timeline
        - Include measurable outcome

        7. Recommended roles:
        - Must be realistically achievable TODAY
        
        Resume:
        {resume}
        
        Job Description:
        {job_description}
        
        """
        
        
        
        response = client.chat.completions.create(
            model="gpt-4.1",
            temperature=0.2,
            response_format={"type": "json_object"},
            messages=[
                {"role": "system", "content": "You are a strict ATS and hiring manager."},
                {"role": "user", "content": prompt}
            ]
        )

        try:
            data = json.loads(response.choices[0].message.content)
        except json.JSONDecodeError:
            st.error("AI returned invalid JSON. Try again.")
            st.write(response.choices[0].message.content)
            st.stop()
            
        st.subheader("Analysis Result")
        st.json(data)