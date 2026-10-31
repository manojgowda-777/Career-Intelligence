# Test connection to a public job-data API

import requests

url = "https://himalayas.app/jobs/api/search"

params = {
    "q": "AI/ML Engineer",
    "sort": "recent",
    "page": 1
}

response = requests.get(url, params=params, timeout=30)

print("Status:", response.status_code)

if response.status_code == 200:
    data = response.json()

    print("Total jobs found:", data.get("totalCount"))
    print()

    for job in data.get("jobs", []):
        print("Job:", job.get("title"))
        print("Company:", job.get("companyName"))
        print("Published:", job.get("pubDate"))
        print("Application:", job.get("applicationLink"))
        print("-" * 50)

else:
    print("Request failed")
    print(response.text)