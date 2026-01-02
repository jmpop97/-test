from dotenv import load_dotenv
import os
import requests

# Load environment variables from .env file
load_dotenv()

# Ensure the environment variable 'domain' is not None
domain=os.environ.get("domain","")
token=os.environ.get("token","")
payload = {
    "token": "",
    "title": "유저이름으로 하면 좋을듯"
}

# Make the POST request
response = requests.post(domain+"/f/createProject", json=payload)

# Print the response status and content
print("Status Code:", response.status_code)
print("Response:", response.json())