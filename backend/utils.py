import re
from sklearn.feature_extraction.text import TfidfVectorizer, ENGLISH_STOP_WORDS
from sklearn.metrics.pairwise import cosine_similarity

def preprocess(text):
    text = text.lower()
    words = re.findall(r'\b[a-zA-Z]+\b', text)
    words = [w for w in words if w not in ENGLISH_STOP_WORDS and len(w) > 2]
    return set(words)

def get_similarity(resume, job):
    tfidf = TfidfVectorizer(stop_words='english', ngram_range=(1,2))
    vectors = tfidf.fit_transform([resume, job])
    similarity = cosine_similarity(vectors[0], vectors[1])[0][0]
    return similarity * 100

def analyze_resume(resume, job):
    resume_words = preprocess(resume)
    job_words = preprocess(job)

    matched = resume_words.intersection(job_words)
    missing = job_words - resume_words
    score = get_similarity(resume, job)

    return score, matched, missing