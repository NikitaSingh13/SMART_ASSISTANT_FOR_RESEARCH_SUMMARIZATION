import fitz  # PyMuPDF
from transformers import pipeline

# Load Hugging Face summarizer
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def extract_text_from_PDF(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    full_text = ""
    for page in doc:
        full_text += page.get_text()
    return full_text

def summarize_text(text):
    if len(text) > 3000:
        text = text[:3000]
    result = summarizer(text, max_length=150, min_length=50, do_sample=False)
    return result[0]['summary_text']
