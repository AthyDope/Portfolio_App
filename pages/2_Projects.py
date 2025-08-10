import streamlit as st
import pandas

# Inject custom CSS for responsiveness
st.markdown("""
    <style>
    /* Make images responsive */
    img {
        max-width: 100%;
        height: auto;
    }

    /* Make text wrap nicely */
    h1, h2, h3, p {
        word-wrap: break-word;
    }

    /* Adjust padding and margin for mobile */
    .block-container {
        padding: 1rem;
    }

    /* Buttons full width on mobile */
    @media only screen and (max-width: 768px) {
        .stButton>button {
            width: 100%;
        }
        .stTextInput>div>div>input {
            width: 100%;
        }
    }
    </style>
""", unsafe_allow_html=True)


st.markdown("# **Projects**")
st.markdown("---")

# st.set_page_config(layout="wide")

# Read project data
df = pandas.read_csv("data.csv", sep=",", encoding='latin1')

# Create one centered column
col, = st.columns([1])  # Single column in the layout

with col:
    for index, row in df.iterrows():
        st.header(row["Title"])
        st.write(row["Description"])
        st.write("🖼️ Screenshot:")
        st.image("images/" + row["Image"])
        st.write("🎥 Project Demo:")
        st.video("videos/" + row["Video"], width=1500)
        st.write(f"[🔗 Source Code]({row['URL']})")
        st.markdown("---")  # horizontal line for separation

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
