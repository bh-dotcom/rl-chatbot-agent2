import streamlit as st
import requests

BACKEND_URL = "http://127.0.0.1:8000"  # replace with Phase 1 Space URL after deployment

st.title("RL Chatbot Frontend")
msg = st.text_input("Enter message:")

if st.button("Send"):
    try:
        response = requests.post(f"{BACKEND_URL}/chat", json={"text": msg})
        st.write(response.json()["reply"])
    except Exception as e:
        st.error(f"Error: {e}")
