from google import genai
from google.genai import types
from dotenv import load_dotenv

from pypdf import PdfReader

import numpy as np
import faiss
import os


# =========================================================
# CONFIGURATION
# =========================================================

load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    raise ValueError("GOOGLE_API_KEY not found in .env file")

client = genai.Client(api_key=API_KEY)

PDF_FILE = "document.pdf"

EMBEDDING_MODEL = "gemini-embedding-001"
GENERATION_MODEL = "gemini-3.5-flash-lite"

CHUNK_SIZE = 200
CHUNK_OVERLAP = 40

TOP_K = 3


# =========================================================
# 1. LOAD PDF
# =========================================================

def load_pdf(pdf_file):
    """
    Extract text from every page of the PDF.

    Returns:
        List of dictionaries containing page number and text.
    """

    reader = PdfReader(pdf_file)

    pages = []

    for page_number, page in enumerate(reader.pages, start=1):

        text = page.extract_text()

        if text and text.strip():

            pages.append({
                "page": page_number,
                "text": text.strip()
            })

    return pages


# =========================================================
# 2. CHUNK EACH PAGE
# =========================================================

def create_chunks(pages):
    """
    Split each page into smaller overlapping chunks.

    Each chunk contains metadata:
    - chunk_id
    - page
    - source
    - text
    """

    chunks = []

    chunk_id = 0

    for page_data in pages:

        page_number = page_data["page"]
        text = page_data["text"]

        words = text.split()

        start = 0

        while start < len(words):

            end = start + CHUNK_SIZE

            chunk_words = words[start:end]

            chunk_text = " ".join(chunk_words)

            if chunk_text.strip():

                chunks.append({
                    "chunk_id": chunk_id,
                    "page": page_number,
                    "source": PDF_FILE,
                    "text": chunk_text
                })

                chunk_id += 1

            # Stop if this is the final chunk
            if end >= len(words):
                break

            # Move forward while keeping overlap
            start = end - CHUNK_OVERLAP

    return chunks


# =========================================================
# 3. CREATE EMBEDDINGS
# =========================================================

def create_embeddings(chunks):
    """
    Generate Gemini embeddings for all document chunks.
    """

    texts = [
        chunk["text"]
        for chunk in chunks
    ]

    print("\nCreating embeddings...")

    response = client.models.embed_content(
        model=EMBEDDING_MODEL,
        contents=texts,
        config=types.EmbedContentConfig(
            task_type="RETRIEVAL_DOCUMENT"
        )
    )

    embeddings = [
        item.values
        for item in response.embeddings
    ]

    embeddings = np.array(
        embeddings,
        dtype=np.float32
    )

    return embeddings


# =========================================================
# 4. CREATE FAISS INDEX
# =========================================================

def create_faiss_index(embeddings):

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(embeddings)

    print(f"FAISS index created with {index.ntotal} vectors.")

    return index


# =========================================================
# 5. EMBED USER QUERY
# =========================================================

def embed_query(query):

    response = client.models.embed_content(
        model=EMBEDDING_MODEL,
        contents=query,
        config=types.EmbedContentConfig(
            task_type="RETRIEVAL_QUERY"
        )
    )

    embedding = np.array(
        response.embeddings[0].values,
        dtype=np.float32
    )

    return embedding.reshape(1, -1)


# =========================================================
# 6. RETRIEVE TOP-K CHUNKS
# =========================================================

def retrieve_chunks(query, index, chunks, top_k=TOP_K):

    query_embedding = embed_query(query)

    distances, indices = index.search(
        query_embedding,
        top_k
    )

    results = []

    for distance, index_position in zip(
        distances[0],
        indices[0]
    ):

        if index_position == -1:
            continue

        results.append({
            "metadata": chunks[index_position],
            "distance": float(distance)
        })

    return results


# =========================================================
# 7. BUILD CONTEXT
# =========================================================

def build_context(results):

    context_parts = []

    for result in results:

        metadata = result["metadata"]

        context_parts.append(
            f"""
[Chunk {metadata['chunk_id']} | Page {metadata['page']}]

{metadata['text']}
"""
        )

    return "\n".join(context_parts)


# =========================================================
# 8. GET UNIQUE SOURCES
# =========================================================

def get_sources(results):

    sources = []

    seen = set()

    for result in results:

        metadata = result["metadata"]

        key = (
            metadata["source"],
            metadata["page"]
        )

        if key not in seen:

            seen.add(key)

            sources.append({
                "source": metadata["source"],
                "page": metadata["page"]
            })

    return sources


# =========================================================
# 9. GENERATE ANSWER
# =========================================================

def generate_answer(question, context):

    prompt = f"""
You are a helpful RAG assistant.

Answer the user's question using ONLY the provided context.

If the answer cannot be found in the context,
say:

"I couldn't find the answer in the document."

Do not use outside knowledge.

Keep the answer clear and concise.

---------------- CONTEXT ----------------

{context}

-------------- END CONTEXT --------------

User Question:
{question}
"""

    response = client.models.generate_content(
        model=GENERATION_MODEL,
        contents=prompt
    )

    return response.text


# =========================================================
# 10. DISPLAY SOURCES
# =========================================================

def display_sources(results):

    sources = get_sources(results)

    print("\n📚 Sources:")

    for i, source in enumerate(sources, start=1):

        print(
            f"[{i}] "
            f"{source['source']} "
            f"— Page {source['page']}"
        )


# =========================================================
# MAIN PROGRAM
# =========================================================

def main():

    print("=" * 60)
    print("📚 DAY 12 - SOURCE AWARE PDF RAG")
    print("=" * 60)

    # -----------------------------------------------------
    # Load PDF
    # -----------------------------------------------------

    print("\n📄 Loading PDF...")

    pages = load_pdf(PDF_FILE)

    if not pages:

        print("❌ No text found in PDF.")

        return

    print(
        f"✅ Loaded {len(pages)} pages."
    )

    # -----------------------------------------------------
    # Create chunks
    # -----------------------------------------------------

    print("\n✂️ Creating chunks...")

    chunks = create_chunks(pages)

    print(
        f"✅ Created {len(chunks)} chunks."
    )

    # -----------------------------------------------------
    # Create embeddings
    # -----------------------------------------------------

    embeddings = create_embeddings(chunks)

    print(
        f"✅ Embedding dimension: "
        f"{embeddings.shape[1]}"
    )

    # -----------------------------------------------------
    # Create FAISS index
    # -----------------------------------------------------

    index = create_faiss_index(embeddings)

    print("\n🚀 RAG system ready!")

    print("\nType 'exit' to quit.\n")

    # -----------------------------------------------------
    # Chat loop
    # -----------------------------------------------------

    while True:

        question = input("You: ").strip()

        if not question:
            continue

        if question.lower() == "exit":

            print("\nGoodbye! 👋")

            break

        try:

            # ---------------------------------------------
            # Retrieve
            # ---------------------------------------------

            results = retrieve_chunks(
                question,
                index,
                chunks,
                TOP_K
            )

            if not results:

                print(
                    "\n❌ No relevant information found."
                )

                continue

            # ---------------------------------------------
            # Build context
            # ---------------------------------------------

            context = build_context(results)

            # ---------------------------------------------
            # Generate answer
            # ---------------------------------------------

            answer = generate_answer(
                question,
                context
            )

            # ---------------------------------------------
            # Display answer
            # ---------------------------------------------

            print("\n🤖 AI:")
            print(answer)

            # ---------------------------------------------
            # Display sources
            # ---------------------------------------------

            display_sources(results)

            # ---------------------------------------------
            # Display retrieval distances
            # ---------------------------------------------

            print("\n🔎 Retrieval distances:")

            for result in results:

                metadata = result["metadata"]

                print(
                    f"Chunk {metadata['chunk_id']} "
                    f"| Page {metadata['page']} "
                    f"| Distance: "
                    f"{result['distance']:.4f}"
                )

            print("\n" + "-" * 60)

        except Exception as error:

            print(
                f"\n❌ Error: {error}"
            )


# =========================================================
# RUN
# =========================================================

if __name__ == "__main__":
    main()