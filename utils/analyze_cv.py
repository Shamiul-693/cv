def check_sections(text):
    sections = ["experience", "education", "skills", "projects", "summary"]
    found_sections = {section: (section in text.lower()) for section in sections}
    return found_sections

def count_keywords(text, keywords):
    text_lower = text.lower()
    counts = {}
    for word in keywords:
        counts[word] = text_lower.count(word.lower())
    return counts

def analyze_length(text):
    word_count = len(text.split())
    if word_count < 200:
        return "CV is too short, consider adding more details."
    elif word_count > 1000:
        return "CV is quite long, consider summarizing."
    else:
        return "CV length looks good."

