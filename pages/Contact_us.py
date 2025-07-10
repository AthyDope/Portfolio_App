import streamlit as st
from send_email import send_email
import pandas

df = pandas.read_csv("topics.csv")

st.header("Contact Us")

with st.form(key='email_form'):
    user_email = st.text_input("Enter your email address")
    option = st.selectbox(
        'What topic you want to discuss?', df['Topic'])
    raw_message = st.text_area("Text")
    message = f"""\
Subject: New email from {user_email}
From: {user_email}
Topic: {option}
{raw_message}"""
    message = message + "\n" + user_email
    button = st.form_submit_button("Submit")
    print(button)
    if button:
        send_email(user_email, option, raw_message)
        st.info("An Email has sent please check!")

st.markdown("---", unsafe_allow_html=True)

st.markdown("""
<div style='text-align: center;'>
    <p style='font-size:18px;'>📱 Connect with me</p>
    <div style='display: flex; justify-content: center; gap: 25px; margin-top: 10px;'>
        <a href='https://www.linkedin.com/in/atharva-chaphe-65545b234/' target='_blank'>
            <img src='https://cdn-icons-png.flaticon.com/512/174/174857.png' width='28' title='LinkedIn'/>
        </a>
        <a href='https://github.com/AthyDope' target='_blank'>
            <img src='https://cdn-icons-png.flaticon.com/512/733/733553.png' width='28' title='GitHub'/>
        </a>
        <a href='https://twitter.com/atharv_chaphe/' target='_blank'>
            <img src='https://cdn-icons-png.flaticon.com/512/733/733579.png' width='28' title='Twitter'/>
        </a>
        <a href='https://www.instagram.com/atharva_chaphe/' target='_blank'>
            <img src='https://cdn-icons-png.flaticon.com/512/2111/2111463.png' width='28' title='Instagram'/>
        </a>
        <a href='https://mail.google.com/mail/?view=cm&to=atharvachaphe7@gmail.com&su=Hello%20Atharva&body=I%20visited%20your%20portfolio%20and%20wanted%20to%20connect!'  target='_blank'>
            <img src='https://cdn-icons-png.flaticon.com/512/732/732200.png' width='28' title='Gmail'/>
        </a>
        <a href="https://leetcode.com/atharvachaphe7" target='_blank'>
            <img src='https://upload.wikimedia.org/wikipedia/commons/1/19/LeetCode_logo_black.png' width='28' title='LeetCode'/>
        </a>
    </div>
</div>
""", unsafe_allow_html=True)

# ---- Footer HTML + CSS ----
st.markdown("""
<style>
.footer-container {
    font-size: 14px;
    color: #cccccc;
    text-align: center;
    padding: 10px 0 30px 0;
}
.footer-line {
    border-top: 1px solid #333333;
    margin-top: 40px;
    margin-bottom: 20px;
}
.footer-content {
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
    padding: 0 40px;
}
.footer-left {
    font-weight: bold;
    color: white;
}
.footer-right a {
    color: #cccccc;
    text-decoration: none;
    margin: 0 8px;
}
.footer-right a:hover {
    color: white;
}
@media (max-width: 768px) {
    .footer-content {
        flex-direction: column;
        align-items: center;
    }
    .footer-right {
        margin-top: 10px;
    }
}
</style>

<div class="footer-line"></div>

<div class="footer-container">
    <div class="footer-content">
        <div class="footer-left">
            © 2025 Atharva Chaphe. All rights reserved.
        </div>
        <div class="footer-right">
            <a href="#">English</a> |
            <a href="#">TOU</a> |
            <a href="#">Privacy</a> |
            <a href="#">Community</a> |
            <a href="#">Cookie Preferences</a> |
            <a href="#">Do not sell or share my personal information</a>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)