import streamlit as st
from utils.affinda_api import parse_cv_affinda  # Import your helper
from utils.analyze_cv import check_sections, count_keywords, analyze_length

st.title("CV Analysis Tool with Affinda API")

uploaded_file = st.file_uploader("Upload your CV (pdf, docx, txt)", type=["pdf", "docx", "txt"])

if uploaded_file is not None:
    parsed_data = parse_cv_affinda(uploaded_file)
    if parsed_data:
        st.subheader("Parsed Resume Data (from Affinda)")
        st.json(parsed_data)  # Display raw JSON for now; you can customize

        # Optionally, you can extract text from parsed_data and run your analysis:
        # For example:
        # full_text = parsed_data.get('text', '')
        # sections_found = check_sections(full_text)
        # st.write(sections_found)
