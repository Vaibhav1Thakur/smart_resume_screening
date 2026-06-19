import pdfplumber
import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


SKILLS_DB = [
    "python",
    "sql",
    "mysql",
    "power bi",
    "excel",
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "tensorflow",
    "keras",
    "pytorch",
    "nlp",
    "data science",
    "data analysis",
    "pandas",
    "numpy",
    "matplotlib",
    "seaborn",
    "scikit-learn",
    "fastapi",
    "flask",
    "aws",
    "git",
    "github",
    "docker",
    "tableau",
    "statistics",
    "opencv"
]


def extract_text_from_pdf(pdf_path):

    text = ""

    with pdfplumber.open(pdf_path) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + " "

    return text.lower()


def extract_skills(text):

    skills = []

    for skill in SKILLS_DB:

        if skill.lower() in text:
            skills.append(skill)

    return sorted(list(set(skills)))


def extract_experience(text):

    patterns = [
        r'(\d+)\+?\s*years',
        r'(\d+)\+?\s*yrs',
        r'(\d+)\+?\s*year',
        r'(\d+)\+?\s*yr'
    ]

    years = []

    for pattern in patterns:

        matches = re.findall(pattern, text)

        for match in matches:
            years.append(int(match))

    if years:
        return max(years)

    return 0


def calculate_tfidf_similarity(jd_text, resume_text):

    vectorizer = TfidfVectorizer(stop_words="english")

    vectors = vectorizer.fit_transform(
        [jd_text, resume_text]
    )

    similarity = cosine_similarity(
        vectors[0:1],
        vectors[1:2]
    )[0][0]

    return round(similarity * 100, 2)


def analyze_resume(jd_pdf, resume_pdf):

    jd_text = extract_text_from_pdf(jd_pdf)

    resume_text = extract_text_from_pdf(resume_pdf)

    jd_skills = extract_skills(jd_text)

    resume_skills = extract_skills(resume_text)

    matched_skills = sorted(
        list(set(jd_skills).intersection(set(resume_skills)))
    )

    missing_skills = sorted(
        list(set(jd_skills) - set(resume_skills))
    )

    if len(jd_skills) > 0:

        skill_score = (
            len(matched_skills)
            / len(jd_skills)
        ) * 100

    else:

        skill_score = 0

    tfidf_score = calculate_tfidf_similarity(
        jd_text,
        resume_text
    )

    resume_exp = extract_experience(
        resume_text
    )

    jd_exp = extract_experience(
        jd_text
    )

    if jd_exp == 0:

        experience_score = 100

    else:

        experience_score = min(
            (resume_exp / jd_exp) * 100,
            100
        )

    final_score = round(
        (0.70 * skill_score)
        +
        (0.20 * tfidf_score)
        +
        (0.10 * experience_score),
        2
    )

    explanation = (
        f"Resume matched {len(matched_skills)} out of "
        f"{len(jd_skills)} required skills. "
        f"TF-IDF similarity is {tfidf_score}%. "
        f"Candidate experience detected: {resume_exp} years. "
        f"Overall Final Match Score = {final_score}%."
    )

    result = {
        "final_match_score": final_score,
        "skill_match_score": round(skill_score, 2),
        "tfidf_score": tfidf_score,
        "experience_score": round(experience_score, 2),
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "resume_experience": resume_exp,
        "jd_experience": jd_exp,
        "explanation": explanation
    }

    return result