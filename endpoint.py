import streamlit as st
import requests

# Streamlit app title
st.title("Connect webui to API")

# User input for text
user_text = st.text_area("Enter some text:")

def detect_text(text):
    # Replace with your custom API endpoint
    api_endpoint = "http://18.210.158.140:8000/analyse/sentiment" 
    payload = {"text": text}
    print(payload,flush=True)
    response = requests.post(api_endpoint, params=payload)
    
    if response.status_code == 200:
        return response.json()
    else:
        return "Text detection failed."

# Detect language when the user submits the form
if st.button("Detect Text"):
    if user_text:
        text_input = detect_text(user_text)
        st.write(f"Detected text: {text_input}")
    else:
        st.warning("Please enter some text.")

st.info("This app connects streamlit UI to AWS hosted FastAPI using Ec2 and Elastic IP Address.")
