# Day 11: PDF RAG with Embeddings + FAISS

## Overview
Built a Retrieval-Augmented Generation (RAG) system that uses vector embeddings and FAISS for efficient similarity search over PDF documents. This implementation combines Google's Gemini embedding model with FAISS (Facebook AI Similarity Search) to create a fast, accurate question-answering system.

## What I Built

### Core Components
1. **PDF Text Extraction**: Extracts text from multi-page PDFs using PyPDF
2. **Text Chunking**: Splits documents into manageable chunks (~1000 characters each)
3. **Vector Embeddings**: Converts text chunks into 3072-dimensional vectors using Gemini
4. **FAISS Indexing**: Stores vectors in a FAISS index for fast similarity search
5. **Semantic Search**: Retrieves the most relevant chunks for user queries
6. **Answer Generation**: Uses Gemini to generate answers based on retrieved context

### Technologies Used
- **Google Gemini API**: For embeddings (`gemini-embedding-001`) and answer generation (`gemini-3.5-flash-lite`)
- **FAISS**: Facebook's library for efficient similarity search
- **PyPDF**: PDF text extraction
- **NumPy**: Array operations for embeddings

## Key Features

### 1. Smart Chunking
```python
def create_chunks(text, chunk_size=1000):
    # Splits text by words to avoid breaking mid-word
    # Maintains context within each chunk
```

### 2. Dual Embedding Tasks
- **Document Embedding**: `RETRIEVAL_DOCUMENT` task type for indexing chunks
- **Query Embedding**: `RETRIEVAL_QUERY` task type for search queries

### 3. FAISS L2 Index
- Uses `IndexFlatL2` for exact nearest neighbor search
- Stores 3072-dimensional vectors efficiently
- Returns top-k most similar chunks with distance scores

### 4. Context-Aware Generation
- Retrieves top 3 most relevant chunks
- Builds context from retrieved chunks
- Generates answers strictly from provided context
- Admits when information isn't found in the PDF

## How It Works

```
1. PDF → Text Extraction (60 pages → 79,161 characters)
2. Text → Chunks (76 chunks of ~1000 characters)
3. Chunks → Embeddings (76 × 3072 vectors)
4. Embeddings → FAISS Index (fast similarity search)
5. Query → Query Embedding
6. Query Embedding → FAISS Search (retrieves top-k chunks)
7. Retrieved Chunks → Context for LLM
8. LLM → Final Answer
```

## Results

**Test Document**: 60-page PDF on "Agentic AI for Executives"
- **Pages Processed**: 60
- **Characters Extracted**: 79,161
- **Chunks Created**: 76
- **Embedding Dimensions**: 3,072
- **Vectors Indexed**: 76

**Sample Query**: "What are the use cases of agentic AI?"

Retrieved relevant information about:
- Retail (predictive maintenance, supply chain optimization)
- Manufacturing (equipment monitoring)
- Healthcare (patient monitoring, drug discovery)
- Finance (fraud detection, trading bots)
- Education (AI tutors)
- Telecommunications (network optimization)

## Code Structure

```
Day11/
├── rag_faiss.ipynb          # Main RAG implementation
├── document.pdf             # Sample PDF (60 pages)
└── README.md                # This file
```

## Setup & Usage

### Prerequisites
```bash
pip install faiss-cpu pypdf google-genai python-dotenv numpy
```

### Environment Variables
```bash
# .env file
GOOGLE_API_KEY=your_api_key_here
```

### Run the Notebook
1. Place your PDF as `document.pdf` in the Day11 folder
2. Run all cells in `rag_faiss.ipynb`
3. Ask questions about your PDF content

## Key Learnings

### 1. FAISS vs ChromaDB
- **FAISS**: Lower-level, faster, requires manual management
- **ChromaDB**: Higher-level, includes metadata, persistence built-in
- **When to use FAISS**: Speed-critical applications, large-scale production systems

### 2. Embedding Task Types Matter
- Different task types optimize embeddings for different use cases
- `RETRIEVAL_DOCUMENT` for indexing, `RETRIEVAL_QUERY` for searching
- Improves retrieval accuracy

### 3. Chunking Strategy
- Chunk size affects retrieval quality
- Too small: loses context
- Too large: less precise retrieval
- 1000 characters is a good starting point

### 4. L2 Distance Interpretation
- Lower distance = higher similarity
- Distances around 0.4-0.5 typically indicate good matches
- Very high distances (>1.0) suggest irrelevant results

## Improvements Over Day 10

| Aspect | Day 10 (ChromaDB) | Day 11 (FAISS) |
|--------|------------------|----------------|
| **Vector Store** | ChromaDB | FAISS |
| **Persistence** | Built-in | Manual |
| **Speed** | Good | Faster |
| **Metadata** | Full support | Manual tracking |
| **Use Case** | General-purpose RAG | Production-scale search |

## Next Steps

Potential enhancements:
- [ ] Add FAISS index persistence (`faiss.write_index`)
- [ ] Implement hybrid search (vector + keyword)
- [ ] Add re-ranking of retrieved chunks
- [ ] Support multiple PDFs with document tracking
- [ ] Experiment with different FAISS index types (IVF, HNSW)
- [ ] Add streaming responses for real-time answers
- [ ] Implement chunk overlap for better context preservation

## Resources

- [FAISS Documentation](https://github.com/facebookresearch/faiss)
- [Google Gemini Embedding Guide](https://ai.google.dev/gemini-api/docs/embeddings)
- [RAG Best Practices](https://www.pinecone.io/learn/retrieval-augmented-generation/)

---

**Progress**: Day 11/100 of Agentic AI Journey 🚀
