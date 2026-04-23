import time
import requests

BACKEND_URL = "http://backend:8000/analyze"

def process_resume(resume, job):
    print("Worker started processing...")

    time.sleep(2)

    response = requests.post(
        BACKEND_URL,
        json={"resume": resume, "job": job}
    )

    if response.status_code == 200:
        print("Processed Result:", response.json())
    else:
        print("Error processing task")


if __name__ == "__main__":
    sample_resume = "Python developer with ML experience"
    sample_job = "Looking for Python and machine learning engineer"

    process_resume(sample_resume, sample_job)
