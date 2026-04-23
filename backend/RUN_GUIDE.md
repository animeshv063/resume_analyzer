AI RESUME ANALYZER - RUN GUIDE

-------------------------------
1. INSTALL DEPENDENCIES
-------------------------------
Run this in terminal:

pip install -r requirements.txt


-------------------------------
2. RUN FRONTEND (STREAMLIT)
-------------------------------
Command:

streamlit run app.py

OR (if using frontend folder):

streamlit run frontend/app.py

Then open in browser:
http://localhost:8501


-------------------------------
3. RUN BACKEND (FASTAPI)
-------------------------------
Command:

python -m uvicorn backend.api:app --reload

Then open:
http://127.0.0.1:8000/docs

Test API:
- Click POST /analyze
- Click "Try it out"
- Enter:

{
  "resume": "python developer",
  "job": "python engineer"
}

- Click Execute


-------------------------------
4. RUN USING DOCKER (OPTIONAL)
-------------------------------
Build image:

docker build -t resume-analyzer .

Run container:

docker run -p 8501:8501 resume-analyzer


-------------------------------
5. RUN USING DOCKER-COMPOSE
-------------------------------
Command:

docker-compose up --build

This runs:
- frontend
- backend


-------------------------------
6. STOP APPLICATION
-------------------------------
Press:
CTRL + C


-------------------------------
PROJECT STRUCTURE
-------------------------------
frontend/  -> Streamlit UI
backend/   -> FastAPI API
worker/    -> background processing
k8s/       -> deployment config
Dockerfile -> container setup
docker-compose.yml -> multi-service setup


-------------------------------
END
-------------------------------