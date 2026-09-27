from google import genai
from dotenv import load_dotenv
from pypdf import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

# =============================
# Load Environment
# =============================
load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

# =============================
# Load PDF
# =============================
reader = PdfReader("document.pdf")

text = ""

for page in reader.pages:
    extracted = page.extract_text()

    if extracted:
        text += extracted + "\n"

# =============================
# Chunking
# =============================
chunks = []

chunk_size = 500

for i in range(0, len(text), chunk_size):
    chunk = text[i:i + chunk_size]

    if chunk.strip():
        chunks.append(chunk)

# =============================
# Create Vector Database
# =============================
vectorizer = TfidfVectorizer()

vectors = vectorizer.fit_transform(chunks)

print("=" * 50)
print("📚 PDF RAG Chatbot")
print("=" * 50)
print(f"Loaded {len(chunks)} text chunks.")
print("Type 'exit' to quit.")
print("-" * 50)

# =============================
# Chat Loop
# =============================
while True:

    question = input("\nYou: ")

    if question.lower() == "exit":
        print("👋 Goodbye!")
        break

    # Convert Question to Vector
    query_vector = vectorizer.transform([question])

    # Similarity Search
    scores = cosine_similarity(query_vector, vectors)

    best_index = scores.argmax()

    best_chunk = chunks[best_index]

    # Prompt
    prompt = f"""
You are a PDF assistant.

Answer ONLY using the provided context.
If the answer is not present, say:
"I couldn't find that information in the PDF."

Context:
{best_chunk}

Question:
{question}
"""

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=prompt
    )

    print("\nAI:", response.text)
    print("-" * 50)