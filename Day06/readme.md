# 🚀 Day 6 — Stateful AI Chatbot with Persistent Memory

Day 6 of my **100 Days of Agentic AI** journey.

## 📚 Topics Covered

- Stateless vs Stateful AI
- Conversation Memory
- JSON-based Message Objects
- Persistent Memory
- File Handling
- Error Handling
- Multi-turn Conversations

## 🛠️ Project

Built a **Gemini Memory Chatbot** that remembers previous conversations by storing chat history in a JSON file.

### Features

- Load previous conversations automatically
- Multi-turn contextual chat
- Persistent memory using `chat_history.json`
- `clear` command to erase memory
- `exit` command to save and quit
- Structured message objects (`role`, `text`)
- Gemini API integration with error handling

## 📂 Project Structure

```text
Day06/
│
├── memory_chatbot.py
├── chat_history.json
├── README.md
├── .env
└── .gitignore
```

## 💡 Key Learning

Large Language Models are **stateless**. Memory is created by the application, not the model itself. By storing conversation history and sending it with every request, we can build stateful AI assistants similar to ChatGPT.

---

**Next:** Day 7 — Tool Calling & Function Calling (Real Agentic AI)
