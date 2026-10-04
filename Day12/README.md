# 📚 Day 12 — Source-Aware PDF RAG

Day 12 of my **100 Days of Agentic AI** journey.

## 📌 Objective

Upgrade the RAG pipeline from Day 11 with **source attribution**, **page-aware chunking**, **chunk overlap**, and **chunk metadata** — making the system production-ready by telling users exactly *where* each answer came from.

---

## 🆕 What's New vs Day 11

| Feature                | Day 11              | Day 12                        |
| ---------------------- | ------------------- | ----------------------------- |
| **Chunking**           | Whole-document      | Per-page (page-aware)         |
| **Chunk Overlap**      | ❌ None             | ✅ 40-word overlap            |
| **Chunk Metadata**     | ❌ None             | ✅ chunk_id, page, source     |
| **Source Attribution** | ❌ None             | ✅ Cited after every answer   |
| **Retrieval Debug**    | ❌ None             | ✅ Distances shown per chunk  |

---

## 🧠 Architecture

```
PDF
 ↓
Page Extraction          ← extract each page separately
 ↓
Page-Aware Chunking      ← split words with 40-word overlap
 ↓
Metadata Tagging         ← chunk_id, page, source
 ↓
Gemini Embeddings        ← gemini-embedding-001 (RETRIEVAL_DOCUMENT)
 ↓
FAISS IndexFlatL2        ← build vector index
 ↓
User Query
 ↓
Query Embedding          ← gemini-embedding-001 (RETRIEVAL_QUERY)
 ↓
Top-K Retrieval          ← FAISS search (top 3)
 ↓
Context Builder          ← [Chunk X | Page Y] + text
 ↓
Gemini LLM               ← gemini-3.5-flash-lite
 ↓
Answer + Sources + Distances
```

---

## 🔑 Key Concepts

### 1. Page-Aware Chunking

Instead of treating the whole PDF as a single text blob, each page is extracted and chunked *independently*. This preserves page boundaries, so every chunk knows exactly which page it came from.

```python
def create_chunks(pages):
    chunks = []
    chunk_id = 0

    for page_data in pages:
        page_number = page_data["page"]
        words = page_data["text"].split()
        start = 0

        while start < len(words):
            end = start + CHUNK_SIZE          # 200 words
            chunk_text = " ".join(words[start:end])

            chunks.append({
                "chunk_id": chunk_id,
                "page": page_number,          # 📌 page attributed here
                "source": PDF_FILE,
                "text": chunk_text
            })

            chunk_id += 1

            if end >= len(words):
                break

            start = end - CHUNK_OVERLAP       # 40-word overlap
```

### 2. Chunk Overlap

Overlap prevents important context from being cut at chunk boundaries. With `CHUNK_SIZE=200` and `CHUNK_OVERLAP=40`, each chunk shares its last 40 words with the next chunk.

```
Chunk 0: words  0 → 200
Chunk 1: words 160 → 360   ← 40-word overlap with chunk 0
Chunk 2: words 320 → 520   ← 40-word overlap with chunk 1
```

**Why it matters:** If a key sentence straddles two chunks, at least one chunk will contain it completely.

### 3. Chunk Metadata

Each chunk carries structured metadata:

```python
{
    "chunk_id": 5,
    "page": 3,
    "source": "document.pdf",
    "text": "..."
}
```

This metadata flows all the way to the user interface, enabling accurate source citations.

### 4. Source Attribution

After every answer, the system cites the exact pages it pulled from:

```
📚 Sources:
[1] document.pdf — Page 3
[2] document.pdf — Page 7
```

```python
def get_sources(results):
    seen = set()
    sources = []

    for result in results:
        key = (result["metadata"]["source"], result["metadata"]["page"])

        if key not in seen:
            seen.add(key)
            sources.append({
                "source": result["metadata"]["source"],
                "page": result["metadata"]["page"]
            })

    return sources
```

The `seen` set deduplicates — if two retrieved chunks are from the same page, that page is listed only once.

### 5. Retrieval Distance Display

After every answer, L2 distances are shown for each retrieved chunk:

```
🔎 Retrieval distances:
Chunk 5 | Page 3 | Distance: 0.3421
Chunk 11 | Page 7 | Distance: 0.4102
Chunk 23 | Page 14 | Distance: 0.5087
```

**Interpreting distances:**

| Distance Range | Meaning          |
| -------------- | ---------------- |
| 0.0 – 0.35     | Excellent match  |
| 0.35 – 0.55    | Good match       |
| 0.55 – 0.80    | Weak match       |
| > 0.80         | Poor / irrelevant|

### 6. Dual Embedding Task Types

```python
# For indexing chunks
client.models.embed_content(
    model="gemini-embedding-001",
    contents=texts,
    config=types.EmbedContentConfig(task_type="RETRIEVAL_DOCUMENT")
)

# For searching queries
client.models.embed_content(
    model="gemini-embedding-001",
    contents=query,
    config=types.EmbedContentConfig(task_type="RETRIEVAL_QUERY")
)
```

Using the correct task type improves retrieval accuracy — document and query embeddings are optimized to match each other.

---

## ⚙️ Configuration

```python
EMBEDDING_MODEL = "gemini-embedding-001"
GENERATION_MODEL = "gemini-3.5-flash-lite"

CHUNK_SIZE    = 200   # words per chunk
CHUNK_OVERLAP = 40    # words shared with next chunk

TOP_K = 3             # how many chunks to retrieve
```

---

## 🗂️ Project Structure

```
Day12/
├── main.py          # Full source-aware RAG implementation
├── document.pdf     # Sample PDF to query
├── README.md        # This file
└── .env             # GOOGLE_API_KEY=your_key_here
```

---

## ⚙️ Setup & Installation

### Prerequisites

```bash
pip install google-genai pypdf faiss-cpu numpy python-dotenv
```

### Environment Variables

```bash
# .env
GOOGLE_API_KEY=your_api_key_here
```

### Run

```bash
python main.py
```

---

## 💬 Sample Session

```
============================================================
📚 DAY 12 - SOURCE AWARE PDF RAG
============================================================

📄 Loading PDF...
✅ Loaded 60 pages.

✂️ Creating chunks...
✅ Created 94 chunks.

Creating embeddings...
✅ Embedding dimension: 3072
FAISS index created with 94 vectors.

🚀 RAG system ready!
Type 'exit' to quit.

You: What are the key risks of agentic AI?

🤖 AI:
Based on the provided context, the key risks of agentic AI include:
1. Autonomous decision-making errors that are hard to audit
2. Security vulnerabilities from tool access
3. Prompt injection via external data
4. Over-reliance without human oversight

📚 Sources:
[1] document.pdf — Page 14
[2] document.pdf — Page 22

🔎 Retrieval distances:
Chunk 31 | Page 14 | Distance: 0.3421
Chunk 51 | Page 22 | Distance: 0.4102
Chunk 67 | Page 22 | Distance: 0.5087

------------------------------------------------------------
```

---

## 🔁 RAG Evolution: Day 10 → 11 → 12

| Aspect                 | Day 10 (TF-IDF)           | Day 11 (FAISS)              | Day 12 (Source-Aware)          |
| ---------------------- | ------------------------- | --------------------------- | ------------------------------ |
| **Search Method**      | Keyword matching          | Semantic similarity         | Semantic similarity            |
| **Chunking**           | Flat text chunks          | Flat text chunks            | Page-aware + overlapping       |
| **Metadata**           | ❌ None                   | ❌ None                     | ✅ chunk_id, page, source      |
| **Source Citation**    | ❌ None                   | ❌ None                     | ✅ File + page per answer      |
| **Retrieval Debug**    | ❌ None                   | ❌ None                     | ✅ Distances per chunk         |
| **Overlap**            | ❌ None                   | ❌ None                     | ✅ 40-word overlap             |
| **Production Ready**   | No                        | Partial                     | Yes                            |

---

## 🧠 Key Learnings

1. **Page-aware chunking** is essential for accurate source citation — without it, you can't tell which page an answer came from.

2. **Chunk overlap** reduces the risk of losing context at boundaries — a 20% overlap is a good rule of thumb (40 words for 200-word chunks).

3. **Metadata flows through the whole pipeline** — attach it at chunk creation time and it's available at retrieval time with no extra work.

4. **Source attribution** is what separates a prototype RAG from a production RAG — users (and auditors) need to verify answers.

5. **L2 distance scores** give immediate feedback on retrieval quality — log them during development to tune chunk size and TOP_K.

---

## 🔮 Next Steps

- [ ] Persist FAISS index to disk (`faiss.write_index`) to avoid re-embedding on every run
- [ ] Support multiple PDFs with per-document metadata
- [ ] Add re-ranking (retrieve top 10, re-rank, use top 3)
- [ ] Hybrid search: combine semantic + keyword scores
- [ ] Stream answers token-by-token for better UX
- [ ] Add a web UI (Streamlit or FastAPI)

---

## 📦 Dependencies

| Package        | Purpose                        |
| -------------- | ------------------------------ |
| `google-genai` | Gemini embeddings + generation |
| `faiss-cpu`    | Vector similarity search       |
| `pypdf`        | PDF text extraction            |
| `numpy`        | Array handling for FAISS       |
| `python-dotenv`| Load API key from `.env`       |

---

**Progress**: Day 12/100 of Agentic AI Journey 🚀
