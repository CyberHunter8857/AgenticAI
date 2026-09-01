from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

# -----------------------------
# Load Environment Variables
# -----------------------------
load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# -----------------------------
# Function: Evaluate Answer
# -----------------------------
def evaluate_answer(role, question, answer):
    prompt = f"""
You are interviewing a candidate for the role of {role}.

Interview Question:
{question}

Candidate's Answer:
{answer}

Evaluate the answer and provide:

1. Score out of 10
2. What was good (3 points)
3. What can be improved (3 points)
4. A better sample answer (maximum 80 words)

Keep the response professional and easy to understand.
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            system_instruction="You are a senior technical interviewer."
        ),
    )

    return response.text


# -----------------------------
# Main Program
# -----------------------------
print("=" * 55)
print("🎯 Welcome to AI Interview Coach")
print("=" * 55)

name = input("Enter your name: ")
role = input("Enter target job role: ")

print(f"\nGood luck, {name}! 🚀")
print("Type 'exit' anytime to quit.\n")

while True:

    print("-" * 55)
    question = input("📌 Interview Question: ")

    if question.lower() == "exit":
        break

    answer = input("💬 Your Answer: ")

    if answer.lower() == "exit":
        break

    print("\n⏳ Evaluating your answer...\n")

    result = evaluate_answer(role, question, answer)

    print("=" * 55)
    print(result)
    print("=" * 55)

print(f"\nThanks for practicing, {name}! 👋")