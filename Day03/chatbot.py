from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client =  genai.Client(api_key= os.getenv("GOOGLE_API_KEY"))

name = input("Enter Your Name:")
history = []
print(f'\nWelcome {name} 🤖 \n')
print("Type 'clear' to reset or 'exit' to quit.\n")

while True:
    user= input(f'{name}: ')
    if user.lower() == "exit":
        break

    if user.lower()=="clear":
        history.clear()
        print("Chat history cleared!\n")
        continue

    history.append(f'{name}: {user}')

    prompt="\n".join(history)

    res= client.models.generate_content (
        model= "gemini-3.5-flash",
        contents= prompt
    )

    ai=res.text

    print("AI: ", ai)
    history.append(f'AI: {ai}')
    print("_"*30)

with open("chat_history.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(history))
print("Conversation saved to chat_history.txt")
