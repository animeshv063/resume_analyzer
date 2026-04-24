AI RESUME ANALYZER - RUN GUIDE

-------------------------------
1. INSTALL DEPENDENCIES
-------------------------------
Run the following command in terminal:

pip install -r requirements.txt

This will install all required libraries such as:
- streamlit
- scikit-learn


-------------------------------
2. RUN FRONTEND (STREAMLIT)
-------------------------------
Command:

streamlit run frontend/app.py

Then open in browser:
http://localhost:8501

Description:
- This launches the user interface.
- The user can paste resume and job description.
- The system processes input and displays:
  • Match Score
  • Matched Keywords
  • Missing Keywords

Note:
- This is the primary way to run the application.
- It uses direct function calls (no API required).


-------------------------------
3. RUN BACKEND (FASTAPI) [OPTIONAL]
-------------------------------
Command:

python -m uvicorn backend.api:app --reload

Then open:
http://127.0.0.1:8000/docs

Description:
- This runs the backend API server.
- Useful for testing API endpoints independently.

To test API:
1. Open /docs page
2. Select POST /analyze
3. Click "Try it out"
4. Enter JSON:

{
  "resume": "Data Analyst with Python and SQL skills",
  "job": "Looking for Data Analyst with Python and SQL"
}

5. Click Execute

Output:
- JSON response containing:
  • score
  • matched keywords
  • missing keywords

Note:
- Backend is NOT required for Streamlit app.
- It is included for modular design and API support.


-------------------------------
4. RUN LOCALLY (FULL MODE - OPTIONAL)
-------------------------------
To run full architecture (frontend + backend):

Step 1: Start backend
python -m uvicorn backend.api:app --reload

Step 2: Modify frontend to use API (requests)

Step 3: Run frontend
streamlit run frontend/app.py

Note:
- This mode demonstrates API-based architecture.
- Not required for deployment.


-------------------------------
5. DEPLOYMENT (STREAMLIT CLOUD)
-------------------------------
Steps:
1. Push code to GitHub
2. Go to Streamlit Cloud
3. Click "New App"
4. Select repository
5. Set main file path:

   frontend/app.py

6. Deploy

Notes:
- App auto-updates on every git push
- No backend server needed for deployment
- Uses self-contained architecture


-------------------------------
6. STOP APPLICATION
-------------------------------
To stop running services:

Press:
CTRL + C


-------------------------------
PROJECT STRUCTURE
-------------------------------
frontend/        -> Streamlit UI (main application)
backend/         -> Core logic (utils.py) + optional API (api.py)
requirements.txt -> Dependency list

Optional components (if present):
Dockerfile        -> Container configuration
docker-compose.yml-> Multi-service setup


-------------------------------
KEY FEATURES
-------------------------------
- NLP-based resume analysis
- TF-IDF vectorization
- Cosine similarity scoring
- Keyword matching and gap analysis
- Interactive Streamlit UI


-------------------------------
END
-------------------------------