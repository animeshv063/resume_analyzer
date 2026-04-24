import streamlit as st
import sys
import os

# make backend visible
sys.path.insert(0, os.getcwd())

from backend.utils import analyze_resume

st.set_page_config(page_title='AI Resume Analyzer', layout='wide')

st.title('📄 AI Resume Analyzer')
st.write('Smart comparison using NLP (TF-IDF + Cosine Similarity)')

col1, col2 = st.columns(2)

with col1:
    resume = st.text_area('📄 Resume', height=300)

with col2:
    job = st.text_area('💼 Job Description', height=300)

if st.button('Analyze'):
    if resume.strip() == '' or job.strip() == '':
        st.warning('Please fill both fields')
    else:
        score, matched, missing = analyze_resume(resume, job)

        st.subheader('📊 Results')

        st.progress(int(score))
        st.write(f'Match Score: {round(score,2)}%')

        if score > 75:
            st.success('Strong Match ✅')
        elif score > 45:
            st.warning('Average Match ⚠️')
        else:
            st.error('Low Match ❌')

        st.subheader('✅ Matched Keywords')
        st.write(matched)

        st.subheader('❌ Missing Keywords')
        st.write(missing)