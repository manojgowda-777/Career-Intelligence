
import requests

base_url = "http://127.0.0.1:5000"

# Generate a quiz
quiz_response = requests.post(
    f"{base_url}/api/mcq/generate",
    json={"skills": ["Python"]}
)

print("Quiz generation status:", quiz_response.status_code)
quiz_data = quiz_response.json()

if quiz_response.status_code != 200:
    print(quiz_data)
    raise SystemExit

quiz_id = quiz_data["quiz_id"]
questions = quiz_data["questions"]

# Submit one valid option for each issued question
answers = [
    {
        "id": question["id"],
        "answer": question["options"][0]
    }
    for question in questions
]

submission = requests.post(
    f"{base_url}/api/mcq/submit",
    json={
        "quiz_id": quiz_id,
        "answers": answers
    }
)

print("Submission status:", submission.status_code)
print(submission.json())

# Try submitting the same quiz again
repeat = requests.post(
    f"{base_url}/api/mcq/submit",
    json={
        "quiz_id": quiz_id,
        "answers": answers
    }
)

print("Repeat submission status:", repeat.status_code)
print(repeat.json())
