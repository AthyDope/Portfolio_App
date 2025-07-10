import streamlit as st
from PIL import Image

# Set wide layout
st.set_page_config(layout="wide")

# Load profile image
image = Image.open("images/photo.png")  # Replace with your image file

with st.container():
    col1, col2 = st.columns([1, 1])

    with col1:
        left_space, center, right_space = st.columns([1, 2, 1])
        with center:
            st.image(image, width=200)

    with col2:
        st.markdown("# **Atharva**  **Chaphe**")
        st.markdown("##### Python Full Stack Developer \n #### Data Analyst")

st.markdown("---")
st.markdown("### 🎓 Education")
st.markdown("""
- **Bachelor of Engineering in Computer Science with an Honors degree in Data Science And Visualization**
    - **University**: Savitribai Phule Pune University  
    - **CGPA**: 8.48/10  with zero backlogs <br> <br>
    
- **Higher Secondary Education (12th Grade)**  
    - **Board**: Maharashtra State Board  
    - **Stream**: Science  
    - **Score**: 66%  <br> <br>
    
- **Secondary School Education (10th Grade)**  
    - **Board**: Maharashtra State Board  
    - **School**: St. Vincents High School  
    - **Score**: 78%  
    """, unsafe_allow_html=True)

st.markdown("---")
st.markdown("### 💼 Experience / Internships")
st.markdown("""
- **Trainee Data Analyst**
    - **Company**: Anikaay Integration
    - **Skills Implemented**: Tableau/Power BI and tools like SQL/Excel/Python. 
    - **Responsibilities**: Developed a dashboard to analyze restaurants data for identifying popular cuisines and customer preferences.<br> <br>

- **Trainee Web Developer**  
    - **Company**: Techview Web Solutions Pvt. Ltd.  
    - **Skills Implemented**: PHP, ReactJS, NodeJs, HTML, JQuery and MySQL.  
    - **Responsibilites**: Developed a secured employee portal for attendance regularization and document management   <br> <br>  
    """, unsafe_allow_html=True)
st.markdown("---")

st.markdown("### 📜 Research Papers")
st.markdown("""
- Presented Technical paper on **“Digital Virtual Business Card Using NFC Tag”** during final year of Engineering
at the **International Conference on Smart Innovation for Society (ICSIS) (2024)**. The paper focused on
integrating NFC tags with digital QR code within PVC Business cards and enabled seamless contact sharing. <br><br>
    """, unsafe_allow_html=True)
st.markdown("---")

st.markdown("### 📜 Certifications")
st.markdown("""
- **Python Full Stack Development** - Oytie Training Institution 
- **Data Analyst** - One Road Map
- **Generative AI** - Ineuron
- **C Programming** - Udemy
- **C++** - Scalar <br><br>
    """, unsafe_allow_html=True)
st.markdown("---")

st.markdown("### 📌 Volunteering / Extracurricular Activities")
st.markdown("""
- 🛕 **Member (Karyakarta) – Shrimant Dagdushet Halwai Ganpati Trust, Pune**
  - Assisting with temple acitivites,managing crowd flow during peak hours.
  - Helping organize religious events and community. <br><br>

- 📅 **Event Cordinator – College Cultural Fest (Sparktech)**
  - Hosted multiple events with an audience of 300+ students.
  - Organized cultural and sports events, which fostered communication, critical thinking.   <br><br>

- 🧩 **Volunteer - Nav Umeed Foundation (NGO)**
  - Participated in campaigns for food donation and medical material distribution during covid times.
  - Promoted sense of social responsibility and cleanliness.  <br><br>

- 🎯 **Sports & Fitness Enthusiast**
  - Represented college in inter-departmental and inter-college cricket and football tournaments.
  - Actively maintain a fitness routine, gym discipline, leadership and teamwork.   <br><br>
    """, unsafe_allow_html=True)
st.markdown("---")

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