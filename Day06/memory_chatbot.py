from google import genai
from dotenv import load_dotenv
import os
import json

# -----------------------------
# Load Environment Variables
# -----------------------------
load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

# -----------------------------
# Load Previous Chat History
# -----------------------------
if os.path.exists("chat_history.json"):
    with open("chat_history.json", "r", encoding="utf-8") as file:
        history = json.load(file)
else:
    history = []

# -----------------------------
# Welcome Message
# -----------------------------
print("=" * 45)
print("Welcome to My Chatbot")
print("=" * 45)
print("Commands:")
print("• exit  → Save & Quit")
print("• clear → Clear Memory")
print("-" * 45)

# -----------------------------
# Chat Loop
# -----------------------------
while True:

    user = input("\nYou: ").strip()

    # Exit
    if user.lower() == "exit":
        print("\nConversation saved successfully!")
        break

    # Clear Memory
    if user.lower() == "clear":
        history.clear()

        with open("chat_history.json", "w", encoding="utf-8") as file:
            json.dump([], file, indent=4)

        print("All chat history cleared!")
        continue

    # Store User Message
    history.append({
        "role": "user",
        "text": user
    })

    # Save Immediately
    with open("chat_history.json", "w", encoding="utf-8") as file:
        json.dump(history, file, indent=4)

    # Build Conversation Prompt
    conversation = ""

    for message in history:
        conversation += f"{message['role']}: {message['text']}\n"

    # Generate AI Response
    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=conversation
        )

        ai = response.text

    except Exception as e:
        print(f"\n❌ Gemini API Error: {e}")
        continue

    # Print Response
    print(f"\nAI: {ai}")

    # Store AI Response
    history.append({
        "role": "model",
        "text": ai
    })

    # Save Updated History
    with open("chat_history.json", "w", encoding="utf-8") as file:
        json.dump(history, file, indent=4)

print("\n Goodbye!")