from fastapi import FastAPI, UploadFile, File
from resume_matcher import analyze_resume

import os

app = FastAPI(
    title="Smart Resume Screening API"
)


@app.get("/")
def home():

    return {
        "message": "Resume Screening API Running"
    }


@app.post("/screen-resume")
async def screen_resume(
    jd: UploadFile = File(...),
    resume: UploadFile = File(...)
):

    jd_path = f"temp_{jd.filename}"
    resume_path = f"temp_{resume.filename}"

    with open(jd_path, "wb") as f:
        f.write(await jd.read())

    with open(resume_path, "wb") as f:
        f.write(await resume.read())

    result = analyze_resume(
        jd_path,
        resume_path
    )

    if os.path.exists(jd_path):
        os.remove(jd_path)

    if os.path.exists(resume_path):
        os.remove(resume_path)

    return result