import streamlit as st
import pandas as pd

st.title('Chat History')

df = pd.read_csv('chat_history.csv')
st.dataframe(df, hide_index=True)