from dotenv import load_dotenv
import os
from google import genai
from google.genai import types

load_dotenv()

client =  genai.Client(api_key= os.getenv("GOOGLE_API_KEY"))

resume= input("Paste your resume:\n")

prompt = f"""
Review this resume.

Give:
1. Score /10
2. Top 3 strengths
3. Top 3 weaknesses
4. Missing technical skills

Resume:
{resume}
"""

response=client.models.generate_content(
    model="gemini-3.5-flash",
    contents=prompt,
    config= types.GenerateContentConfig(
        system_instruction="You are a senior software recruiter."
    ),
)

print(response.text)