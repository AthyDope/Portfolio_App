import streamlit as st

st.set_page_config(layout="wide")

params = st.query_params
page = params.get("page", "Home")

# --- Navigation Bar ---
st.markdown(f"""
    <style>
        .topnav {{
            background-color: #1f1f2e;
            overflow: hidden;
            display: flex;
            justify-content: center;
            padding: 12px 0;
            border-bottom: 2px solid #444;
        }}
        .topnav a {{
            color: white;
            text-align: center;
            padding: 12px 20px;
            text-decoration: none;
            font-size: 17px;
            font-weight: 500;
        }}
        .topnav a:hover {{
            background-color: #575757;
            color: white;
        }}
        .topnav a.active {{
            background-color: #007bff;
            color: white;
            border-radius: 5px;
        }}
    </style>

    <div class="topnav">
        <a href="/?page=Home" class="{ 'active' if page == 'Home' else '' }">Home</a>
        <a href="/?page=About" class="{ 'active' if page == 'About' else '' }">About Me</a>
        <a href="/?page=Projects" class="{ 'active' if page == 'Projects' else '' }">Projects</a>
        <a href="/?page=Tech" class="{ 'active' if page == 'Tech' else '' }">Tech Stack</a>
        <a href="/?page=Contact" class="{ 'active' if page == 'Contact' else '' }">Contact Us</a>
    </div>
""", unsafe_allow_html=True)

# --- Render the Selected Page ---
if page == "Home":
    st.title("Welcome to my Portfolio website.")
    # st.write("")
    # Your home page content goes here

elif page == "About":
    with open("pages/About_Me.py", encoding="utf-8") as f:
        exec(f.read(), {"st": st})

elif page == "Projects":
    with open("pages/Projects.py", encoding="utf-8") as f:
        exec(f.read(), {"st": st})

elif page == "Tech":
    with open("pages/Tech_stack.py", encoding="utf-8") as f:
        exec(f.read(), {"st": st})

elif page == "Contact":
    with open("pages/Contact_us.py", encoding="utf-8") as f:
        exec(f.read(), {"st": st})

col1, col2 = st.columns(2)

with col1:
    # st.markdown("<br>", unsafe_allow_html=True)
    st.image("images/ChatGPT_Home.png", width=450)

with col2:
    st.title("Atharva Chaphe")
    content = ("Hi, I am Atharva Chaphe! I am a Python Developer.\n\n"
               "I graduated in June 2024 with a Bachelor's degree in Computer Science and an honor's degree in Data Science and Visualisation from Pune University.\n\n"
               "I scored had an overall CGPA of 8.48 on the scale of 10.\n\n"
               "I have completed several course certifications in C Programming , CPP, Python and MySQL.\n\n"
               "I completed two interships\n\n"
               " - Anikaay Integration as a junior Data Analyst.\n\n"
               " - Techview Web Solutions Pvt. Ltd. as a Trainee Web Developer.\n\n"
               "Social Work\n\n"
               " - Member (Karyakarta) at Shrimant Dagdushet Halwai Ganpati\n\n"
               " - Volunteer at NavUmmed Foundation\n\n"
               "Aspiring for higher education through a master’s.\n\n")
    st.info(content)

col3, col4 = st.columns([1, 1])  # Adjust width ratios as needed

with col3:
    st.markdown("<div style='text-align: center;margin-top: 10px;'>Click to check out my resume:</div>", unsafe_allow_html=True)

with col4:
    with open("CV_Atharva_Chaphe_Final.pdf", "rb") as file:
        resume_data = file.read()
    st.download_button(
        label="⬇️ Download Resume",
        data=resume_data,
        file_name="CV_Atharva_Chaphe_Final.pdf",
        mime="application/pdf",
        help="Click to download my latest resume.",
    )
st.markdown(" ")
st.markdown(" ")
content2 = "Welcome to my portfolio website. Feel free to connect with me for any queries or collaborations."
st.write(content2)

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