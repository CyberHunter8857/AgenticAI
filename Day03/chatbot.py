from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client =  genai.Client(api_key= os.getenv("GOOGLE_API_KEY"))

print("Gemini ChatBot( type exit to quit )")

while True:
    user= input("You: ")
    if user.lower() == "exit":
        break
    res= client.models.generate_content (
        model= "gemini-3.5-flash",
        contents= user
    )

    print("AI: ", res.text)
    print("_"*30)