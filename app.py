import streamlit as st
import re
from sklearn.feature_extraction.text import TfidfVectorizer, ENGLISH_STOP_WORDS
from sklearn.metrics.pairwise import cosine_similarity

st.set_page_config(page_title='AI Resume Analyzer', layout='wide')

st.title('📄 AI Resume Analyzer')
st.write('Smart comparison using NLP (TF-IDF + Cosine Similarity)')

# 🔹 Clean + filter words
def preprocess(text):
    text = text.lower()
    words = re.findall(r'\b[a-zA-Z]+\b', text)
    words = [w for w in words if w not in ENGLISH_STOP_WORDS and len(w) > 2]
    return set(words)

# 🔹 Better similarity with phrases
def get_similarity(resume, job):
    tfidf = TfidfVectorizer(stop_words='english', ngram_range=(1,2))
    vectors = tfidf.fit_transform([resume, job])
    similarity = cosine_similarity(vectors[0], vectors[1])[0][0]
    return similarity * 100

col1, col2 = st.columns(2)

with col1:
    resume = st.text_area('📄 Paste Resume Here', height=300)

with col2:
    job = st.text_area('💼 Paste Job Description Here', height=300)

if st.button('Analyze'):
    if resume.strip() == '' or job.strip() == '':
        st.warning('Please fill both fields')
    else:
        resume_words = preprocess(resume)
        job_words = preprocess(job)

        matched = resume_words.intersection(job_words)
        missing = job_words - resume_words

        score = get_similarity(resume, job)

        st.subheader('📊 Results')
        st.progress(int(score))
        st.write(f'Match Score: {round(score, 2)}%')

        if score > 75:
            st.success('Strong Match ✅')
        elif score > 45:
            st.warning('Average Match ⚠️')
        else:
            st.error('Low Match ❌')

        st.subheader('✅ Matched Keywords')
        st.write(sorted(matched))

        st.subheader('❌ Missing Keywords')
        st.write(sorted(missing))