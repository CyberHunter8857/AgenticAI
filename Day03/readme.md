# Day 03 - Simple Terminal Chatbot (Gemini API)

A basic command-line chatbot built using Google's Gemini API. It keeps track of the conversation history in memory, lets you clear it mid-chat, and saves the full conversation to a text file when you exit.

## Features

- Takes your name and greets you
- Chat continuously with the Gemini model (`gemini-3.5-flash`)
- Maintains conversation context (sends full history with each prompt)
- `clear` command to reset chat history
- `exit` command to quit
- Saves the entire conversation to `chat_history.txt` on exit

## Files

- `chatbot.py` - main chatbot script
- `chat_history.txt` - example saved conversation from a previous run

## Requirements

```bash
pip install google-genai python-dotenv
```

## Setup

1. Create a `.env` file in this folder with your Gemini API key:

   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

2. Run the script:

   ```bash
   python chatbot.py
   ```

## Usage

- Enter your name when prompted
- Type your message and press Enter to chat
- Type `clear` to wipe the current chat history
- Type `exit` to end the chat (this also saves the conversation to `chat_history.txt`)

## Notes

- Each new message is sent along with the full prior conversation, so the model has context.
- The saved model name in the script is `gemini-3.5-flash` - update it if you're using a different available model.
