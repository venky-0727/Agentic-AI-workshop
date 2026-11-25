"""Day 1 experiment: compare lower and higher temperature outputs."""
import os
from openai import OpenAI

API_KEY = os.getenv("GROQ_API_KEY")
if not API_KEY:
    raise RuntimeError("Set GROQ_API_KEY before running this program.")

MODEL_NAME = "openai/gpt-oss-20b"
client = OpenAI(api_key=API_KEY, base_url="https://api.groq.com/openai/v1")

PROMPT = "Write one short, memorable tagline for Sweet Crumbs Home Bakery."

for temperature in (0.2, 1.2):
    print(f"\n--- temperature={temperature} ---")
    for attempt in range(1, 4):
        response = client.chat.completions.create(
            model=MODEL_NAME,
            temperature=temperature,
            messages=[
                {"role": "system", "content": "You are a creative bakery copywriter."},
                {"role": "user", "content": PROMPT},
            ],
        )
        print(f"{attempt}. {response.choices[0].message.content}")
