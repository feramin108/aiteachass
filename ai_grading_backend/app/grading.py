# app/grading.py
from app.utils import process_text, process_image, process_config_file

def grade_submission(file_content, filename):
    """
    Determine the type of file and grade it accordingly.
    """
    feedback = ""
    grade = 0

    if filename.endswith(".txt") or filename.endswith(".md"):
        feedback, grade = process_text(file_content)
    elif filename.endswith(".png") or filename.endswith(".jpg"):
        feedback, grade = process_image(file_content)
    elif filename.endswith(".conf") or filename.endswith(".ini"):
        feedback, grade = process_config_file(file_content)
    
    return feedback, grade
