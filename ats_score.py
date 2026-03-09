import re
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer('all-MiniLM-L6-v2')


def skill_score(required_skills, candidate_skills):

    matched = set(required_skills).intersection(set(candidate_skills))

    if len(required_skills) == 0:
        return 0

    return (len(matched) / len(required_skills)) * 40


def similarity_score(job_description, resume_text):

    job_embedding = model.encode([job_description])
    resume_embedding = model.encode([resume_text])

    similarity = cosine_similarity(job_embedding, resume_embedding)[0][0]

    return similarity * 30


def extract_experience(text):

    matches = re.findall(r'(\d+)\s+year', text.lower())

    years = [int(x) for x in matches]

    if len(years) == 0:
        return 0

    return sum(years)


def experience_score(candidate_years, required_years):

    if required_years == 0:
        return 0

    if candidate_years >= required_years:
        return 20

    return (candidate_years / required_years) * 20


def quality_score(text):

    score = 0

    text = text.lower()

    if "education" in text:
        score += 3

    if "experience" in text:
        score += 3

    if "skills" in text:
        score += 2

    if "project" in text:
        score += 2

    return score


def calculate_ats(resume_text, job_description, required_skills, candidate_skills, required_years):

    s1 = skill_score(required_skills, candidate_skills)

    s2 = similarity_score(job_description, resume_text)

    years = extract_experience(resume_text)

    s3 = experience_score(years, required_years)

    s4 = quality_score(resume_text)

    final_score = s1 + s2 + s3 + s4

    return round(final_score,2)