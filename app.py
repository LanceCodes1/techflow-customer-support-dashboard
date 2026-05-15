import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

DATABASE_URL = "sqlite:///data/techflow_support.db"

engine = create_engine(DATABASE_URL)

query = "SELECT * FROM support_calls"

df = pd.read_sql(query, engine)

st.title("TechFlow Customer Support Dashboard")

st.subheader("Support Call Dataset")
st.dataframe(df.head(20))

st.subheader("Average Call Duration")
st.write(round(df["call_duration"].mean(), 2), "minutes")

st.subheader("Average Satisfaction Score")
st.write(round(df["satisfaction_score"].mean(), 2))

st.subheader("Issue Type Breakdown")
st.bar_chart(df["issue_type"].value_counts())

st.subheader("Resolution Status Breakdown")
st.bar_chart(df["resolution_status"].value_counts())