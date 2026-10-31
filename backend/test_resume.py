
# Test the resume PDF extraction API.
import requests
from pathlib import Path

API_URL = "http://127.0.0.1:5000/api/resume/extract"

# Enter the full path to a real PDF resume on your computer.
PDF_PATH = Path(r"C:\Users\manoj\OneDrive\Desktop\Manoj_Resume.pdf")

try:
    with PDF_PATH.open("rb") as pdf_file:
        response = requests.post(
            API_URL,
            files={
                "resume": (
                    PDF_PATH.name,
                    pdf_file,
                    "application/pdf"
                )
            },
            timeout=60
        )

    print("HTTP Status:", response.status_code)

    data = response.json()
    print("Message:", data.get("message", data.get("error")))

    
    if response.ok:
        # Import the function that identifies resume skills.
        from resume_analyzer import extract_resume_skills

        # Display the skills found in your resume.
        print("\nSkills identified:")
        print(extract_resume_skills(data["resume_text"]))


except FileNotFoundError:
    print("PDF not found. Update PDF_PATH to your actual resume location.")

except requests.RequestException as error:
    print("Request failed:", error)
