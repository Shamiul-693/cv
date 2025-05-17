import re

def analyze_cv(cv_text):
    # Define keywords for strengths and weaknesses
    strength_keywords = {
        'skills': ['python', 'machine learning', 'data analysis', 'project management', 'leadership', 'problem solving'],
        'experience': ['years of experience', 'managed', 'led', 'developed', 'implemented', 'designed'],
        'education': ['phd', 'master', 'bachelor', 'degree', 'certification', 'course']
    }
    
    weakness_keywords = {
        'lack_of_skills': ['no experience', 'beginner', 'limited knowledge', 'basic understanding'],
        'gaps_in_experience': ['no management experience', 'no leadership', 'short internships', 'limited projects'],
        'education_gaps': ['no degree', 'incomplete', 'dropped out']
    }
    
    # Lowercase text for simple matching
    text = cv_text.lower()
    
    # Analyze strengths
    strengths = []
    for category, keywords in strength_keywords.items():
        for kw in keywords:
            if kw in text:
                strengths.append(f"Strong in {category}: '{kw}' found.")
                
    # Analyze weaknesses
    weaknesses = []
    for category, keywords in weakness_keywords.items():
        for kw in keywords:
            if kw in text:
                weaknesses.append(f"Potential weakness in {category}: '{kw}' mentioned.")
                
    # Basic advice based on findings
    advice = []
    if not strengths:
        advice.append("Try to highlight your skills, experience, and education more clearly.")
    if weaknesses:
        advice.append("Consider improving areas related to your weaknesses or addressing them in your CV.")
    if 'python' not in text and 'programming' not in text:
        advice.append("Learning programming skills like Python could strengthen your CV.")
    
    return {
        'strengths': strengths,
        'weaknesses': weaknesses,
        'advice': advice
    }

# Example CV text input
cv_example = """
John Doe has 3 years of experience in data analysis and project management. 
He holds a Master degree in Computer Science and has skills in Python and machine learning.
"""

result = analyze_cv(cv_example)

print("Strengths:")
for s in result['strengths']:
    print("-", s)

print("\nWeaknesses:")
for w in result['weaknesses']:
    print("-", w)

print("\nAdvice:")
for a in result['advice']:
    print("-", a)
