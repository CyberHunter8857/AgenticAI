# 🤖 Day 7 — Smart Utility Agent (Tool Calling)

Day 7 of my **100 Days of Agentic AI** journey.

Today I built my **first real AI Agent** that doesn't just generate text—it decides which Python tool to use and executes it.

## 📚 Topics Covered

- Agentic AI Fundamentals
- Tool Calling
- Function Calling
- Structured JSON Commands
- Decision Making with LLMs
- Python Function Execution

## 🛠️ Project — Smart Utility Agent

A command-line AI assistant powered by **Google Gemini** that selects the appropriate utility tool based on natural language input.

### Features

- ➕ Addition
- ➖ Subtraction
- ✖️ Multiplication
- ➗ Division
- 🧮 BMI Calculator
- 🎂 Age Calculator
- 🌍 KM to Miles Converter
- 🔐 Random Password Generator

## ⚙️ Workflow

```text id="x6sgph"
User Request
      │
      ▼
Google Gemini
(Chooses Tool + Parameters)
      │
      ▼
Structured JSON
      │
      ▼
Python Tool Execution
      │
      ▼
Final Result
```

## 💻 Tech Stack

- Python
- Google Gemini API
- python-dotenv
- JSON

## 📂 Project Structure

```text id="xksl1h"
Day07/
│
├── smart_utility_agent.py
├── tools.py
├── README.md
├── .env
└── .gitignore
```

## 🎯 Key Learning

A Large Language Model should **reason**, while Python should **execute deterministic tasks** like calculations, conversions, and utility functions. This separation of reasoning and execution is the foundation of modern Agentic AI systems.

---

**Next:** Day 8 — Native Function Calling with Gemini 🚀
