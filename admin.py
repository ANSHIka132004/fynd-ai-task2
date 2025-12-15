import streamlit as st
import pandas as pd
import os

FILE_NAME = "submissions.csv"

st.title("Admin Dashboard")

if not os.path.exists(FILE_NAME):
    st.warning("No submissions yet.")
else:
    df = pd.read_csv(FILE_NAME)
    st.subheader("All User Submissions")
    st.dataframe(df)
