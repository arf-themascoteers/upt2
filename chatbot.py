import ollama
import json
from pathlib import Path

HISTORY_FILE = Path("history.json")

def load_history():
    if HISTORY_FILE.exists():
        return json.loads(HISTORY_FILE.read_text())
    return []

def save_history(history):
    HISTORY_FILE.write_text(json.dumps(history, indent=2))

history = load_history()

while True:
    user_input = input("You: ")
    if user_input.lower().strip() in ("exit", "quit"):
        break

    history.append({"role": "user", "content": user_input})

    response = ollama.chat(model="deepseek-r1:7b", messages=history)

    reply = response.message.content
    history.append({"role": "assistant", "content": reply})
    save_history(history)

    print(f"Bot: {reply}\n")
