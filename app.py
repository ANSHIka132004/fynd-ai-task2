import streamlit as st
from storage import save_submission

st.title("Leave a Review")

rating = st.selectbox("Select rating", [1,2,3,4,5])
review = st.text_area("Write your review")

if st.button("Submit"):
    # Dummy AI outputs (we'll replace with Gemini later)
    ai_response = "Thank you for your feedback! We really appreciate you taking the time to share your experience."
    ai_summary = "User shared feedback about service experience."
    ai_action = "Review internally and take action if needed."

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

