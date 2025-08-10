import streamlit as st

st.set_page_config(
    page_title="Blogs | Atharva Chaphe",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="auto"
)

# Now your code starts below
st.title("📝 My Blogs")
st.write("Welcome to my blog section! Here I share my thoughts, tutorials, and experiences.")


st.markdown("---")

# --- SAMPLE BLOG DATA ---
blogs = [
    {
        "title": "Getting Started with Python: A Beginner’s Guide",
        "description": "This guide introduces Python, explains how to set up the environment, and walks you through writing your first program while covering key beginner topics such as syntax, variables, and basic operations.",
        "link": "https://yourbloglink1.com"
    },
    {
        "title": "Understanding Classes and Objects in Python",
        "description": "Learn the fundamentals of classes and objects in Python, how to define them, and how they form the building blocks of object-oriented programming.",
        "link": "https://yourbloglink2.com"
    },
    {
        "title": "5 Tips to Improve Your Coding Skills",
        "description": "Here are 5 simple and practical tips to become a better programmer.",
        "link": "https://yourbloglink3.com"
    },
    {
        "title": "My Journey: From Beginner to Full-Stack Developer",
        "description": "A personal story about how I transitioned into full-stack development.",
        "link": "https://yourbloglink4.com"
    }
]

# --- DISPLAY BLOG CARDS ---
for blog in blogs:
    st.markdown(f"### [{blog['title']}]({blog['link']})", unsafe_allow_html=True)
    st.markdown(f"{blog['description']}")
    st.markdown(f"[Read more →]({blog['link']})")
    st.markdown("---")

# --- FOOTER (HIDE STREAMLIT FOOTER) ---
hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

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
