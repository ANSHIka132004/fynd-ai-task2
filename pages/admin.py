import streamlit as st
import pandas as pd
import os

st.title("Admin Dashboard")

FILE_NAME = "submissions.csv"

if not os.path.exists(FILE_NAME):
    st.warning("No submissions yet.")
else:
    df = pd.read_csv(FILE_NAME)
    st.dataframe(df)

