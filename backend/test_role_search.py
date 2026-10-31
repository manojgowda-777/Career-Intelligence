
# Test the Career Intelligence role-search API.
import requests

# Address of the running Flask backend.
API_URL = "http://127.0.0.1:5000/api/role/search"

# Test Python Developer jobs in India.
payload = {
    "role": "Python Developer",
    "mode": "india"
}

try:
    # Send the role-search request to Flask.
    response = requests.post(
        API_URL,
        json=payload,
        timeout=300
    )

    # Display the HTTP status and API response.
    print("HTTP Status:", response.status_code)
    print("Response:")

    print(response.text)

except requests.RequestException as error:
    # Show connection or request errors.
    print("Request failed:", error)
