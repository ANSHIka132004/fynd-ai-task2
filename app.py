import streamlit as st

st.title("Leave a Review")

rating = st.selectbox("Select rating", [1,2,3,4,5])
review = st.text_area("Write your review")

if st.button("Submit"):
    st.success("Thanks for your feedback!")
    st.write("Rating:", rating)
    st.write("Review:", review)
