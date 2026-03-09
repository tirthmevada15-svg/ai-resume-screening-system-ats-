import streamlit as st
import pandas as pd

from resume_parser import extract_resume_text
from skill_extractor import extract_skills
from ats_score import calculate_ats


st.title("AI Resume Screening System (ATS)")

st.write("Upload resumes and calculate ATS score")

job_description = st.text_area("Enter Job Description")

required_skills_input = st.text_input("Required Skills (comma separated)")

required_years = st.number_input("Required Experience (years)",0,20,1)

uploaded_files = st.file_uploader(
    "Upload Resumes",
    accept_multiple_files=True
)


if st.button("Analyze Resumes"):

    required_skills = [s.strip().lower() for s in required_skills_input.split(",")]

    results = []

    for file in uploaded_files:

        resume_text = extract_resume_text(file)

        candidate_skills = extract_skills(resume_text)

        score = calculate_ats(
            resume_text,
            job_description,
            required_skills,
            candidate_skills,
            required_years
        )

        results.append({
            "Candidate": file.name,
            "ATS Score": score,
            "Skills": ", ".join(candidate_skills)
        })

    df = pd.DataFrame(results)

    df = df.sort_values(
        by="ATS Score",
        ascending=False
    )

    st.subheader("Candidate Ranking")

    st.dataframe(df)