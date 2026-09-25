from google import genai
from google.genai import types
from dotenv import load_dotenv
from tools import *
import os

# -----------------------------
# Load API Key
# -----------------------------
load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

# -----------------------------
# Register Native Tools
# -----------------------------
TOOLS = [
    add,
    subtract,
    multiply,
    divide,
    square,
    calculate_percentage,
    grade_from_percentage,
    calculate_cgpa,
    attendance_required,
    generate_password
]

SYSTEM_PROMPT = """
You are a Smart Student Utility Agent.

Use the available Python tools whenever needed.
Do not calculate manually if a suitable tool exists.

Examples:
- Add 10 and 20
- Square 15
- Calculate percentage of 420 out of 500
- Convert 84 into grade
- My CGPA points are 88
- I attended 48 out of 70 classes
- Generate a 16 character password
"""

# -----------------------------
# Welcome Screen
# -----------------------------
print("=" * 50)
print("🤖 Smart Student Utility Agent")
print("=" * 50)
print("Available Features:")
print("• Calculator")
print("• Percentage Calculator")
print("• Grade Generator")
print("• CGPA Calculator")
print("• Attendance Calculator")
print("• Password Generator")
print("\nType 'exit' to quit.")
print("-" * 50)

# -----------------------------
# Chat Loop
# -----------------------------
while True:

    user = input("\nYou: ").strip()

    if user.lower() == "exit":
        print("\n👋 Goodbye!")
        break

    try:

        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=user,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT,
                tools=TOOLS
            )
        )

        print(f"\nAI: {response.text}")

    except Exception as e:
        print(f"\n❌ Error: {e}")