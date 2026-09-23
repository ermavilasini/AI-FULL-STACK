import ollama
while True:
    question = input("Ask the question:")
    if question.lower()=="exit"
    response = ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role": "system",
            "content":"Give answers in 2 lines only"
        }
        {
            "role": "user",
            "content": "Name only main types of AI"
        }
    ]
)
print(response["message"]["content"])
