import streamlit as st
import pandas as pd
import os

FILE_NAME = "submissions.csv"

st.title("Admin Dashboard")

if not os.path.exists(FILE_NAME):
    st.warning("No submissions yet.")
else:
    # Python engine handles inconsistent columns safely
    df = pd.read_csv(FILE_NAME, engine="python")
    st.dataframe(df)

