import streamlit as st
name=st.text_input("Enter your name")
age=st.number_input("Age")
date=st.date_input("Date")
file=st.file_uploader("Select a file")
st.write(name)
st.write(age)
st.write(date)
if file is not None:
    a=file.getvalue()
    st.write(a)