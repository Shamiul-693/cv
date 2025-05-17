import streamlit as st
from utils.extract_text import extract_text_from_pdf, extract_text_from_docx, extract_text_from_txt
from utils.analyze_cv import check_sections, count_keywords, analyze_length
import requests

def check_grammar_languagetool(text):
    url = "https://api.languagetool.org/v2/check"
    data = {
        'text': text,
        'language': 'en-US',
    }
    response = requests.post(url, data=data)
    result = response.json()

    matches = result.get('matches', [])
    corrections = []
    for match in matches:
        message = match['message']
        context = match['context']['text']
        offset = match['context']['offset']
        length = match['context']['length']
        replacement = match.get('replacements', [{}])[0].get('value', '')

        corrections.append({
            'message': message,
            'context': context,
            'offset': offset,
            'length': length,
            'suggestion': replacement
        })

    return corrections

st.title("CV Analysis Tool")

uploaded_file = st.file_uploader("Upload your CV (pdf, docx, txt)", type=["pdf", "docx", "txt"])

if uploaded_file is not None:
    file_type = uploaded_file.type
    text = ""

    if file_type == "application/pdf":
        text = extract_text_from_pdf(uploaded_file)
    elif file_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        text = extract_text_from_docx(uploaded_file)
    elif file_type == "text/plain":
        text = extract_text_from_txt(uploaded_file)
    else:
        st.error("Unsupported file type")

    if text:
        st.subheader("Extracted Text Preview")
        st.write(text[:1000] + "...")  # show first 1000 chars

        # Analyze sections
        sections_found = check_sections(text)
        st.subheader("Sections Found")
        for section, found in sections_found.items():
            st.write(f"{section.title()}: {'✅' if found else '❌'}")

        # Analyze keywords
        keywords = ["python", "project", "management", "team", "machine learning"]
        keyword_counts = count_keywords(text, keywords)
        st.subheader("Keyword Counts")
        for k, v in keyword_counts.items():
            st.write(f"{k}: {v}")

        # Analyze length
        length_feedback = analyze_length(text)
        st.subheader("Length Feedback")
        st.write(length_feedback)

        # Grammar Check with LanguageTool API
        st.subheader("Grammar & Style Suggestions")
        corrections = check_grammar_languagetool(text)
        if corrections:
            for i, corr in enumerate(corrections[:10]):  # Show first 10 suggestions
                st.write(f"{i+1}. {corr['message']}")
                st.write(f"Context: ...{corr['context']}...")
                if corr['suggestion']:
                    st.write(f"Suggestion: {corr['suggestion']}")
                st.write("---")
        else:
            st.write("No grammar or style issues found!")
