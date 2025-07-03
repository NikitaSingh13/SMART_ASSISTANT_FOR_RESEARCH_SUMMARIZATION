import fitz  # PyMuPDF
from transformers import pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Summarizer
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def extract_text_from_PDF(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    return "".join([page.get_text() for page in doc])

def summarize_text(text):
    if len(text) > 3000:
        text = text[:3000]
    result = summarizer(text, max_length=150, min_length=50, do_sample=False)
    return result[0]['summary_text']

# Ask Anything
qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

def answer_question(question, context):
    result = qa_pipeline(question=question, context=context)
    return result['answer']

# Question Generator (prompt-based, not model-based)
import re
import random
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
from collections import Counter

def generate_questions(summary_text):
    # Clean and extract words
    words = re.findall(r'\b\w{5,}\b', summary_text.lower())  # only longer words
    words = [w for w in words if w not in ENGLISH_STOP_WORDS]

    top_words = [word for word, _ in Counter(words).most_common(5)]

    # Generate questions from those keywords
    templates = [
        f"What do you understand by the term '{top_words[0]}'?",
        f"How is '{top_words[1]}' related to the topic discussed?",
        f"Explain the importance of '{top_words[2]}' in the context of the document.",
        f"Can you describe how '{top_words[3]}' affects the problem or solution?",
        f"Summarize the role of '{top_words[4]}' based on the summary."
    ]

    return templates[:3]


# Answer Evaluation
def evaluate_answer(user_answer, reference_context):
    vectorizer = TfidfVectorizer().fit_transform([user_answer, reference_context])
    score = cosine_similarity(vectorizer[0], vectorizer[1])[0][0]
    if score > 0.7:
        return f"✅ Good answer! (Score: {score:.2f})"
    elif score > 0.4:
        return f"⚠️ Partial match. Try adding more detail. (Score: {score:.2f})"
    else:
        return f"❌ Not quite right. Recheck the material. (Score: {score:.2f})"


#day 4: notes generator
def generate_study_notes(summary):
    # Basic NLP structure from summary
    notes = []

    # Title
    notes.append("Study Notes\n")

    # Break into points
    lines = summary.split(". ")
    for line in lines:
        line = line.strip()
        if len(line) > 10:
            if ":" in line:
                notes.append(f" {line}")
            else:
                notes.append(f" {line}")

    # Add a final takeaway
    notes.append("\n✅ Key Takeaway: Understand the above points for exam/interview prep.")

    return "\n".join(notes)
