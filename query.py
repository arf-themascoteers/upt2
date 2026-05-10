import ollama

response = ollama.chat(
    model="deepseek-r1:7b",
    messages=[{"role": "user", "content": "What is a wetland?"}]
)

print(response.message.content)
