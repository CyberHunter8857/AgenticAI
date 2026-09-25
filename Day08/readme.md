# 🤖 Day 8 — Native Function Calling with Gemini

Day 8 of my **100 Days of Agentic AI** journey.

Today I learned how to let Gemini directly invoke Python functions without manually parsing JSON or writing routing logic.

## 📚 Topics Covered

- Native Function Calling
- Tool Registration
- Python Docstrings
- Automatic Tool Selection
- Agent Architecture

## 🛠️ Project

Built a **Native Function Calling Agent** that performs mathematical operations by allowing Gemini to automatically choose and execute Python functions.

## Workflow

User → Gemini → Python Function → Final Response

## Key Learning

Instead of asking the LLM to return JSON and manually deciding which function to execute, Gemini can directly call registered Python functions. This is the production approach used in modern AI agents.
