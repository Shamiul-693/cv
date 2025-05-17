import streamlit as st
import PyPDF2
import docx
from io import StringIO
import re

# Function to extract text from PDF
def extract_text_from_pdf(uploaded_file):
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    text = ''
    for page in range(len(pdf_reader.pages)):
        text += pdf_reader.pages[page].extract_text()
    return text

# Function to extract text from DOCX
def extract_text_from_docx(uploaded_file):
    doc = docx.Document(uploaded_file)
    text = ''
    for para in doc.paragraphs:
        text += para.text + '\n'
    return text

# Function to analyze CV content (Strengths, Weaknesses, and Advice)
def analyze_cv(text):
    # Example simple analysis (you can expand this as needed)
    strengths_keywords = ['strong', 'expert', 'skilled', 'proficient', 'leadership', 'successful']
    weaknesses_keywords = ['improve', 'develop', 'need', 'work on', 'struggle']
    advice_keywords = ['recommend', 'advice', 'suggest', 'improve', 'focus on']

    strengths = [word for word in strengths_keywords if word in text.lower()]
    weaknesses = [word for word in weaknesses_keywords if word in text.lower()]
    advice = [word for word in advice_keywords if word in text.lower()]

    # Prepare responses
    strength_analysis = "Strengths: " + ", ".join(strengths) if strengths else "No clear strengths identified."
    weakness_analysis = "Weaknesses: " + ", ".join(weaknesses) if weaknesses else "No clear weaknesses identified."
    advice_analysis = "Advice: " + ", ".join(advice) if advice else "No specific advice mentioned."

    return strength_analysis, weakness_analysis, advice_analysis

# Streamlit UI
def main():
    st.title('CV Analyzer')

    # Upload CV file (PDF or DOCX)
    uploaded_file = st.file_uploader("Upload your CV (PDF or DOCX)", type=["pdf", "docx"])

    if uploaded_file is not None:
        # Extract text based on file type
        if uploaded_file.type == "application/pdf":
            cv_text = extract_text_from_pdf(uploaded_file)
        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            cv_text = extract_text_from_docx(uploaded_file)

        # Display extracted text
        st.subheader("Extracted CV Content:")
        st.text(cv_text)

        # Perform analysis
        strength_analysis, weakness_analysis, advice_analysis = analyze_cv(cv_text)

        # Display analysis results
        st.subheader("CV Analysis")
        st.write(strength_analysis)
        st.write(weakness_analysis)
        st.write(advice_analysis)

if __name__ == "__main__":
    main()
