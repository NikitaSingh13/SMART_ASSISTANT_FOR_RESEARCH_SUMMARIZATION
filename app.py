import streamlit as st
from util import extract_text_from_PDF, summarize_text

st.set_page_config(page_title="PDF Summarizer", layout="centered")
st.title("PDF summarizer")
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
    else:
        st.warning("No extractable text found in the PDF.")
