import os
import google.generativeai as genai

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-pro")


def generate_user_response(review, rating):
    prompt = f"""
    A user gave a {rating}-star review:
    "{review}"

    Write a polite, empathetic response from a brand.
    """
    return model.generate_content(prompt).text


def summarize_review(review):
    prompt = f"""
    Summarize the following customer review in one short sentence:
    "{review}"
    """
    return model.generate_content(prompt).text


def recommend_action(review, rating):
    prompt = f"""
    A user gave a {rating}-star review:
    "{review}"

    Suggest one clear internal action the company should take.
    """
    return model.generate_content(prompt).text

