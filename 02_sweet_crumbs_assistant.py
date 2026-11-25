"""Day 1 build: Sweet Crumbs Home Bakery support assistant."""
import os
from openai import OpenAI

API_KEY = os.getenv("GROQ_API_KEY")
if not API_KEY:
    raise RuntimeError("Set GROQ_API_KEY before running this program.")

MODEL_NAME = "openai/gpt-oss-20b"

SYSTEM_PROMPT = """ROLE:
You are the customer-support assistant for Sweet Crumbs Home Bakery.

FACTS:
- We bake to order.
- Orders need 24 hours' notice.
- All cakes have eggless versions.
- Plum cake costs Rs 500.
- Chocolate cake costs Rs 650.
- Cupcake costs Rs 80.

RULES:
- Never promise a delivery time.
- Do not invent delivery charges, stock, discounts or policies.
- If the answer is not present in FACTS, say: "I'll check with the owner."

STYLE:
- Be friendly and concise.
- Reply in English or Telugu according to the customer's language.
- Keep the answer under 50 words.
"""

client = OpenAI(
    api_key=API_KEY,
    base_url="https://api.groq.com/openai/v1",
)

def ask_bakery(question: str) -> None:
    response = client.chat.completions.create(
        model=MODEL_NAME,
        temperature=0.2,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": question},
        ],
    )
    print(response.choices[0].message.content)
    print("\nUsage:", response.usage)

if __name__ == "__main__":
    customer_question = input("Customer question: ").strip()
    if customer_question:
        ask_bakery(customer_question)
