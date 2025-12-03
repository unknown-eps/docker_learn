import streamlit as st
import requests
import os

BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")

st.title("Streamlit + FastAPI Demo")

st.header("Health Check")
if st.button("Check Backend Health"):
    try:
        response = requests.get(f"{BACKEND_URL}/health")
        if response.status_code == 200:
            st.success(f"Backend is healthy: {response.json()}")
        else:
            st.error(f"Backend returned status: {response.status_code}")
    except requests.exceptions.ConnectionError:
        st.error("Could not connect to backend. Is it running?")

st.header("Save Text")
user_text = st.text_input("Enter text to save:")
if st.button("Save to File"):
    if user_text:
        try:
            response = requests.post(f"{BACKEND_URL}/save", json={"text": user_text})
            if response.status_code == 200:
                st.success("Text saved!")
            else:
                st.error(f"Failed to save: {response.text}")
        except requests.exceptions.ConnectionError:
             st.error("Could not connect to backend.")
    else:
        st.warning("Please enter some text first.")
