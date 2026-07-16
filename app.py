import streamlit as st

st.title("Student Information")
st.write("Welcome to Streamlit!")

name = st.text_input("Enter your name")

if st.button("Submit"):
    st.success(f"Hello {name}")