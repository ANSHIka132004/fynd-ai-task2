import os
import requests

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
API_URL = "https://openrouter.ai/api/v1/chat/completions"

def call_llm(prompt):
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
    }

    data = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(API_URL, headers=headers, json=data)
    response.raise_for_status()
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

