# https://platform.openai.com/docs/guides/vision
import streamlit as st
# from openai import OpenAI
import base64
import requests
import json

# Load OpenAI API key
api_key = st.secrets["OPENAI_API_KEY"]

# Function to encode the image to base64
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Path to your image
image_path = "image.png"

# Encode the image
base64_image = encode_image(image_path)

# Headers for the API request
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

# Payload for the API request
payload = {
    "model": "gpt-4-vision-preview",
    "messages": [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Summarize this slide "
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/png;base64,{base64_image}"
                    }
                }
            ]
        }
    ],
    "max_tokens": 300
}

# Sending the request to the OpenAI API
response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

# Printing the response
if response.status_code == 200:
    print("Response from GPT-4 Vision API:")
    print(json.dumps(response.json(), indent=4))
else:
    print("Failed to get response. Status code:", response.status_code)
    print("Response content:", response.content)
