# 📚 Day 10 — RAG Chatbot (Retrieval-Augmented Generation)

Day 10 of my **100 Days of Agentic AI** journey.

## Topics Covered

- Retrieval-Augmented Generation (RAG)
- Text Chunking
- TF-IDF Vectorization
- Cosine Similarity
- Context Injection
- Knowledge Base Search

## Project

Built a chatbot that answers questions from a local knowledge base (`notes.txt`) by retrieving the most relevant text before sending it to Gemini.

## Workflow

Document → Chunks → TF-IDF Vectors → Similarity Search → Gemini → Answer

## Tech Stack

- Python
- Google Gemini API
- scikit-learn
- TF-IDF
- Cosine Similarity

## Key Learning

LLMs don't need the entire document. A RAG pipeline retrieves only the most relevant context, making responses more accurate, faster, and cheaper.

# 📚 Day 10 — Chat with PDF (RAG)

Day 10 of my **100 Days of Agentic AI** journey.

## Topics Covered

- PDF Text Extraction
- Retrieval-Augmented Generation (RAG)
- Text Chunking
- TF-IDF Vectorization
- Cosine Similarity
- Context-Based Question Answering

## Project

Built a chatbot that answers questions directly from a PDF by retrieving the most relevant text before sending it to Gemini.

## Workflow

PDF → Extract Text → Chunks → TF-IDF → Similarity Search → Gemini → Answer

## Tech Stack

- Python
- Google Gemini API
- pypdf
- scikit-learn
- TF-IDF
- Cosine Similarity

## Key Learning

RAG allows an AI application to answer questions from **your own documents** instead of relying only on the model's training data. This is the foundation of ChatPDF, enterprise document assistants, and knowledge-base chatbots.
