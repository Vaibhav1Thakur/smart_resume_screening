# Smart Resume Screening System (AI-Powered)

## Project Overview

The Smart Resume Screening System is an AI-powered application that compares resumes against a Job Description (JD) and calculates a relevance score based on skills, experience, and textual similarity.

The system helps recruiters quickly identify suitable candidates by automatically screening resumes and generating match scores.

---

## Features

* Upload Job Description (PDF)
* Upload Resume (PDF)
* Extract Skills from JD and Resume
* Extract Experience Information
* TF-IDF + Cosine Similarity Matching
* Match Score Generation (0-100)
* Matched Skills Identification
* Missing Skills Detection
* Short Explanation Generation
* FastAPI Endpoint for Resume Screening

---

## Tech Stack

* Python
* FastAPI
* PDFPlumber
* Scikit-Learn
* TF-IDF Vectorizer
* Cosine Similarity

---

## Project Structure

smart_resume_screening/

├── app.py

├── resume_matcher.py

├── requirements.txt

├── README.md

└── .gitignore

---

## Installation

1. Clone the repository

git clone <repository-url>

2. Navigate to project folder

cd smart_resume_screening

3. Create virtual environment

python -m venv venv

4. Activate virtual environment

Windows:

venv\Scripts\activate

5. Install dependencies

pip install -r requirements.txt

---

## Run the API

python -m uvicorn app:app --reload

Server will start at:

http://127.0.0.1:8000

Swagger Documentation:

http://127.0.0.1:8000/docs

---

## API Endpoint

POST /screen-resume

Inputs:

* Job Description PDF
* Resume PDF

Output:

* Final Match Score
* Skill Match Score
* TF-IDF Similarity Score
* Experience Score
* Matched Skills
* Missing Skills
* Explanation

---

## Scoring Formula

Final Match Score is calculated using:

Final Score =
(70% × Skill Match Score)
+
(20% × TF-IDF Similarity Score)
+
(10% × Experience Match Score)

---

## Approach

1. Extract text from Job Description PDF.
2. Extract text from Resume PDF.
3. Identify skills from both documents.
4. Extract experience using regular expressions.
5. Convert text into TF-IDF vectors.
6. Calculate cosine similarity.
7. Compute weighted final score.
8. Generate explanation and return results through FastAPI.

---

## Future Improvements

* Automatic Skill Extraction using NLP
* Sentence Transformer Embeddings
* Resume Ranking for Multiple Candidates
* Database Integration
* Cloud Deployment (AWS/Azure)

## Sample Output

{
  "final_match_score": 84.63,
  "skill_match_score": 84.61,
  "tfidf_score": 31.71,
  "experience_score": 100,
  "matched_skills": [
    "python",
    "sql",
    "machine learning"
  ],
  "missing_skills": [
    "aws"
  ],
  "resume_experience": 1,
  "jd_experience": 0,
  "explanation": "Resume matched 11 out of 13 required skills."
}

## Author

Vaibhav Thakur
