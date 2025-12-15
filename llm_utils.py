import os
import requests

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
API_URL = "https://openrouter.ai/api/v1/chat/completions"

def call_llm(prompt):
    if not OPENROUTER_API_KEY:
        raise ValueError("OPENROUTER_API_KEY not found in environment variables")

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        # REQUIRED by OpenRouter
        "HTTP-Referer": "https://streamlit.io",
        "X-Title": "Fynd AI Task 2"
    }

    data = {
        # very safe, always-available model
        "model": "mistralai/mistral-7b-instruct",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(API_URL, headers=headers, json=data)

    # Helpful debug if something still fails
    if response.status_code != 200:
        raise RuntimeError(
            f"OpenRouter error {response.status_code}: {response.text}"
        )

    return response.json()["choices"][0]["message"]["content"]


def generate_user_response(review, rating):
    prompt = f"""
A customer gave a {rating}-star review:
"{review}"

Write a polite, empathetic response from the company.
"""
    return call_llm(prompt)


def summarize_review(review):
    prompt = f"""
Summarize this customer review in one short sentence:
"{review}"
"""
    return call_llm(prompt)


def recommend_action(review, rating):
    prompt = f"""
A customer gave a {rating}-star review:
"{review}"

Suggest one clear internal action the company should take.
"""
    return call_llm(prompt)

