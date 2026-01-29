   import streamlit as st

st.title("Simple Streamlit App")

name = st.text_input("Enter your name")

if st.button("Click Me"):
    st.write("Hello", name)
