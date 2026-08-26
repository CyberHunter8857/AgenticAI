from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client =  genai.Client(api_key= os.getenv("GOOGLE_API_KEY"))

response= client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Explain Agentic AI in simple words."
)

print(response.text)