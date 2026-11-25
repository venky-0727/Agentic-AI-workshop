# Agentic AI Workshop — Day 1
## How LLMs Work and Your First Groq API Call

This repository organizes the Day 1 workshop into runnable Google Colab exercises.

### Day 1 learning outcomes
By the end of Day 1, you should be able to:
- Explain why developers use model APIs instead of training every model themselves.
- Describe an LLM as a next-token prediction system.
- Understand tokens, temperature, conversation history, context windows and hallucinations.
- Explain the role of an AI engineer.
- Make a chat-completion request to Groq from Python.
- Build a simple, fact-grounded customer-support assistant for the fictional **Sweet Crumbs Home Bakery**.

### Workshop agenda (approximately 2 hours)

| Topic | Time | Key idea |
|---|---:|---|
| 1. Why AI is everywhere now | 10 min | Ready-made models are accessible through APIs |
| 2. What an LLM does | 10 min | Next-token prediction in a loop |
| 3. Tokens | 10 min | Units used for input, output and pricing |
| 4. Temperature | 10 min | Lower is more focused; higher is more varied |
| 5. No memory by default | 10 min | Your application resends conversation history |
| 6. Context window | 10 min | Instructions, history, documents and output share a token budget |
| 7. Hallucination | 15 min | Plausible text can still be wrong; provide trusted facts |
| 8. The AI engineer | 10 min | Build a product around a model |
| 9. First API call | 25 min | Configure Groq and call a chat model |
| Practice/build | 20 min | Bakery assistant and experiments |

The source workshop also contains interactive diagrams, demonstrations and two quiz questions per topic. Use the original HTML lesson for those visual explanations.

---

## Repository structure

```text
agentic-ai-day1/
├── README.md
├── requirements.txt
├── 01_first_groq_api_call.py
├── 02_sweet_crumbs_assistant.py
├── 03_temperature_experiment.py
└── notebooks/
    └── Agentic_AI_Day1_Groq_Colab.ipynb
```

### Files
- `01_first_groq_api_call.py` — the basic API request, equivalent to the lesson's first joke example.
- `02_sweet_crumbs_assistant.py` — the bakery assistant using facts and rules from the lesson.
- `03_temperature_experiment.py` — compares repeated generations at two temperature settings.
- `notebooks/Agentic_AI_Day1_Groq_Colab.ipynb` — Colab-ready guided notebook with setup and exercises.
- `requirements.txt` — Python dependency list.

---

## 1. Create a Groq API key

1. Open [Groq Console](https://console.groq.com/).
2. Sign in and open **API Keys**.
3. Create a key and copy it once.
4. Treat the key like a password. Do not paste it into source code, screenshots, public notebooks or GitHub.

Groq provides an OpenAI-compatible API. The Python `openai` package can therefore be used with Groq by setting the Groq `base_url`.

Official references:
- [Groq documentation](https://console.groq.com/docs/overview)
- [Groq API reference](https://console.groq.com/docs/api-reference)
- [Groq models](https://console.groq.com/docs/models)

The model ID used in the workshop source is `openai/gpt-oss-20b`. Model availability and limits can change. If Groq reports that the model is unavailable, check the current model catalogue in the Groq Console and replace `MODEL_NAME` in the notebook/script with an available chat model ID.

---

## 2. Run the notebook in Google Colab

1. Download this repository ZIP and extract it, or download the notebook file.
2. Go to [Google Colab](https://colab.research.google.com/).
3. Choose **File → Upload notebook** and upload `Agentic_AI_Day1_Groq_Colab.ipynb`.
4. In Colab, open the **Secrets** panel (key icon in the left sidebar).
5. Add a secret named exactly `GROQ_API_KEY`.
6. Paste your Groq key into the secret value and enable **Notebook access**.
7. Run the notebook cells from top to bottom using the play icon or **Runtime → Run all**.
8. If Colab asks for permission to access the secret, approve it.

Do not put your actual API key in a notebook cell. The notebook reads it from Colab Secrets.

### First run: what should happen?
- The install cell installs the `openai` Python package.
- The client setup cell reads `GROQ_API_KEY` and configures the Groq endpoint.
- The first API cell sends a joke prompt.
- The response cell prints the assistant text and token usage.

---

## 3. Run the Python files in Colab

You can upload a `.py` file to Colab using the Files panel, or paste its contents into a code cell. Before running a script, run the setup cells below:

```python
!pip -q install openai
from google.colab import userdata
import os
os.environ["GROQ_API_KEY"] = userdata.get("GROQ_API_KEY")
```

Then run a script after uploading it:

```python
!python 01_first_groq_api_call.py
```

For `02_sweet_crumbs_assistant.py` or `03_temperature_experiment.py`, use the same setup first. The scripts read the key from the `GROQ_API_KEY` environment variable.

---

## 4. Run locally (optional)

```bash
python -m venv .venv
```

Activate the environment:

**Windows PowerShell**
```powershell
.venv\Scripts\Activate.ps1
```

**macOS/Linux**
```bash
source .venv/bin/activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Set the key for the current terminal session:

**Windows PowerShell**
```powershell
$env:GROQ_API_KEY="your_groq_api_key"
```

**macOS/Linux**
```bash
export GROQ_API_KEY="your_groq_api_key"
```

Run:
```bash
python 01_first_groq_api_call.py
python 02_sweet_crumbs_assistant.py
python 03_temperature_experiment.py
```

Never commit a real API key or a `.env` file containing the key.

---

## 5. Understand the Groq client code

```python
from openai import OpenAI

client = OpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1",
)

response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Tell me a joke."},
    ],
)

print(response.choices[0].message.content)
```

- `OpenAI(...)` creates/configures the client. It does not itself send the chat request.
- `base_url` points the OpenAI-compatible client to Groq.
- `model` selects the model.
- `messages` contains the instructions and user prompt.
- `.create(...)` sends the request and waits for the response.
- `response.choices[0].message.content` extracts the generated text.
- `response.usage` reports token usage when returned by the provider.

---

## 6. Day 1 practical exercises

1. **Temperature:** ask for a bakery tagline several times with temperature `0.2`, then with `1.2`. Compare consistency and variety.
2. **Hallucination:** remove the bakery facts and ask whether delivery to a location is available. Notice whether the model guesses. Do not treat a guess as policy.
3. **Memory:** make one API call saying “My name is Ravi”, then a separate call asking “What is my name?” without sending the earlier message. Then resend both messages in one conversation and compare.
4. **Tokens:** compare `response.usage` for a short English prompt and a Telugu prompt. Token counts vary by tokenizer and text.
5. **Your own business:** write five verified facts and three rules for a business you know. Replace the sample system prompt and test three customer questions.

### Sweet Crumbs sample facts from the workshop
- Cakes are baked to order.
- Orders need 24 hours' notice.
- All cakes have eggless versions.
- Plum cake: ₹500.
- Chocolate cake: ₹650.
- Cupcake: ₹80.
- Never promise a delivery time.
- If the answer is not in the supplied facts, say: “I'll check with the owner.”

These are fictional workshop facts, not real business information.

---

## 7. Common errors

| Error | Likely meaning | What to check |
|---|---|---|
| `api_key client option must be set` | The key was not loaded | Secret spelling: `GROQ_API_KEY`; Colab Notebook access |
| `401 AuthenticationError` | Key is invalid, expired or sent to the wrong provider | Create/check a Groq key and confirm the Groq base URL |
| `404 model not found` | Model ID is unavailable or misspelled | Check Groq's current model catalogue |
| `429 RateLimitError` | Request/rate limit reached | Wait, reduce repeated calls, check account limits |
| `ModuleNotFoundError: openai` | Package not installed in this runtime | Run `!pip -q install openai` |
| `SecretNotFoundError` | Colab secret does not exist under that name | Add `GROQ_API_KEY` in the Secrets panel |

---

## 8. Before Day 2

Write down the ten questions customers most often ask about your chosen business. Day 2 can use these questions to design a stronger system prompt, conversation history and a first test file.

## Safety checklist
- [ ] API key is stored in Colab Secrets or an environment variable.
- [ ] No API key is present in code, notebook output, screenshots or Git history.
- [ ] The model's answer is checked against the supplied facts.
- [ ] Prices, availability and delivery promises are not accepted without verification.
