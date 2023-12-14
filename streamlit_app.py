import streamlit as st
st.title('Curriculum Vitae')
st.header('Personal Details')
name = st.text_input("Name")
email = st.text_input("Email")st.write('Name:', name)
st.write('Email:', email)

