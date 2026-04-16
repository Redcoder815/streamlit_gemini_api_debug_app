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
    # if debug_option == "Hints":
    #     prompt = f"Generate debug with hints and solutions. Give me response exactly like this: Error:[description] || Solution:[description]"
    # else:
    #     prompt = f"Generate debug with code and solutions. Give me response exactly like this: Error:[description] || Solution:[description]"

    # if debug_option == "Hints":
    #     prompt = f"Generate debug with hints and solutions"
    # else:
    #     prompt = f"Generate debug with code and solutions"

    if debug_option == "Hints":
        prompt = f"Analyze the error. Provide a description and a hint for the solution with Error header. Give Error header in error analyze and Solution header in hint for solution and show both of them in different blocks"
    else:
        prompt = f"Analyze the error. Provide a description and the corrected code block with Solution header. Give Error header in error analyze and Solution header in code block for solution and show both of them in different blocks"

    response = client.models.generate_content(
        model = "gemini-3-flash-preview",
        contents = [images, prompt]
    )
    return response.text