from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def rank_resumes(job_description, resumes):

    documents = [job_description] + resumes

    vectorizer = TfidfVectorizer(stop_words='english')
    vectors = vectorizer.fit_transform(documents)

    job_vector = vectors[0]

    resume_vectors = vectors[1:]

    similarity_scores = cosine_similarity(job_vector, resume_vectors)

    scores = similarity_scores.flatten()

    return scores