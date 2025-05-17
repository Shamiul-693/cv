import streamlit as st

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

    cv_text = st.text_area("Paste your CV text here:")

    if st.button("Analyze"):
        if not cv_text.strip():
            st.warning("Please enter CV text to analyze.")
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
