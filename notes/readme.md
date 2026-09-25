# 📝 Agentic AI Bootcamp — Day-by-Day Notes

> Quick-reference notes for every day of the bootcamp.
> Each section covers **what was learned**, **simple definitions**, and **code examples**.

---

## 📅 Table of Contents

| Day | Topic |
|-----|-------|
| [Day 1](#day-1--python-basics--oop) | Python Basics & OOP |
| [Day 2](#day-2--apis-json--exception-handling) | APIs, JSON & Exception Handling |
| [Day 3](#day-3--first-ai-chatbot-gemini-api) | First AI Chatbot (Gemini API) |
| [Day 4](#day-4--prompt-engineering) | Prompt Engineering |
| [Day 5](#day-5--structured-outputs-json-from-llms) | Structured Outputs (JSON from LLMs) |
| [Day 6](#day-6--stateful-chatbot-with-persistent-memory) | Stateful Chatbot with Persistent Memory |
| [Day 7](#day-7--smart-utility-agent-tool-calling) | Smart Utility Agent (Tool Calling) |
| [Day 8](#day-8--native-function-calling-with-gemini) | Native Function Calling with Gemini |

---

## Day 1 — Python Basics & OOP

### What was built

- A "Hello World" script
- Functions and Classes
- A **Student Profile Manager** (mini project)

### Key Concepts

#### 1. Print Statement

The simplest way to show output in Python.

```python
print("Hello Agentic AI!")
```

#### 2. Variables

A variable stores a value so you can use it later.

```python
name = "Mayur"
age = 22
print(name)  # Output: Mayur
```

#### 3. Data Types

| Type   | Example              | Description           |
|--------|----------------------|-----------------------|
| `str`  | `"Hello"`            | Text                  |
| `int`  | `22`                 | Whole number          |
| `float`| `3.14`               | Decimal number        |
| `list` | `["Python", "Java"]` | Ordered collection    |
| `dict` | `{"name": "Mayur"}`  | Key-value pairs       |
| `bool` | `True` / `False`     | True or False         |

#### 4. Lists

A list is an ordered, changeable collection of items.

```python
languages = ["Python", "JavaScript", "C++", "Java"]

# Loop through a list
for i, lang in enumerate(languages, start=1):
    print(f"{i}. {lang}")
```

**Output:**
```
1. Python
2. JavaScript
3. C++
4. Java
```

#### 5. Dictionaries

A dictionary stores data as **key-value** pairs (like a real dictionary: word → definition).

```python
student = {
    "name": "Mayur",
    "age": 22,
    "branch": "E&TC"
}

print(student["name"])  # Output: Mayur
```

#### 6. Functions

A function is a reusable block of code that performs a specific task.

```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # Output: 8
```

#### 7. Classes & Objects (OOP)

A **class** is a blueprint for creating objects. An **object** is an instance of a class.

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Create an object
student = Student("Mayur", 22)
student.greet()
```

**Output:**
```
Hello, my name is Mayur and I am 22 years old.
```

**Key OOP Terms:**
| Term          | Meaning                                                 |
|---------------|----------------------------------------------------------|
| `class`       | A blueprint/template for objects                         |
| `object`      | An instance created from a class                         |
| `__init__`    | Constructor — runs automatically when an object is created |
| `self`        | Refers to the current object itself                      |
| `method`      | A function defined inside a class                        |

#### 8. f-Strings

An easy way to insert variables into strings.

```python
name = "Mayur"
age = 22
print(f"I am {name} and I am {age} years old.")
```

---

## Day 2 — APIs, JSON & Exception Handling

### What was built

- A calculator module (importing functions)
- Exception handling examples
- JSON parsing examples
- A **GitHub Profile Analyzer** (mini project)

### Key Concepts

#### 1. Modules & Imports

A **module** is just a `.py` file. You can import functions from one file into another.

```python
# calculator.py
def addition(a, b):
    return a + b

# main.py
from calculator import addition
print(addition(5, 3))  # Output: 8
```

#### 2. Exception Handling (`try` / `except`)

Exceptions are errors that happen while running code. Instead of crashing, you can **catch** them.

```python
try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Please enter a valid number!")
```

**Why?** Without `try/except`, your program crashes. With it, the program shows a friendly message instead.

#### 3. JSON (JavaScript Object Notation)

JSON is a format for storing and exchanging data. It looks like a Python dictionary.

```python
import json

# Python dict → JSON string (dumps)
student = {"Name": "Mayur", "Age": 21}
json_string = json.dumps(student)
print(json_string)         # '{"Name": "Mayur", "Age": 21}'
print(type(json_string))   # <class 'str'>

# JSON string → Python dict (loads)
data = json.loads(json_string)
print(data["Name"])        # Mayur
print(type(data))          # <class 'dict'>
```

**Remember:**
| Function      | Direction                     | Think of it as        |
|---------------|-------------------------------|-----------------------|
| `json.dumps()`| Python → JSON string          | **d**ump to **s**tring|
| `json.loads()`| JSON string → Python          | **l**oad from **s**tring|

#### 4. REST API

An **API** (Application Programming Interface) lets your code talk to other services over the internet.

```
Your Python Code  →  HTTP Request  →  Server  →  JSON Response  →  Your Code
```

```python
import requests

response = requests.get("https://api.github.com/users/CyberHunter8857")

if response.status_code == 200:
    data = response.json()
    print(data["name"])       # Mayur Tamanke
    print(data["followers"])  # 5
else:
    print("User not found")
```

**Common HTTP Status Codes:**
| Code | Meaning          |
|------|------------------|
| 200  | ✅ OK (Success)  |
| 404  | ❌ Not Found     |
| 500  | 💥 Server Error  |

#### 5. Environment Variables

Store secret values (API keys, passwords) outside your code using a `.env` file.

```bash
# .env file
GOOGLE_API_KEY=your_secret_key_here
```

```python
from dotenv import load_dotenv
import os

load_dotenv()  # Loads .env file

api_key = os.getenv("GOOGLE_API_KEY")
print(api_key)  # your_secret_key_here
```

**Why?** Never put API keys directly in your code — anyone who sees your code would see your key.

---

## Day 3 — First AI Chatbot (Gemini API)

### What was built

A **terminal chatbot** using Google Gemini API that:
- Chats in a loop
- Maintains conversation history in memory
- Saves the full conversation to a text file on exit

### Key Concepts

#### 1. What is an LLM?

A **Large Language Model** (LLM) is an AI trained on massive text data that can understand and generate human language. Examples: Gemini, GPT, Claude.

#### 2. Google Gemini API Setup

```python
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
```

#### 3. Making Your First AI Call

```python
response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="What is Python?"
)

print(response.text)
```

This sends your text to Google's AI and gets back a response — like texting a very smart assistant.

#### 4. Conversation History (Context)

LLMs don't remember past messages by default. To have a conversation, you send **all previous messages** with each new request.

```python
history = []

while True:
    user_input = input("You: ")
    if user_input == "exit":
        break

    history.append(f"User: {user_input}")

    # Send full history as one prompt
    prompt = "\n".join(history)

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=prompt
    )

    ai_reply = response.text
    print("AI:", ai_reply)

    history.append(f"AI: {ai_reply}")
```

**How it works:**
```
Turn 1: "Hi"                         → AI: "Hello!"
Turn 2: "Hi\nAI: Hello!\nUser: What is Python?" → AI: "Python is..."
```

Each turn sends the **entire conversation** so the AI knows what was said before.

#### 5. Saving to a File

```python
with open("chat_history.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(history))
```

---

## Day 4 — Prompt Engineering

### What was built

- An **AI Resume Reviewer**
- An **AI Interview Coach** (main project)

### Key Concepts

#### 1. What is Prompt Engineering?

Prompt Engineering is the skill of writing clear, structured instructions to get the best output from an AI model.

**Bad prompt:** `"Review my resume"`
**Good prompt:** `"Review this resume. Give: 1. Score /10, 2. Top 3 strengths, 3. Top 3 weaknesses"`

#### 2. Prompt Formula

```
Role + Task + Context + Constraints = Good Prompt
```

| Part        | Example                                       |
|-------------|-----------------------------------------------|
| **Role**    | "You are a Python mentor."                    |
| **Task**    | "Explain dictionaries."                       |
| **Context** | "I'm a third-year engineering student."       |
| **Constraints** | "Use simple English and one real-life example." |

#### 3. System Instruction

A **system instruction** tells the AI *who it should act as* before the conversation starts. It sets the AI's personality and behavior.

```python
from google.genai import types

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Review this resume...",
    config=types.GenerateContentConfig(
        system_instruction="You are a senior software recruiter."
    )
)
```

**Without system instruction:** AI answers as a generic assistant.
**With system instruction:** AI answers as a recruiter, giving scores, strengths, weaknesses.

#### 4. Dynamic Prompts

Build prompts that change based on user input using f-strings.

```python
role = input("Enter target job role: ")
question = input("Interview Question: ")
answer = input("Your Answer: ")

prompt = f"""
You are interviewing a candidate for the role of {role}.

Interview Question:
{question}

Candidate's Answer:
{answer}

Evaluate and provide:
1. Score out of 10
2. What was good (3 points)
3. What can be improved (3 points)
4. A better sample answer (max 80 words)
"""
```

**Key idea:** The prompt template stays the same, but the values change every time.

#### 5. Structured Prompt Output

Tell the AI exactly **what format** you want:

```python
prompt = """
Give:
1. Score /10
2. Top 3 strengths
3. Top 3 weaknesses
4. Missing technical skills
"""
```

This makes AI output consistent and predictable every time.

---

## Day 5 — Structured Outputs (JSON from LLMs)

### What was built

An **AI Skill Gap Analyzer** that:
- Takes a resume and job role as input
- Returns structured JSON with match analysis
- Parses JSON into a Python dictionary for display

### Key Concepts

#### 1. Why Structured Output?

Plain text → hard for code to process.
JSON output → easy for code to parse and use.

```
LLM returns: "The candidate has 3 years of experience in Python..."  ← Hard to parse
LLM returns: {"experience_years": 3, "skills": ["Python"]}          ← Easy to parse
```

**In Agentic AI**, agents need structured data (not paragraphs) to make decisions.

#### 2. JSON Schema in Prompts

Tell the AI exactly what shape the JSON should be:

```python
prompt = f"""
Extract candidate information.

Return ONLY valid JSON.
Do not use markdown.

Schema:
{{
    "name": "",
    "email": "",
    "skills": [],
    "experience_years": 0,
    "matching_skills": [],
    "missing_skills": [],
    "match_percentage": 0,
    "recommendation": ""
}}

Candidate Profile:
{resume}

Job Role:
{job_role}
"""
```

**Note:** Use `{{` and `}}` inside f-strings to get literal `{` and `}` in the output.

#### 3. Parsing JSON from AI Responses

AI sometimes wraps JSON in markdown code blocks. Clean it first, then parse:

```python
import json

# Clean the response
clean_text = response.text.replace("```json", "").replace("```", "").strip()

# Parse JSON → Python dict
try:
    data = json.loads(clean_text)
    print(data["name"])
    print(data["skills"])
except json.JSONDecodeError:
    print("AI returned invalid JSON")
```

#### 4. The Full AI Workflow

```
User Input (resume + job role)
        ↓
Prompt + JSON Schema
        ↓
Google Gemini API
        ↓
Structured JSON Response
        ↓
json.loads() → Python Dictionary
        ↓
Display Clean Report
```

#### 5. Detailed System Instruction

For complex tasks, give the AI step-by-step instructions:

```python
system_instruction = """
You are an expert AI HR Specialist.

Your task:
1. Extract candidate profile details from the resume.
2. Compare skills against the target Job Role.
3. Identify matching_skills.
4. Identify missing_skills.
5. Calculate match_percentage (0 to 100).
6. Provide a recommendation.
"""
```

---

## Day 6 — Stateful Chatbot with Persistent Memory

### What was built

A **Gemini chatbot with persistent memory** that:
- Remembers conversations even after restart
- Stores chat history in a JSON file
- Supports clear and exit commands

### Key Concepts

#### 1. Stateless vs Stateful

| Type       | Meaning                              | Example               |
|------------|--------------------------------------|-----------------------|
| **Stateless** | Forgets everything after each request | A basic API call    |
| **Stateful**  | Remembers previous interactions      | ChatGPT-like chatbot |

**LLMs are stateless by nature.** Your application must handle memory.

#### 2. Message Objects

Instead of storing plain strings, store structured message objects:

```python
# ❌ Plain string (Day 3 approach)
history = ["User: Hi", "AI: Hello!"]

# ✅ Structured objects (Day 6 approach)
history = [
    {"role": "user", "text": "Hi"},
    {"role": "model", "text": "Hello!"}
]
```

**Why?** Structured objects are easier to filter, search, and process programmatically.

#### 3. Persistent Memory (Save to File)

Save history to a JSON file so the chatbot remembers across sessions:

```python
import json

# Save history
with open("chat_history.json", "w", encoding="utf-8") as file:
    json.dump(history, file, indent=4)

# Load history on startup
import os

if os.path.exists("chat_history.json"):
    with open("chat_history.json", "r", encoding="utf-8") as file:
        history = json.load(file)
else:
    history = []
```

#### 4. Building Conversation Prompt from History

Convert structured history back into a text prompt for the AI:

```python
conversation = ""
for message in history:
    conversation += f"{message['role']}: {message['text']}\n"

response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=conversation
)
```

#### 5. Save After Every Message

Save immediately after each message — not just on exit. If the program crashes, you don't lose data:

```python
# After user message
history.append({"role": "user", "text": user_input})
with open("chat_history.json", "w") as file:
    json.dump(history, file, indent=4)

# After AI response
history.append({"role": "model", "text": ai_reply})
with open("chat_history.json", "w") as file:
    json.dump(history, file, indent=4)
```

#### 6. Memory Flow

```
App Starts
    ↓
Load chat_history.json (if exists)
    ↓
User sends message → Add to history → Save to file
    ↓
Build full conversation from history
    ↓
Send to Gemini → Get response
    ↓
Add AI response to history → Save to file
    ↓
Repeat until "exit"
```

---

## Day 7 — Smart Utility Agent (Tool Calling)

### What was built

A **Smart Utility AI Agent** powered by Google Gemini that:
- Connects an LLM to deterministic Python functions (tools)
- Decides which tool to call based on natural language input
- Extracts arguments and outputs structured JSON commands
- Executes functions for math, BMI, age calculation, unit conversions, and password generation

### Key Concepts

#### 1. What is an AI Agent?

A traditional LLM only **generates text**. An **AI Agent** can **reason, make decisions, select tools, and take actions**.

| Traditional LLM (Chatbot) | AI Agent |
|----------------------------|----------|
| Generates text responses only | Decides actions and calls external tools |
| Guesses math / calculations (prone to hallucination) | Executes exact Python functions for math & logic |
| Passive responder | Goal-driven problem solver |

**Core Philosophy of Agentic AI:**
> **LLM reasons, Code executes.**
> The LLM figures out *what* needs to be done and extracts parameters, while Python code deterministically executes the action.

#### 2. The Agentic Tool Calling Workflow

```
User Input ("Calculate BMI for 175cm and 70kg")
        │
        ▼
LLM (Gemini) Reasoning
- Identifies intent: BMI calculation
- Selects tool: "bmi"
- Extracts arguments: height_cm=175, weight_kg=70
        │
        ▼
Structured JSON Command
{"tool": "bmi", "height_cm": 175, "weight_kg": 70}
        │
        ▼
Python Dispatcher
- Parses JSON
- Routes to calculate_bmi(175, 70)
        │
        ▼
Tool Execution & Output (BMI: 22.86)
```

#### 3. Defining Deterministic Tools (`tools.py`)

Tools are modular Python functions designed to perform specific tasks reliably.

```python
# tools.py
from datetime import datetime
import random
import string

# 1. Calculator Tools
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

# 2. BMI Calculator
def calculate_bmi(height_cm, weight_kg):
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 2)

# 3. Age Calculator
def calculate_age(year, month, day):
    dob = datetime(year, month, day)
    today = datetime.today()
    age = today.year - dob.year
    if (today.month, today.day) < (dob.month, dob.day):
        age -= 1
    return age

# 4. KM to Miles Converter
def km_to_miles(km):
    return round(km * 0.621371, 3)

# 5. Password Generator
def generate_password(length):
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(random.choice(chars) for _ in range(length))
```

#### 4. Prompting the LLM for Tool Selection

Using system instructions to define available tools and provide structured JSON schemas:

```python
SYSTEM_PROMPT = """
You are an AI Utility Agent.

Available tools:

1. add(a,b)
2. subtract(a,b)
3. multiply(a,b)
4. divide(a,b)
5. bmi(height_cm, weight_kg)
6. age(year, month, day)
7. km_to_miles(km)
8. password(length)

Return ONLY valid JSON.

Schemas:

Calculator:
{
  "tool":"add",
  "a":10,
  "b":20
}

BMI:
{
  "tool":"bmi",
  "height_cm":175,
  "weight_kg":70
}

Age:
{
  "tool":"age",
  "year":2003,
  "month":5,
  "day":18
}

KM:
{
  "tool":"km_to_miles",
  "km":5
}

Password:
{
  "tool":"password",
  "length":16
}
"""
```

#### 5. Tool Dispatcher & Execution Loop

The agent receives the JSON command from Gemini, parses it, and executes the matched function:

```python
from google import genai
from google.genai import types
from dotenv import load_dotenv
from tools import *
import os
import json

load_dotenv()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

# LLM call with system prompt
response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=user_input,
    config=types.GenerateContentConfig(
        system_instruction=SYSTEM_PROMPT
    )
)

# Clean and parse JSON
clean = response.text.replace("```json", "").replace("```", "").strip()
command = json.loads(clean)
tool = command["tool"]

# Dispatch & Execute
if tool == "add":
    result = add(command["a"], command["b"])
elif tool == "subtract":
    result = subtract(command["a"], command["b"])
elif tool == "multiply":
    result = multiply(command["a"], command["b"])
elif tool == "divide":
    result = divide(command["a"], command["b"])
elif tool == "bmi":
    result = calculate_bmi(command["height_cm"], command["weight_kg"])
elif tool == "age":
    result = calculate_age(command["year"], command["month"], command["day"])
elif tool == "km_to_miles":
    result = km_to_miles(command["km"])
elif tool == "password":
    result = generate_password(command["length"])
else:
    result = "Unknown tool."

print(f"AI: {result}")
```

#### 6. Why LLMs Need External Tools

1. **Deterministic Accuracy:** LLMs predict text probabilistically and can make arithmetic errors or hallucinate. Python functions guarantee 100% mathematical precision.
2. **Real-time & System Access:** LLMs do not know dynamic runtime information (e.g., today's date for age calculation) or generate truly random secure passwords without code execution.
3. **Action Capability:** Tools transform passive language models into active agents capable of interacting with APIs, databases, files, and external systems.

---

## Day 8 — Native Function Calling with Gemini

### What was built

A **Smart Student Utility Agent** with **Native Function Calling** powered by Google Gemini SDK (`google-genai`) that:
- Leverages Gemini's native tool calling capability (`tools=[...]`)
- Eliminates manual JSON parsing, custom schema prompt engineering, and manual `if/elif` routing
- Uses Python type hints and docstrings as tool specifications for the LLM
- Automatically executes registered functions and synthesizes natural conversational answers
- Provides student calculation tools: Basic math (`add`, `subtract`, `multiply`, `divide`, `square`), Academic tools (`calculate_percentage`, `grade_from_percentage`, `calculate_cgpa`, `attendance_required`), and Utilities (`generate_password`)

### Key Concepts

#### 1. Manual Tool Calling (Day 7) vs Native Function Calling (Day 8)

| Feature | Manual Tool Calling (Day 7) | Native Function Calling (Day 8) |
|---|---|---|
| **Tool Definition** | Defined in System Prompt as text / JSON schemas | Plain Python functions with type hints & docstrings |
| **Model Output** | Raw JSON string containing tool name & arguments | SDK handles tool call protocol natively |
| **Dispatch & Execution** | Manual `json.loads()`, `if/elif` dispatcher, manual execution | Gemini SDK registers Python functions directly via `tools=[...]` |
| **Final Answer Synthesis** | Requires manual formatting or second prompt turn | Model receives tool return and synthesizes natural response automatically |
| **Maintenance & Scalability** | High overhead — prompts and Python code must stay in sync | Low overhead — pass Python function references directly |

#### 2. The Native Function Calling Workflow

```
User Input ("I attended 48 out of 70 classes, how many more to reach 75% attendance?")
                                │
                                ▼
Gemini Model (Inspects registered tools, signatures & docstrings)
                                │
                                ▼
Model determines intent & invokes `attendance_required(current=48, total=70)`
                                │
                                ▼
Python Function Executes (Returns: 18)
                                │
                                ▼
Gemini receives output & synthesizes conversational response
                                │
                                ▼
Final Output: "You need to attend 18 more consecutive classes to reach 75% attendance."
```

#### 3. Docstrings & Type Annotations as Tool Schemas

In native function calling, Python functions **are** the API contracts. Gemini inspects the function name, type hints (`int`, `float`, `str`), and docstrings (`"""..."""`) to understand when and how to call each tool:

```python
def attendance_required(current: int, total: int):
    """
    Calculate the number of consecutive classes required
    to reach 75% attendance.
    """
    if total == 0:
        return "Total classes cannot be zero."

    target = 0.75

    if current / total >= target:
        return 0

    required = math.ceil(
        (target * total - current) / (1 - target)
    )

    return required
```

**Why Type Hints and Docstrings Matter:**
- **Docstrings:** Tell the LLM **what** the tool does and **when** to choose it.
- **Type Hints (`a: float, b: float`):** Tell the LLM **what data types** to pass for each argument.
- **Parameter Names (`current`, `total`):** Help the LLM extract the correct values from user text.

#### 4. Defining Native Tools (`tools.py`)

Tools are written as clean, standalone Python functions:

```python
import math
import random
import string

# 1. Basic Calculator
def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b

def subtract(a: float, b: float) -> float:
    """Subtract two numbers."""
    return a - b

def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b

def divide(a: float, b: float):
    """Divide two numbers."""
    if b == 0:
        return "Cannot divide by zero."
    return round(a / b, 2)

def square(a: float) -> float:
    """Return square of a number."""
    return a * a

# 2. Student Utilities
def calculate_percentage(marks: float, total_marks: float) -> float:
    """Calculate percentage from obtained and total marks."""
    if total_marks == 0:
        return 0
    return round((marks / total_marks) * 100, 2)

def grade_from_percentage(percent: float) -> str:
    """Convert percentage into a letter grade."""
    if percent < 0 or percent > 100:
        return "Invalid Percentage"
    if percent >= 90:
        return "A+"
    elif percent >= 80:
        return "A"
    elif percent >= 70:
        return "B"
    elif percent >= 60:
        return "C"
    elif percent >= 50:
        return "D"
    elif percent >= 40:
        return "E"
    else:
        return "F"

def calculate_cgpa(total_points: float) -> float:
    """Convert total grade points into CGPA."""
    return round(total_points / 10, 2)

def attendance_required(current: int, total: int):
    """Calculate the number of consecutive classes required to reach 75% attendance."""
    if total == 0:
        return "Total classes cannot be zero."
    target = 0.75
    if current / total >= target:
        return 0
    required = math.ceil((target * total - current) / (1 - target))
    return required

# 3. Extra Utility
def generate_password(length: int) -> str:
    """Generate a secure random password."""
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(random.choice(chars) for _ in range(length))
```

#### 5. Registering Native Tools with Gemini SDK (`native_function_agent.py`)

Register the functions directly in `types.GenerateContentConfig(tools=...)`:

```python
from google import genai
from google.genai import types
from dotenv import load_dotenv
from tools import *
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

# Register native Python functions as tools
TOOLS = [
    add,
    subtract,
    multiply,
    divide,
    square,
    calculate_percentage,
    grade_from_percentage,
    calculate_cgpa,
    attendance_required,
    generate_password
]

SYSTEM_PROMPT = """
You are a Smart Student Utility Agent.

Use the available Python tools whenever needed.
Do not calculate manually if a suitable tool exists.
"""

# Native Function Calling Execution
response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents="I scored 420 out of 500. What is my percentage and grade?",
    config=types.GenerateContentConfig(
        system_instruction=SYSTEM_PROMPT,
        tools=TOOLS
    )
)

print(f"AI: {response.text}")
```

#### 6. Why Native Function Calling is the Production Standard

1. **Zero JSON Parsing Boilerplate:** No string stripping, regex manipulation, or manual `json.loads()` handling.
2. **Automatic Execution & Result Feeding:** The Gemini SDK handles calling the function and supplying its return value back to the model seamlessly.
3. **Multi-Step & Multi-Tool Reasoning:** The model can call multiple functions across reasoning steps to fulfill complex user prompts.
4. **Maintainable & Extensible:** Adding a new tool is as simple as defining a standard Python function and adding it to the `TOOLS` list.

---

## 🧠 Concepts Progression Summary

| Day | Concept                 | Why It Matters for Agentic AI |
|-----|-------------------------|-------------------------------|
| 1   | Python Basics & OOP     | Foundation — everything is built on this |
| 2   | APIs & JSON             | AI models communicate through APIs returning JSON |
| 3   | First LLM API call      | Core skill — calling AI models from code |
| 4   | Prompt Engineering      | Better prompts = better AI output |
| 5   | Structured Outputs      | Agents need JSON, not paragraphs, to make decisions |
| 6   | Memory & Persistence    | Real AI assistants remember past conversations |
| 7   | Tool Calling & Agents   | Separation of reasoning (LLM) and execution (code) |
| 8   | Native Function Calling | Production agent architecture — Gemini directly registers and executes Python functions |

---

> **Next up:** Day 9 — Advanced Agent Workflows & Multi-Tool Orchestration 🚀
