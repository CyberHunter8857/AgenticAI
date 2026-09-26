from google import genai
from google.genai import types
from dotenv import load_dotenv
from tools import *
import os
import json

# =============================
# Load Environment
# =============================
load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

# =============================
# Register Native Tools
# =============================
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
You are a Smart Student AI Assistant.

Rules:
- Remember previous conversation.
- Use available Python tools whenever required.
- If user asks mathematical or student related questions, use tools.
- Keep responses short and helpful.
"""

# =============================
# Safe JSON Loader
# =============================
def load_json(filename):
    try:
        if os.path.exists(filename):
            with open(filename, "r", encoding="utf-8") as file:
                content = file.read().strip()

                if content:
                    return json.loads(content)

        return []

    except json.JSONDecodeError:
        return []


def save_json(filename, data):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


# =============================
# Load Memory
# =============================
history = load_json("chat_history.json")
notes = load_json("notes.json")

# =============================
# Welcome
# =============================
print("=" * 50)
print("🤖 Smart Student AI Agent")
print("=" * 50)
print("Commands:")
print("  save note <text>")
print("  show notes")
print("  delete notes")
print("  clear")
print("  exit")
print("-" * 50)

# =============================
# Chat Loop
# =============================
while True:

    user = input("\nYou: ").strip()

    # ---------- EXIT ----------
    if user.lower() == "exit":
        print("\n💾 Data saved successfully!")
        break

    # ---------- CLEAR CHAT ----------
    if user.lower() == "clear":
        history.clear()
        save_json("chat_history.json", history)
        print("🧹 Conversation history cleared!")
        continue

    # ---------- SAVE NOTE ----------
    if user.lower().startswith("save note"):
        note = user[9:].strip()

        if note:
            notes.append(note)
            save_json("notes.json", notes)
            print("📝 Note saved!")
        else:
            print("Please enter a note.")

        continue

    # ---------- SHOW NOTES ----------
    if user.lower() == "show notes":

        if not notes:
            print("📭 No notes available.")
        else:
            print("\n📒 Your Notes")
            print("-" * 30)

            for i, note in enumerate(notes, start=1):
                print(f"{i}. {note}")

        continue

    # ---------- DELETE NOTES ----------
    if user.lower() == "delete notes":
        notes.clear()
        save_json("notes.json", notes)
        print("🗑 All notes deleted!")
        continue

    # ---------- SAVE USER MESSAGE ----------
    history.append({
        "role": "user",
        "text": user
    })

    save_json("chat_history.json", history)

    # ---------- BUILD CONVERSATION ----------
    conversation = ""

    if notes:
        conversation += "User Notes:\n"

        for note in notes:
            conversation += f"- {note}\n"

        conversation += "\n"

    for msg in history:
        conversation += f"{msg['role']}: {msg['text']}\n"

    # ---------- GEMINI ----------
    try:

        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=conversation,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT,
                tools=TOOLS
            )
        )

        ai = response.text

        print(f"\nAI: {ai}")

        history.append({
            "role": "model",
            "text": ai
        })

        save_json("chat_history.json", history)

    except Exception as e:
        print(f"\n❌ Error: {e}")