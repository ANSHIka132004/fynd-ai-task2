# Fynd AI Intern – Take Home Assessment

This repository contains my submission for the Fynd AI Intern Take Home Assessment. The assessment consists of two tasks focused on prompt engineering, evaluation, and building a web-based AI feedback system.

--------------------------------------------------

## Task 1: Rating Prediction via Prompting

### Objective
Classify Yelp reviews into 1–5 star ratings using prompt-based LLM inference and return structured JSON output.

### Dataset
- Yelp Reviews Dataset (sampled for efficiency)

### Approach
- Designed three distinct prompting strategies to classify reviews.
- Prompts were iteratively refined to:
  - Improve accuracy
  - Enforce structured JSON output
  - Improve reliability and consistency

### Output Format
Example output returned by the model:

{
  "predicted_stars": 4,
  "explanation": "Brief reasoning for the assigned rating."
}

### Evaluation
Each prompting strategy was evaluated on:
- Accuracy (actual vs predicted rating)
- JSON validity rate
- Reliability and consistency

A comparison table and discussion are included in the notebook.

### Files
- task1_rating_prediction.ipynb

--------------------------------------------------

## Task 2: Two-Dashboard AI Feedback System (Web-Based)

### Objective
Build a web-based AI feedback system with two dashboards:
- User Dashboard (public-facing)
- Admin Dashboard (internal-facing)

Both dashboards must be deployed, accessible via public URLs, and must read/write from the same data source.

--------------------------------------------------

## User Dashboard

### Features
- Select a star rating (1–5)
- Write a short textual review
- Submit feedback

### On Submission
- An AI-generated user-facing response is returned
- The submission is stored in a shared data source

--------------------------------------------------

## Admin Dashboard

### Features
The Admin Dashboard displays a live-updating list of all submissions, including:
- User rating
- User review
- AI-generated summary
- AI-suggested recommended action

Both dashboards access the same persisted data source to ensure consistency.

--------------------------------------------------

## LLM Usage

Large Language Models are used for:
- Generating user-facing responses
- Review summarisation
- Recommended next actions

LLM access is handled via OpenRouter. API keys are securely managed using Streamlit Secrets and are not committed to the repository.

--------------------------------------------------

## Architecture

- Single Streamlit application with multiple pages
- User Dashboard implemented in app.py
- Admin Dashboard implemented as a Streamlit page in pages/admin.py
- Shared CSV-based storage for all submissions

--------------------------------------------------

## Tech Stack

- Python
- Streamlit (multi-page application)
- OpenRouter (LLM API)
- Pandas
- Requests
- CSV-based persistence

--------------------------------------------------

## Deployment

- Application deployed on Streamlit Cloud
- Both dashboards are accessible via public URLs
- Admin dashboard is accessible via the sidebar within the same deployed app

--------------------------------------------------

## Files

- app.py
- pages/admin.py
- llm_utils.py
- storage.py
- requirements.txt
- task1_rating_prediction.ipynb

--------------------------------------------------
## 🚀 Live Deployments

- **User Dashboard:** https://fynd-ai-task2-4kzew33j25msm4hgm8zxmk.streamlit.app/
- **Admin Dashboard:** https://fynd-ai-task2-4kzew33j25msm4hgm8zxmk.streamlit.app/admin



