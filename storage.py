import csv
import os
from datetime import datetime

FILE_NAME = "submissions.csv"

def save_submission(rating, review, ai_response, ai_summary, ai_action):
    file_exists = os.path.isfile(FILE_NAME)

    with open(FILE_NAME, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow([
                "timestamp",
                "rating",
                "review",
                "ai_response",
                "ai_summary",
                "ai_action"
            ])

        writer.writerow([
            datetime.now().isoformat(),
            rating,
            review,
            ai_response,
            ai_summary,
            ai_action
        ])

