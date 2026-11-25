"""Day 1: Your first Groq API call.

Set GROQ_API_KEY in the environment before running this file.
In Google Colab, add it to Secrets and set os.environ in a setup cell.
"""
import os
from openai import OpenAI

API_KEY = os.getenv("GROQ_API_KEY")
if not API_KEY:
    raise RuntimeError(
        "GROQ_API_KEY is missing. Add it to Colab Secrets or your environment."
    )

MODEL_NAME = "openai/gpt-oss-20b"  # Check Groq's current model catalogue if unavailable.

client = OpenAI(
    api_key=API_KEY,
    base_url="https://api.groq.com/openai/v1",
)

response = client.chat.completions.create(
    model=MODEL_NAME,
    messages=[
        {"role": "system", "content": "You are a funny joker."},
        {"role": "user", "content": "Tell me a short joke."},
    ],
)

print("Assistant:")
print(response.choices[0].message.content)
print("\nToken usage:")
print(response.usage)
