import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Atharva Chaphe")
    content = ("Hi, I am Atharva Chaphe! I am a Python Developer." 
               "I graduated in June 2024 with a Bachelor's degree in Computer Science and an honor's degree in Data Science and Visualisation from Pune University."
               "I scored had an overall CGPA of 8.48 on the scale of 10."
               "I have completed several course certifications in C Programming , CPP, Python and MySQL."
               "I completed two interships"
               " - Anikaay Integration as a junior Data Analyst."
               " - Techview Web Solutions Pvt. Ltd. as a Trainee Web Developer.")
    st.info(content)

content2 = "Below you can find some of my apps I have build in Python. Feel free to contact me!"
st.write(content2)