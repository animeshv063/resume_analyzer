import streamlit as st
import re

st.set_page_config(page_title="AI Resume Analyzer", layout="centered")

st.title("📄 AI Resume Analyzer")
st.write("Compare your resume with job description using AI (NLP-based)")

def preprocess(text):
    text = text.lower()
    words = re.findall(r'\b\w+\b', text)
    return set(words)

resume = st.text_area("Paste Resume Here")
job = st.text_area("Paste Job Description Here")

if st.button("Analyze"):
    resume_words = preprocess(resume)
    job_words = preprocess(job)

    matched = resume_words.intersection(job_words)

    score = (len(matched) / len(job_words)) * 100 if len(job_words) > 0 else 0

    st.subheader("Results")
    st.write("Matched Keywords:", matched)
    st.write("Match Score:", round(score, 2), "%")

    if score > 70:
        st.success("Strong Match ✅")
    elif score > 40:
        st.warning("Average Match ⚠️")
    else:
        st.error("Low Match ❌")