import requests
import json

MODEL = "phi3:mini"


# -----------------------------
# Streaming Response
# -----------------------------
def generate_response_stream(prompt):

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": True
        },
        stream=True
    )

    for line in response.iter_lines():

        if line:

            data = json.loads(line.decode("utf-8"))

            yield data["response"]


# -----------------------------
# Conversation Summary
# -----------------------------
def summarize_conversation(summary, messages):

    conversation = ""

    # Previous summary
    if summary:

        conversation += f"Existing Summary:\n{summary}\n\n"

    conversation += "Conversation:\n\n"

    for msg in messages:

        conversation += (
            f"{msg['role'].capitalize()}: "
            f"{msg['content']}\n"
        )

    prompt = f"""
You are creating memory for an AI assistant.

Summarize the following conversation.

Include:
- Important topics
- User preferences
- Important facts
- Decisions made

Ignore greetings.

Keep the summary under 150 words.

{conversation}

Updated Summary:
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"].strip()