from cv_analysis import analyze_cv

def main():
    # Example: CV text could come from a file, input, or API
    cv_text = """
    Experienced engineer with strong leadership and teamwork skills.
    Occasionally misses deadlines due to time management issues.
    Has shown errors in reports, indicating a need for attention to detail.
    """

    analysis = analyze_cv(cv_text)

    print("Strengths:")
    for s in analysis['strengths']:
        print(f"- {s}")

    print("\nWeaknesses:")
    for w in analysis['weaknesses']:
        print(f"- {w}")

    print("\nAdvice:")
    for a in analysis['advice']:
        print(f"- {a}")

if __name__ == "__main__":
    main()
