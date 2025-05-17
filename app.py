import streamlit as st
import PyPDF2
import docx

# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

# Function to extract text from DOCX (Word) file
def extract_text_from_docx(docx_file):
    doc = docx.Document(docx_file)
    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text

# Function to analyze CV content
def analyze_cv(cv_text):
    strengths = []
    weaknesses = []
    advice = []

    text = cv_text.lower()

    # Example keyword-based analysis (you can extend this logic)
    if "leadership" in text:
        strengths.append("Leadership skills")
    if "team" in text:
        strengths.append("Teamwork")
    if "deadline" in text:
        strengths.append("Meeting deadlines")

    if "error" in text or "mistake" in text:
        weaknesses.append("Attention to detail")
    if "late" in text:
        weaknesses.append("Time management")

    if "attention to detail" in weaknesses:
        advice.append("Improve focus on details and proofreading.")
    if "time management" in weaknesses:
        advice.append("Work on better scheduling and prioritizing tasks.")

    return strengths, weaknesses, advice


def main():
    st.title("CV Strengths & Weaknesses Analyzer")

    # File uploader
    uploaded_file = st.file_uploader("Upload your CV (PDF, DOCX)", type=["pdf", "docx"])

    if uploaded_file is not None:
        # Extract text from the uploaded file
        if uploaded_file.type == "application/pdf":
            cv_text = extract_text_from_pdf(uploaded_file)
        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            cv_text = extract_text_from_docx(uploaded_file)

        # Display extracted text (for debugging or review)
        st.subheader("Extracted Text")
        st.text_area("CV Text", cv_text, height=300)

        # Analyze the CV
        if st.button("Analyze CV"):
            if not cv_text.strip():
                st.warning("Please upload a CV with text.")
                return

            strengths, weaknesses, advice = analyze_cv(cv_text)

            st.subheader("Strengths")
            if strengths:
                for s in strengths:
                    st.write(f"- {s}")
            else:
                st.write("No specific strengths detected.")

            st.subheader("Weaknesses")
            if weaknesses:
                for w in weaknesses:
                    st.write(f"- {w}")
            else:
                st.write("No specific weaknesses detected.")

            st.subheader("Advice")
            if advice:
                for a in advice:
                    st.write(f"- {a}")
            else:
                st.write("No advice available.")


if __name__ == "__main__":
    main()
