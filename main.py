
import os
import json

from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

with open("candidate_profile.json", "r", encoding="utf-8") as file:
    candidate_profile = json.load(file)

SYSTEM_PROMPT = f"""
You are an AI assistant representing Ashwani Upadhyay.

Candidate Profile:
{json.dumps(candidate_profile, indent=2)}

Rules:
1. Answer only using the provided profile.
2. Never invent skills or experience.
3. If information is unavailable, say so.
4. Be professional and concise.
"""

# Conversation history
messages = [
    {"role": "system", "content": SYSTEM_PROMPT}
]

print("Ashwani AI Portfolio Chatbot")
print("Type 'exit' to quit.\n")


while True:

    question = input("You: ")

    if question.lower() == "exit":
        print("Chatbot closed!")
        break

    messages.append({
        "role": "user",
        "content": question
    })

    # Streaming LLM call
    stream = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=messages,
        temperature=0.3,
        stream=True
    )

    print("\nAI: ", end="", flush=True)

    answer = ""

    for chunk in stream:
        content = chunk.choices[0].delta.content

        if content:
            print(content, end="", flush=True)
            answer += content

    print("\n")

    # Save assistant response
    messages.append({
        "role": "assistant",
        "content": answer
    })
