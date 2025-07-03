import streamlit as st
from util import extract_text_from_PDF, summarize_text, answer_question, generate_questions
from util import evaluate_answer 
from util import generate_study_notes  # make sure it's imported


st.set_page_config(page_title="PDF Summarizer", layout="centered")
st.title("PDF Summarizer")
st.markdown("Upload any PDF file and get a concise summary")

uploaded_file = st.file_uploader("Upload your PDF file", type="pdf")

if uploaded_file:
    st.info("Extracting text from PDF")
    raw_text = extract_text_from_PDF(uploaded_file)

    if raw_text.strip() != "":
        st.success("Text extraction completed")
        st.markdown("Generating summary...")

        with st.spinner("Summarizing..."):
            summary = summarize_text(raw_text)
            st.subheader("Summary")
            st.write(summary)

        # DAY 2: ASK ANYTHING
        st.markdown("---")
        st.header("Ask Anything")
        user_question = st.text_input("Ask a question about the PDF")
        if user_question:
            with st.spinner("Finding answer..."):
                answer = answer_question(user_question, raw_text)
            st.subheader("Answer:")
            st.write(answer)

        # DAY 3: CHALLENGE ME
        st.markdown("---")
        st.header("Challenge Me")
        if st.button("Generate Questions from PDF"):
            with st.spinner("Generating questions..."):
                questions = generate_questions(summary)

            user_answers = []
            for idx, q in enumerate(questions[:3]):
                st.markdown(f"**Q{idx+1}:** {q}")
                answer = st.text_input(f"Your answer for Q{idx+1}", key=f"q{idx}")
                user_answers.append((q, answer))

            #SUBMIT ANSWERS BLOCK

            if st.button("Submit Answers"):
                st.subheader("📊 Feedback:")
                for i, (q, ans) in enumerate(user_answers):
                    st.markdown(f"**Q{i+1}:** {q}")
                    if ans.strip() == "":
                        st.warning("⚠️ No answer provided.")
                    else:
                        feedback = evaluate_answer(ans, summary)  # ← this is what was missing
                        st.write(f"🧠 Your Answer: {ans}")
                        st.write(f"📝 Feedback: {feedback}")
    else:
        st.warning("No extractable text found in the PDF.")


#notes generator
st.markdown("---")
st.header("📝 Generate Study Notes")

if st.button("Generate Notes from Summary"):
    with st.spinner("Generating structured notes..."):
        notes = generate_study_notes(summary)
        st.text_area("📄 Auto-Generated Notes", value=notes, height=300)

        st.download_button(
            label="📥 Download Notes as .txt",
            data=notes,
            file_name="study_notes.txt",
            mime="text/plain"
        )
