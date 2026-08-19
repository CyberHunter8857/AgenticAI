# 🚀 Day 2 — Python APIs, JSON & Exception Handling

Day 2 of my **100 Days of Agentic AI journey**.

Today I focused on learning how Python communicates with external services through **APIs** and how API data is handled using **JSON**.

## 📚 Topics Covered

- Python Modules & Packages
- Exception Handling
- `try` / `except`
- File Handling
- JSON
- HTTP Requests
- REST APIs
- HTTP Status Codes
- Environment Variables
- API Error Handling

## 🛠️ Mini Project — GitHub Profile Analyzer

For today's project, I built a simple **GitHub Profile Analyzer** using the GitHub REST API.

The program:

1. Takes a GitHub username as input.
2. Sends a request to the GitHub API.
3. Receives the user's profile data in JSON format.
4. Extracts useful information from the response.
5. Displays the user's GitHub profile details.
6. Handles API errors using exception handling.
7. Calculates the follower/following ratio.

### Information Displayed

- Name
- Username
- Bio
- Followers
- Following
- Follower/Following Ratio
- Public Repositories
- GitHub Profile URL

## 💻 Technologies Used

- Python
- Requests
- REST API
- JSON
- Exception Handling

## 📂 Project Structure

```text
Day02/
│
├── github_user.py
└── README.md
```

## 🔑 Key Learning

The most important concept I learned today was the basic API communication flow:

```text
Python Application
       ↓
   HTTP Request
       ↓
    REST API
       ↓
     Server
       ↓
   JSON Response
       ↓
 Python Application
```

This concept will be fundamental for building AI applications because LLMs and AI agents also communicate with external services through APIs.

## 🎯 What's Next?

**Day 3:** My first LLM API call and understanding how AI models communicate with Python.

> One step closer to building real Agentic AI systems. 🤖🚀
