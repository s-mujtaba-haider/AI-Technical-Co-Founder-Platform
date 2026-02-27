import streamlit as st
import requests
import json

BACKEND_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="AI CTO", layout="wide")

st.title("🚀 AI CTO SaaS Planner")

# Input
idea = st.text_area("💡 Startup Idea", value="I want to build SaaS app", height=120)

# Generate
if st.button("Generate Plan"):

    payload = {"idea": idea}

    with st.spinner("AI thinking..."):
        response = requests.post(f"{BACKEND_URL}/generate", json=payload)

    if response.status_code == 200:
        result = response.json()

        st.success("Generated!")

        # PLAN
        st.subheader("📊 Startup Plan")
        st.json(result.get("plan", {}))

        # ARCHITECTURE
        st.subheader("🏗 Architecture")
        st.json(result.get("architecture", {}))

        # CODEGEN
        st.subheader("💻 Folder Structures Generator")
        st.json(result.get("codegen", {}))

    else:
        st.error(f"Error: {response.status_code}")
        st.write(response.text)