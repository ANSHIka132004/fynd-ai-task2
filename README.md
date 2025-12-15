# Fynd AI Intern – Take Home Assessment

This repository contains my submission for the Fynd AI Intern Take Home Assessment, which consists of two tasks focused on prompt engineering, evaluation, and building a web-based AI feedback system.

##Task 1: Rating Prediction via Prompting
Objective

Classify Yelp reviews into 1–5 star ratings using prompt-based LLM inference and return structured JSON output.

Dataset

Yelp Reviews Dataset (sampled for efficiency)

Approach

Designed three distinct prompting strategies to classify reviews.

Each prompt was iteratively refined to:

Improve accuracy

Enforce structured JSON output

Improve response consistency

Output Format
{
  "predicted_stars": 4,
  "explanation": "Brief reasoning for the assigned rating."
}

Evaluation

Each prompting strategy was evaluated on:

Accuracy (actual vs predicted)

JSON validity rate

Reliability and consistency

A comparison table and discussion are included in the notebook.

Files

task1_rating_prediction.ipynb

###Task 2: Two-Dashboard AI Feedback System (Web-Based)
Objective

Build a web-based application with two dashboards:

User Dashboard (public-facing)

Admin Dashboard (internal-facing)

Both dashboards read and write to the same data source and are fully deployed.

User Dashboard

Features:

Select a star rating

Write a short review

Submit feedback

On submission:

An AI-generated user-facing response is returned

The data is stored in a shared data source

Admin Dashboard

Displays a live-updating list of submissions, including:

User rating

User review

AI-generated summary

AI-suggested recommended action

LLM Usage

LLMs are used for:

User-facing response generation

Review summarization

Recommended next actions

LLM access is handled via OpenRouter, with API keys managed securely using Streamlit Secrets.

Architecture and Tech Stack

Python

Streamlit (multi-page application)

OpenRouter (LLM API)

Pandas

Requests

CSV-based persistence

Repository Structure
├── app.py
├── pages/
│   └── admin.py
├── llm_utils.py
├── storage.py
├── requirements.txt
├── task1_rating_prediction.ipynb
├── README.md

Deployed Dashboards

User Dashboard URL:
<ADD USER DASHBOARD URL HERE>

Admin Dashboard URL:
<ADD ADMIN DASHBOARD URL HERE>
(Admin dashboard is accessible via the sidebar in the same application.)
