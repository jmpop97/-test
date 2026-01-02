from dotenv import load_dotenv
import os
import requests

# Load environment variables from .env file
load_dotenv()

# Ensure the environment variable 'domain' is not None
domain=os.environ.get("domain","")
token=os.environ.get("token","")

# Update payload to include the image file
image_path = "images.jpeg"  # Ensure this file exists in the same directory or provide the full path

# Open the image file in binary mode and make the POST request within the same block
with open(image_path, "rb") as image_file:
    files = {"images": image_file}
    payload = {"token": token}

    # Make the POST request with files
    response = requests.post(domain + "/f/uploadImage", data=payload, files=files)

    # Print the response status and content
    print("Status Code:", response.status_code)
    print("Response:", response.json())