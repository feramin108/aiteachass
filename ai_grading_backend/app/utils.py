# app/utils.py
import spacy
import pytesseract
from PIL import Image
from io import BytesIO

# Load a pre-trained NLP model (e.g., English model)
nlp = spacy.load("en_core_web_sm")

def process_text(text):
    """
    Analyze student text report using NLP and provide feedback.
    """
    doc = nlp(text.decode("utf-8"))
    # Sample grading logic (basic word count)
    word_count = len(doc)
    feedback = f"Your report has {word_count} words."

    # Simple grading logic based on word count
    grade = min(100, max(0, word_count // 10))  # Grade out of 100
    

def process_image(image_content):
    """
    Extract text from images using OCR and analyze for grading.
    """
    image = Image.open(BytesIO(image_content))
    text = pytesseract.image_to_string(image)

    # Apply the same logic as text files
    feedback, grade = process_text(text.encode("utf-8"))
    return feedback, grade
