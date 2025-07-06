import streamlit as st
from util import extract_text_from_PDF, summarize_text, answer_question, generate_questions
from util import evaluate_answer 
from util import generate_study_notes

# Page Configuration - Professional layout setup
st.set_page_config(
    page_title="Smart Research Assistant", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Load external CSS file for clean styling
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

load_css('styles.css')

# Main Header
st.markdown("""
<div class="main-header">
    <h1>Smart Research Assistant</h1>
    <p>Your AI-powered companion for PDF analysis, summarization, and interactive learning</p>
</div>
""", unsafe_allow_html=True)

# About This Tool Section - Feature description and benefits
st.markdown("""
<div class="about-section">
    <div class="about-header">🚀 About This Tool</div>
    <div class="about-text">
        Transform your research workflow with AI-powered document analysis. Our smart assistant helps you extract insights, generate summaries, and test your understanding of complex documents in minutes.
    </div>
</div>
""", unsafe_allow_html=True)

# Feature Cards Section - Interactive feature overview
st.markdown("""
<div class="features-container">
    <h3>Features</h3>
    <div class="features-grid">
        <div class="feature-card extract-card">
            <h3>📄 Extract</h3>
            <p>Advanced PDF text extraction</p>
        </div>
        <div class="feature-card summarize-card">
            <h3>📝 Summarize</h3>
            <p>AI-powered summaries</p>
        </div>
        <div class="feature-card ask-card">
            <h3>❓ Ask</h3>
            <p>Interactive Q&A system</p>
        </div>
        <div class="feature-card test-card">
            <h3>🎯 Test</h3>
            <p>Challenge your knowledge</p>
        </div>
        <div class="feature-card notes-card">
            <h3>📚 Notes</h3>
            <p>Generate study materials</p>
        </div>
        <div class="feature-card text-input-card">
            <h3>✍️ Text Input</h3>
            <p>Direct text analysis</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Input Section - Multiple ways to provide content
st.markdown("""
<div class="upload-section">
    <h4>Get started with AI-powered analysis</h4>
    <p>Choose your preferred input method below</p>
</div>
""", unsafe_allow_html=True)

# Create tabs for different input methods
input_tab1, input_tab2 = st.tabs(["📄 Upload PDF", "✍️ Enter Text"])

with input_tab1:
    st.markdown("**Upload any PDF file for analysis**")
    uploaded_file = st.file_uploader(
        "Drag and drop file here", 
        type="pdf",
        help="Limit 200MB per file • PDF format",
        label_visibility="collapsed"
    )

with input_tab2:
    st.markdown("**Type or paste your text for analysis**")
    user_text = st.text_area(
        "Enter your text here...",
        height=200,
        placeholder="Paste your article, research paper, notes, or any text you want to analyze...",
        help="You can paste any text content here for AI analysis"
    )
    
    process_text_btn = st.button(
        "Process Text", 
        use_container_width=True,
        disabled=not user_text or not user_text.strip(),
        help="Click to start AI analysis of your text"
    )
    
# Processing Logic - Handle both PDF and text input
raw_text = ""
processing_source = ""

if uploaded_file:
    st.markdown("---")
    processing_source = "PDF"
    
    with st.spinner("Extracting text from PDF..."):
        raw_text = extract_text_from_PDF(uploaded_file.read())

elif user_text and user_text.strip() and process_text_btn:
    st.markdown("---")
    processing_source = "Text Input"
    raw_text = user_text.strip()
    st.success("Text input received successfully!")

if raw_text.strip() != "":
        if processing_source == "PDF":
            st.success("Text extraction completed successfully!")
        
        # Create tabs for different features - Organized interface for better user experience
        tab1, tab2, tab3, tab4 = st.tabs(["Summary", "Ask Questions", "Test Yourself", "Study Notes"])
        
        with tab1:
            st.markdown("### Document Summary")
            with st.spinner("Generating AI-powered summary..."):
                summary = summarize_text(raw_text)
            
            st.markdown(f"""
            <div class="success-message">
                <h4>Summary</h4>
                <p>{summary}</p>
            </div>
            """, unsafe_allow_html=True)

        with tab2:
            st.markdown("### Ask Anything About Your Document")
            user_question = st.text_input("Type your question here...", placeholder="What is the main topic of this document?")
            
            if user_question:
                with st.spinner("Finding the best answer..."):
                    answer = answer_question(user_question, raw_text)
                
                st.markdown(f"""
                <div class="success-message">
                    <h5>AI Answer:</h5>
                    <p>{answer}</p>
                </div>
                """, unsafe_allow_html=True)

        with tab3:
            st.markdown("### Test Your Understanding")
            
            if st.button("Generate Quiz Questions", use_container_width=True):
                with st.spinner("Creating personalized questions..."):
                    questions = generate_questions(summary)
                
                st.session_state.questions = questions
                st.session_state.user_answers = [""] * len(questions)
            
            # Interactive quiz form for knowledge assessment
            if 'questions' in st.session_state:
                with st.form("quiz_form"):
                    st.markdown("#### Answer the following questions:")
                    
                    user_answers = []
                    for idx, q in enumerate(st.session_state.questions[:3]):
                        st.markdown(f"**Question {idx+1}:** {q}")
                        answer = st.text_area(f"Your answer:", key=f"answer_{idx}", height=100)
                        user_answers.append((q, answer))
                    
                    submitted = st.form_submit_button("Submit & Get Feedback", use_container_width=True)
                    
                    if submitted:
                        st.markdown("### Your Results")
                        for i, (q, ans) in enumerate(user_answers):
                            if ans.strip() == "":
                                st.warning(f"Question {i+1}: No answer provided.")
                            else:
                                feedback = evaluate_answer(ans, summary)
                                st.markdown(f"""
                                <div class="question-card">
                                    <h5>Question {i+1}:</h5>
                                    <p><strong>Your Answer:</strong> {ans}</p>
                                    <p><strong>Feedback:</strong> {feedback}</p>
                                </div>
                                """, unsafe_allow_html=True)

        with tab4:
            st.markdown("### Generate Study Notes")
            
            if st.button("Create Study Materials", use_container_width=True):
                with st.spinner("Generating structured study notes..."):
                    notes = generate_study_notes(summary)
                
                # Display notes in a styled container
                st.markdown('<div class="study-notes-container">', unsafe_allow_html=True)
                st.markdown("#### Your Study Notes")
                st.text_area("", value=notes, height=400, disabled=True, key="study_notes_display")
                st.markdown('</div>', unsafe_allow_html=True)
                
                st.download_button(
                    label="Download Notes as .txt",
                    data=notes,
                    file_name="study_notes.txt",
                    mime="text/plain",
                    use_container_width=True
                )
            else:
                if processing_source == "PDF":
                    st.error("No extractable text found in the PDF. Please try a different file.")
                else:
                    st.info("👆 Please upload a PDF file or enter text above to get started with AI analysis!")

# Force text color in disabled text areas using JavaScript
st.markdown("""
<script>
function forceTextColor() {
    const textAreas = document.querySelectorAll('textarea[disabled]');
    textAreas.forEach(textarea => {
        textarea.style.color = '#000000';
        textarea.style.webkitTextFillColor = '#000000';
        textarea.style.background = '#ffffff';
    });
}

// Run after page loads
setTimeout(forceTextColor, 100);

// Run on mutation (when content changes)
const observer = new MutationObserver(forceTextColor);
observer.observe(document.body, { childList: true, subtree: true });
</script>
""", unsafe_allow_html=True)


