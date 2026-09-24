from google import genai
from google.genai import types
from dotenv import load_dotenv
from tools import *
import os
import json

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

SYSTEM_PROMPT = """
You are an AI Utility Agent.

Available tools:

1. add(a,b)
2. subtract(a,b)
3. multiply(a,b)
4. divide(a,b)
5. bmi(height_cm, weight_kg)
6. age(year, month, day)
7. km_to_miles(km)
8. password(length)

Return ONLY valid JSON.

Schemas:

Calculator:
{
  "tool":"add",
  "a":10,
  "b":20
}

BMI:
{
  "tool":"bmi",
  "height_cm":175,
  "weight_kg":70
}

Age:
{
  "tool":"age",
  "year":2003,
  "month":5,
  "day":18
}

KM:
{
  "tool":"km_to_miles",
  "km":5
}

Password:
{
  "tool":"password",
  "length":16
}
"""

print("="*45)
print("🤖 Smart Utility Agent")
print("="*45)
print("Type 'exit' to quit\n")

while True:

    user = input("You: ")

    if user.lower() == "exit":
        print("Goodbye! 👋")
        break

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=user,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT
        )
    )

    clean = (
        response.text
        .replace("```json","")
        .replace("```","")
        .strip()
    )

    try:
        command = json.loads(clean)

        tool = command["tool"]

        if tool == "add":
            result = add(command["a"], command["b"])

        elif tool == "subtract":
            result = subtract(command["a"], command["b"])

        elif tool == "multiply":
            result = multiply(command["a"], command["b"])

        elif tool == "divide":
            result = divide(command["a"], command["b"])

        elif tool == "bmi":
            result = calculate_bmi(
                command["height_cm"],
                command["weight_kg"]
            )

        elif tool == "age":
            result = calculate_age(
                command["year"],
                command["month"],
                command["day"]
            )

        elif tool == "km_to_miles":
            result = km_to_miles(command["km"])

        elif tool == "password":
            result = generate_password(command["length"])

        else:
            result = "Unknown tool."

        print(f"\nAI: {result}")
        print("-"*35)

    except Exception as e:
        print("Error:", e)