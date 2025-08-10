import streamlit as st

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
            margin-top: 34px;
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
        <a href="/?page=Home" target="_self" class="{ 'active' if page == 'Home' else '' }">Home</a>
        <a href="/?page=1_About_Me" target="_self" class="{ 'active' if page == '1_About_Me' else '' }">About Me</a>
        <a href="/?page=2_Projects" target="_self" class="{ 'active' if page == '2_Projects' else '' }">Projects</a>
        <a href="/?page=4_Tech_stack" target="_self" class="{ 'active' if page == '4_Tech_stack' else '' }">Tech Stack</a>
        <a href="/?page=3_Contact_us" target="_self" class="{ 'active' if page == '3_Contact_us' else '' }">Contact Us</a>
        <a href="/?page=5_BLogs" target="_self" class="{ 'active' if page == '5_Blogs' else '' }">Blogs</a>
    </div>
""", unsafe_allow_html=True)

# --- Render the Selected Page ---
if page == "Home":
    st.title("Welcome to my Portfolio website.")

elif page == "1_About_Me":
    with open("pages/1_About_Me.py", encoding="utf-8") as f:
        exec(f.read(), {"st": st})

elif page == "2_Projects":
    with open("pages/2_Projects.py", encoding="utf-8") as f:
        exec(f.read(), {"st": st})

elif page == "4_Tech_stack":
    with open("pages/4_Tech_stack.py", encoding="utf-8") as f:
        exec(f.read(), {"st": st})

elif page == "3_Contact_us":
    with open("pages/3_Contact_us.py", encoding="utf-8") as f:
        exec(f.read(), {"st": st})

elif page == "5_Blogs":
    with open("pages/5_Blogs.py", encoding="utf-8") as f:
        exec(f.read(), {"st": st})

col1, col2 = st.columns(2)

with col1:
    st.image("images/ChatGPT_Home.png", width=450, output_format="PNG")
    st.markdown(
        """
        <style>
            div[data-testid="stImage"] {
                text-align: left;
                margin-left: 105px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

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