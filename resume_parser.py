import pdfminer.high_level
import docx

def extract_text_from_pdf(file):
    return pdfminer.high_level.extract_text(file)

def extract_text_from_docx(file):

    doc = docx.Document(file)

    text = []

    for para in doc.paragraphs:
        text.append(para.text)

    return "\n".join(text)

def extract_resume_text(uploaded_file):

    if uploaded_file.name.endswith(".pdf"):
        return extract_text_from_pdf(uploaded_file)

    elif uploaded_file.name.endswith(".docx"):
        return extract_text_from_docx(uploaded_file)

    else:
        return ""