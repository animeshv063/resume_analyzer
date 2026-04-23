from fastapi import FastAPI
from backend.utils import analyze_resume

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Resume Analyzer API running"}

@app.post("/analyze")
def analyze(data: dict):
    resume = data.get("resume", "")
    job = data.get("job", "")

    score, matched, missing = analyze_resume(resume, job)

    return {
        "score": score,
        "matched": list(matched),
        "missing": list(missing)
    }
