from google import genai
from dotenv import load_dotenv
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

# -----------------------------
# Load Environment
# -----------------------------
load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

# -----------------------------
# Load Knowledge Base
# -----------------------------
with open("notes.txt", "r", encoding="utf-8") as file:
    text = file.read()

chunks = [chunk.strip() for chunk in text.split("\n\n") if chunk.strip()]

# -----------------------------
# Create Vector Database
# -----------------------------
vectorizer = TfidfVectorizer()

vectors = vectorizer.fit_transform(chunks)

print("=" * 45)
print("📚 RAG Chatbot")
print("=" * 45)
print("Ask questions from notes.txt")
print("Type 'exit' to quit.\n")

while True:

    user = input("You: ")

    if user.lower() == "exit":
        break

    query_vector = vectorizer.transform([user])

    scores = cosine_similarity(query_vector, vectors)

    best_index = scores.argmax()

    context = chunks[best_index]

    prompt = f"""
Answer the user's question using ONLY the provided context.

Context:
{context}

Question:
{user}
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    print("\nAI:", response.text)
    print("-" * 40)