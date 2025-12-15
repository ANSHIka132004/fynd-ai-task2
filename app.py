import streamlit as st
from storage import save_submission
from llm_utils import (
    generate_user_response,
    summarize_review,
    recommend_action
)

st.title("Leave a Review")

rating = st.selectbox("Select rating", [1,2,3,4,5])
review = st.text_area("Write your review")

if st.button("Submit"):
    ai_response = generate_user_response(review, rating)
    ai_summary = summarize_review(review)
    ai_action = recommend_action(review, rating)

    save_submission(
        rating,
        review,
        ai_response,
        ai_summary,
        ai_action
    )

    st.success("Thanks for your feedback!")
    st.write("🤖 AI Response:")
    st.write(ai_response)

