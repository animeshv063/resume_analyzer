import streamlit as st
import requests

st.set_page_config(page_title='AI Resume Analyzer', layout='wide')

st.title('📄 AI Resume Analyzer')
st.write('Frontend connected to backend API')

col1, col2 = st.columns(2)

with col1:
    resume = st.text_area('📄 Resume', height=300)

with col2:
    job = st.text_area('💼 Job Description', height=300)

if st.button('Analyze'):
    if resume.strip() == '' or job.strip() == '':
        st.warning('Please fill both fields')
    else:
        response = requests.post(
            'http://backend:8000/analyze',
            json={'resume': resume, 'job': job}
        )

        data = response.json()

        score = data['score']
        matched = data['matched']
        missing = data['missing']

        st.subheader('📊 Results')

        st.progress(int(score))
        st.write(f'Match Score: {round(score,2)}%')

        st.subheader('✅ Matched Keywords')
        st.write(matched)

        st.subheader('❌ Missing Keywords')
        st.write(missing)
