from google import genai
# import google.generativeai as genai
import os
from dotenv import load_dotenv
import streamlit as st
from gtts import gTTS
import io

load_dotenv()

# api_key = os.environ.get("GOOGLE_GEMINI_KEY")
api_key = os.getenv("GOOGLE_GEMINI_KEY")

client = genai.Client(api_key = api_key)

def debug_error(images, debug_option):
    if debug_option == "Hints":
        prompt = f"Generate debug with hints and solutions"
    else:
        prompt = f"Generate debug with code and solutions"

    response = client.models.generate_content(
        model = "gemini-3-flash-preview",
        contents = [images, prompt]
    )
    return response.text