
import requests
from pathlib import Path

API_URL = "http://127.0.0.1:5000/api/resume/compare"

# Your existing resume PDF path.
PDF_PATH = Path(
    r"C:\Users\manoj\OneDrive\Desktop\Manoj_Resume.pdf"
)

# Choose the job role and search region.
ROLE = "Python Developer"
MODE = "india"  # india, international, or both

try:
    with PDF_PATH.open("rb") as pdf_file:
        response = requests.post(
            API_URL,
            data={
                "role": ROLE,
                "mode": MODE
            },
            files={
                "resume": (
                    PDF_PATH.name,
                    pdf_file,
                    "application/pdf"
                )
            },
            timeout=300
        )

    print("HTTP Status:", response.status_code)

    data = response.json()

    if response.ok:
        print("Message:", data["message"])
        print("Job Role:", data["role"])
        print("Jobs Analyzed:", data["total_jobs_analyzed"])

        print("\nResume Skills:")
        print(data["resume_skills"])

        print("\nMatching Skills:")
        print(data["matching_skills"])

        print("\nMissing Skills:")
        print(data["missing_skills"])

        print("\nMatched Count:", data["matched_count"])
        print("Required Skill Count:", data["required_count"])
        print("Readiness Score:", str(data["readiness_score"]) + "%")
    else:
        print("Error:", data.get("error", data))

except FileNotFoundError:
    print("Resume PDF not found. Check PDF_PATH.")

except requests.RequestException as error:
    print("Request failed:", error)
