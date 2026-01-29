   import streamlit as st
import pandas as pd

st.title("Predefined Data App")

# Predefined data
data = {
    "Name": ["Arun", "Bala", "Charan"],
    "Marks": [85, 90, 78]
}

df = pd.DataFrame(data)

st.write("Student Marks")
st.dataframe(df)
