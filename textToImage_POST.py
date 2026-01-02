from dotenv import load_dotenv
import os
import requests

# Load environment variables from .env file
load_dotenv()

# Ensure the environment variable 'domain' is not None
domain=os.environ.get("domain","")
token=os.environ.get("token","")
projectId=os.environ.get("projectId","")
# Update payload to include the image file
# Open the image file in binary mode and make the POST request within the same block
payload = {
    "token": token,
    "projectId":projectId,
    "prompt":"고릴라 DJ"
    }

# Make the POST request with files
response = requests.post(domain + "/f/uploadImage", data=payload)

# Print the response status and content
print("Status Code:", response.status_code)
print("Response:", response.json())