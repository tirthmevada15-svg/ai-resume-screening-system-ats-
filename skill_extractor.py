import spacy
from skill_db import SKILLS_DB

nlp = spacy.load("en_core_web_sm")

def extract_skills(text):

    doc = nlp(text.lower())

    found = []

    for token in doc:

        if token.text in SKILLS_DB:
            found.append(token.text)

    return list(set(found))