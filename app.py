import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

st.set_page_config(
    page_title="AI News Summarizer",
    page_icon="📰",
    layout="wide"
)

st.title("📰 AI News Summarizer")

if st.button("Test Gemini Connection"):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")

        response = model.generate_content(
            "Reply with: Gemini connection successful"
        )

        st.success(response.text)

    except Exception as e:
        st.error(f"Error: {e}")