# 🚀 Day 5 — Structured Outputs & Skill Gap Analyzer

Day 5 of my **100 Days of Agentic AI** journey.

Today I learned how to make an LLM return **structured JSON** instead of plain text, allowing Python to directly process AI responses like real production applications.

## 📚 Topics Covered

- Structured Outputs
- JSON Schema Design
- Prompt Engineering
- Gemini API
- `json.loads()`
- Dictionary Parsing
- Skill Gap Analysis

## 🛠️ Project — AI Candidate Skill Gap Analyzer

A CLI application that analyzes a candidate's resume against a target job role using **Google Gemini**.

### Features

- Extracts candidate details from resume
- Identifies technical skills
- Compares resume with job role
- Finds matching skills
- Detects missing skills
- Calculates match percentage
- Provides hiring recommendation
- Returns structured JSON and converts it into a Python dictionary

## 💻 Tech Stack

- Python
- Google Gemini API
- python-dotenv
- JSON

## 📂 Project Structure

```text
Day05/
│
├── candidate_analyzer.py
├── README.md
├── .env
└── .gitignore
```

## 🔍 AI Workflow

```text
Resume + Job Role
        │
        ▼
Prompt + JSON Schema
        │
        ▼
Google Gemini
        │
        ▼
Structured JSON
        │
        ▼
Python Dictionary
        │
        ▼
Candidate Analysis Report
```

## 🎯 Key Learning

The biggest takeaway from Day 5 was understanding that **LLMs become much more powerful when they return structured data instead of paragraphs**. This pattern is the foundation of Agentic AI, where applications use AI outputs for reasoning and decision-making.

---

**Next:** Day 6 — Memory & Multi-turn AI Agents 🤖
