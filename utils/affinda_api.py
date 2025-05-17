# utils/affinda_api.py

import requests
import streamlit as st

AFFINDA_API_KEY = "aff_c91d44b7c5f262efac374817a6b3f65a883a43bc"  # Replace with your actual API key

def parse_cv_affinda(file):
    url = "https://api.affinda.com/v1/resumes"
    headers = {
        "Authorization": f"Bearer {AFFINDA_API_KEY}",
    }
    files = {
        "file": (file.name, file, file.type),
    }
    response = requests.post(url, headers=headers, files=files)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Affinda API Error: {response.status_code} - {response.text}")
        return None

