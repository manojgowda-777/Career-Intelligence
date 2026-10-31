
# Test the Search Job API.
import requests

API_URL = "http://127.0.0.1:5000/api/jobs/search"

payload = {
    "role": "ai engineer",
    "mode": "both"
}

try:
    response = requests.post(
        API_URL,
        json=payload,
        timeout=300
    )

    print("HTTP Status:", response.status_code)
    print("Response:")

    # Show only the first two jobs to keep the output readable.
    data = response.json()
    print("Message:", data.get("message", data.get("error")))
    print("Total jobs:", data.get("total_jobs", 0))
    
    for job in data.get("jobs", []):
        print("\nTitle:", job.get("title"))
        print("Company:", job.get("company"))
        print("Location:", job.get("location"))
        print("Application link:", job.get("application_link"))
        print("Source:", job.get("source"))

except requests.RequestException as error:
    print("Request failed:", error)
