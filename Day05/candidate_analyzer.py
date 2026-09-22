from google import genai
from dotenv import load_dotenv
from google.genai import types
import os
import json


load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

resume = input("Paste candidate profile:\n")

jobRole = input("Enter the Job Role or Job description:")

prompt = f"""
Extract candidate information.

Return ONLY valid JSON.
Do not use markdown.

Schema:

{{
    "name": "",
    "email": "",
    "skills": [],
    "experience_years": 0,
    "education": "",
    "matching_skills": [],
    "missing_skills": [],
    "match_percentage": 0,
    "recommendation": ""
}}

Candidate Profile:
{resume}

Job Role or Job description:
{jobRole}
"""

try:
    response = client.models.generate_content(
    model="gemini-3.1-flash-lite",
    contents=prompt,
    config=types.GenerateContentConfig(
        system_instruction="""
You are an expert AI HR Specialist and Skill Gap Analyzer. 

Your task:
1. Extract candidate profile details from the resume.
2. Compare the candidate's skills, experience, and tools against the target Job Role provided.
3. Identify 'matching_skills' (skills present in resume that match job requirements).
4. Identify 'missing_skills' (key skills required for the job role that are absent or weak in the resume).
5. Calculate 'match_percentage' (0 to 100) based on how well the candidate fits the target role.
6. Provide a concise 'recommendation' (e.g., "Highly Recommended", "Suitable for interview", or "Needs further evaluation").
"""
    ),
)
except Exception as e:
    print("Gemini API Error:", e)
    exit()

clean_text = response.text.replace("```json", "").replace("```", "").strip()

try:
    data = json.loads(clean_text)
except json.JSONDecodeError:
    print("Invalid JSON received from Gemini.")
    exit()

print("\n📊 Candidate Summary")
print("-" * 30)
print("Name:", data["name"])
print("Email:", data["email"])
print("Skills:", ", ".join(data["skills"]))
print("Experience:", data["experience_years"], "years")
print("Education:", data["education"])
print("Matching Skills:", ", ".join(data["matching_skills"]))
print("Missing Skills:", ", ".join(data["missing_skills"]))
print("Match Percentage:", data["match_percentage"], "%")
print("Recommendation:", data["recommendation"])