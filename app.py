import streamlit as st
from utils.affinda_api import parse_cv_affinda

def analyze_parsed_cv(parsed_json):
    # (Use the function above here)
    # ...copy the full function here...
    score = 0
    feedback = []

    experiences = parsed_json.get("experience", [])
    total_years = 0
    for exp in experiences:
        start = exp.get("startDate")
        end = exp.get("endDate")
        if start and end:
            total_years += 1

    if total_years >= 5:
        score += 30
        feedback.append("Strong experience with over 5 years.")
    elif total_years > 0:
        score += 15
        feedback.append(f"Some experience ({total_years} years), consider adding more.")
    else:
        feedback.append("No experience listed. Adding relevant work experience would improve your CV.")

    skills = parsed_json.get("skills", [])
    num_skills = len(skills)
    if num_skills >= 10:
        score += 20
        feedback.append("Good variety of skills listed.")
    elif num_skills > 0:
        score += 10
        feedback.append("Consider adding more skills relevant to your job target.")
    else:
        feedback.append("No skills found. Adding key skills is important.")

    education = parsed_json.get("education", [])
    if education:
        score += 20
        feedback.append("Education section present.")
    else:
        feedback.append("Consider adding your education details.")

    text = parsed_json.get("text", "").lower()
    sections = ["summary", "projects", "achievements"]
    sections_found = [sec for sec in sections if sec in text]
    section_score = (len(sections_found) / len(sections)) * 15
    score += section_score
    if sections_found:
        feedback.append(f"Sections found: {', '.join(sections_found)}.")
    else:
        feedback.append("Consider adding summary, projects, or achievements sections.")

    contact = parsed_json.get("contactDetails", {})
    if contact.get("email") or contact.get("phone"):
        score += 15
        feedback.append("Contact information is present.")
    else:
        feedback.append("Add contact info like email and phone number.")

    score = min(score, 100)

    return score, feedback


st.title("CV Analysis Tool with  SamCV")

uploaded_file = st.file_uploader("Upload your CV (pdf, docx, txt)", type=["pdf", "docx", "txt"])

if uploaded_file is not None:
    parsed_data = parse_cv_affinda(uploaded_file)
    if parsed_data:
        st.subheader("Parsed Resume Data (raw)")
        st.json(parsed_data)  # Optional: show raw JSON

        # Analyze CV
        score, feedback = analyze_parsed_cv(parsed_data)

        st.subheader("CV Quality Score")
        st.write(f"{score} / 100")

        st.subheader("Strengths & Weaknesses")
        for item in feedback:
            st.write("- " + item)
