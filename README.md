# Smart Research Assistant

An AI-powered research companion that transforms your document analysis workflow with intelligent PDF processing, text summarization, and interactive learning features.


## 📋 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)
- [API Reference](#api-reference)
- [Contributing](#contributing)
- [License](#license)

## 🔍 Overview

Smart Research Assistant is a comprehensive tool designed to help researchers, students, and professionals analyze documents efficiently. It combines state-of-the-art AI models with an intuitive user interface to provide:

- **PDF Text Extraction**: Advanced PDF processing with PyMuPDF
- **AI-Powered Summarization**: Intelligent document summarization using DistilBART
- **Interactive Q&A**: Question-answering system powered by DistilBERT
- **Knowledge Testing**: Auto-generated quiz questions to test comprehension
- **Study Notes Generation**: Structured note creation from document content
- **Text Input Support**: Direct text analysis without file upload

## ✨ Features

### 📄 Extract
- Advanced PDF text extraction using PyMuPDF
- Support for various PDF formats and sizes (up to 200MB)
- Robust handling of complex document layouts

### 📝 Summarize
- AI-powered document summarization
- Configurable summary length and detail level
- Maintains key information while reducing content length

### ❓ Ask
- Interactive question-answering system
- Natural language query processing
- Context-aware responses based on document content

### 🎯 Test
- Automatic quiz question generation
- Intelligent answer evaluation using TF-IDF similarity
- Personalized feedback and scoring

### 📚 Notes
- Structured study notes generation
- Downloadable text format
- Organized content for easy review

### ✍️ Text Input
- Direct text analysis without file upload
- Support for pasted content from various sources
- Real-time processing and analysis

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd SMART_ASSISTANT_FOR_RESEARCH_SUMMARIZATION
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirement.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Access the application**
   Open your browser and navigate to `http://localhost:8501`

## 💻 Usage

### Getting Started

1. **Launch the Application**
   - Run `streamlit run app.py` in your terminal
   - Open the provided local URL in your browser

2. **Choose Input Method**
   - **PDF Upload**: Drag and drop or browse for PDF files
   - **Text Input**: Paste or type text directly into the text area

3. **Analyze Content**
   - **Summary Tab**: Get AI-generated summaries
   - **Ask Questions Tab**: Query specific information
   - **Test Yourself Tab**: Take auto-generated quizzes
   - **Study Notes Tab**: Generate and download structured notes

### Example Workflow

```python
# 1. Upload a research paper PDF
uploaded_file = st.file_uploader("Upload PDF", type="pdf")

# 2. Extract and summarize
summary = summarize_text(extracted_text)

# 3. Ask questions
answer = answer_question("What is the main finding?", extracted_text)

# 4. Generate quiz questions
questions = generate_questions(summary)

# 5. Create study notes
notes = generate_study_notes(summary)
```

## 📁 Project Structure

```
SMART_ASSISTANT_FOR_RESEARCH_SUMMARIZATION/
│
├── app.py                 # Main Streamlit application
├── util.py               # Core utility functions
├── styles.css            # Custom CSS styling
├── requirement.txt       # Project dependencies
├── README.md            # Project documentation
└── __pycache__/         # Python cache files
    └── util.cpython-313.pyc
```

### File Descriptions

- **`app.py`**: Main application file containing the Streamlit interface and user interaction logic
- **`util.py`**: Utility functions for PDF processing, text analysis, and AI model operations
- **`styles.css`**: Custom CSS for professional UI styling and responsive design
- **`requirement.txt`**: List of all Python package dependencies

## 📦 Dependencies

### Core Libraries
- **Streamlit (≥1.28.0)**: Web application framework
- **PyMuPDF (≥1.23.0)**: PDF text extraction
- **Transformers (≥4.30.0)**: Hugging Face AI models
- **PyTorch (≥2.0.0)**: Deep learning framework
- **Scikit-learn (≥1.3.0)**: Machine learning utilities
- **NumPy (≥1.24.0)**: Numerical computing

### AI Models Used
- **DistilBART-CNN**: Document summarization
- **DistilBERT-SQuAD**: Question answering
- **TF-IDF Vectorizer**: Answer evaluation

## 🔧 API Reference

### Core Functions

#### PDF Processing
```python
def extract_text_from_PDF(pdf_file):
    """Extract text content from PDF file"""
    # Returns: String containing extracted text
```

#### Text Summarization
```python
def summarize_text(text):
    """Generate AI-powered summary of input text"""
    # Parameters: text (str) - Input text to summarize
    # Returns: String containing summary
```

#### Question Answering
```python
def answer_question(question, context):
    """Answer questions based on provided context"""
    # Parameters: question (str), context (str)
    # Returns: String containing answer
```

#### Quiz Generation
```python
def generate_questions(summary_text):
    """Generate quiz questions from summary"""
    # Parameters: summary_text (str)
    # Returns: List of question strings
```

#### Answer Evaluation
```python
def evaluate_answer(user_answer, reference_context):
    """Evaluate user answers using similarity scoring"""
    # Parameters: user_answer (str), reference_context (str)
    # Returns: String containing feedback and score
```

#### Study Notes
```python
def generate_study_notes(summary):
    """Create structured study notes from summary"""
    # Parameters: summary (str)
    # Returns: String containing formatted notes
```

## 🎨 UI Features

- **Responsive Design**: Adapts to different screen sizes
- **Professional Styling**: Clean, modern interface
- **Interactive Elements**: Hover effects and smooth transitions
- **Color-Coded Features**: Different colors for each feature card
- **Tabbed Interface**: Organized content with easy navigation

## 🚀 Performance Optimization

- **Efficient PDF Processing**: Optimized text extraction
- **Model Caching**: Reduced loading times for AI models
- **Chunked Processing**: Handles large documents efficiently
- **Memory Management**: Optimized for resource usage

## 🛠️ Customization

### Styling
Modify `styles.css` to customize:
- Color schemes
- Layout dimensions
- Animation effects
- Typography

### AI Models
Update `util.py` to use different models:
- Change summarization models
- Adjust question-answering models
- Modify evaluation algorithms


