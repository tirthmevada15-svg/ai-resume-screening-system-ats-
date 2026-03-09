# AI Resume Screening System (ATS)

An AI-powered Resume Screening System built using **Python and Streamlit** that automatically analyzes resumes and ranks candidates based on how well they match a given job description.

The system extracts text from resumes, identifies candidate skills using NLP, calculates an ATS score, and ranks candidates automatically. This helps recruiters quickly identify the most suitable candidates.

---

# Features

- Upload multiple resumes (PDF or DOCX)
- Extract text automatically from resumes
- Identify candidate skills using NLP
- Match resumes with job description
- Calculate ATS score out of 100
- Rank candidates automatically
- Interactive web interface using Streamlit

---

# Project Workflow

1. Upload resumes through the Streamlit interface.
2. Enter the job description.
3. Provide required skills and required experience.
4. The system processes each resume:
   - Extracts text from the resume.
   - Identifies skills from the resume.
   - Compares resume with job description.
5. ATS score is calculated.
6. Candidates are ranked automatically.

---


---

# Technologies Used

- Python
- Streamlit
- Natural Language Processing (NLP)
- Sentence Transformers
- Scikit-learn
- SpaCy
- PDFMiner
- Python-docx
- Pandas

---

# ATS Scoring Logic

The ATS score is calculated using four components:

| Component | Score |
|----------|------|
| Skill Matching | 40 |
| Resume Similarity with Job Description | 30 |
| Experience Match | 20 |
| Resume Quality | 10 |
| **Total Score** | **100** |

The final ATS score is calculated by combining all four components.

---

# Resume Parsing

The system supports two resume formats:

- PDF
- DOCX

The resume parser extracts text from these files and converts it into readable format for analysis.

---

# Skill Extraction

Skills are extracted using **SpaCy NLP** and matched with a predefined skill database.

Example skills included in the database:

- Python
- Machine Learning
- Deep Learning
- TensorFlow
- PyTorch
- SQL
- Pandas
- NumPy
- Scikit-learn
- Docker
- AWS
- Data Analysis

---

# Requirements

Install all required libraries using: pip install -r requirements.txt

Dependencies used in the project:

- streamlit
- pandas
- scikit-learn
- pdfminer.six
- python-docx
- spacy
- sentence-transformers
