# app/main.py
from fastapi import FastAPI, UploadFile, File
from app.grading import grade_submission

app = FastAPI()

@app.post("/grade/")
async def grade_assignment(file: UploadFile = File(...)):
    """
    Endpoint to grade student assignments.
    Accepts files (text, config, images) and returns grades with feedback.
    """
    contents = await file.read()
    feedback, grade = grade_submission(contents, file.filename)
    return {"feedback": feedback, "grade": grade}

@app.get("/")
async def root():
    return {"message": "AI Grading System Ready"}
