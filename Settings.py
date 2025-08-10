import streamlit as st

# Initialize session state for settings
if "theme" not in st.session_state:
    st.session_state.theme = "light"

if "accent_color" not in st.session_state:
    st.session_state.accent_color = "#007bff"  # Default blue

if "font_style" not in st.session_state:
    st.session_state.font_style = "Sans-serif"

if "language" not in st.session_state:
    st.session_state.language = "English"

# Title
st.title("⚙️ Settings")
st.markdown("---")

# --- Theme Toggle ---
st.subheader("🎨 Theme")
dark_mode = st.checkbox("🌙 Enable Dark Mode", value=st.session_state.theme == "dark")
if dark_mode:
    st.session_state.theme = "dark"
else:
    st.session_state.theme = "light"
st.markdown("---")

# --- Accent Color Picker ---
st.subheader("🌈 Accent Color")
accent_color = st.color_picker("Pick your favorite accent color", st.session_state.accent_color)
st.session_state.accent_color = accent_color
st.markdown("---")

# --- Font Style Selector ---
st.subheader("🔤 Font Style")
font_style = st.selectbox("Choose a font style", ["Sans-serif", "Serif", "Monospace"])
st.session_state.font_style = font_style
st.markdown("---")

# --- Language Selector ---
st.subheader("🌍 Language")
language = st.selectbox("Select language", ["English", "Hindi", "Marathi"])
st.session_state.language = language
st.markdown("---")


# --- Reset Button ---
if st.button("🔄 Reset to Default Settings"):
    st.session_state.theme = "light"
    st.session_state.accent_color = "#007bff"
    st.session_state.font_style = "Sans-serif"
    st.session_state.language = "English"
    st.success("Settings reset to default!")

if st.session_state.theme == "dark":
    st.markdown(
        """
        <style>
            body {
                background-color: #1e1e1e;
                color: white;
            }
            .stApp {
                background-color: #1e1e1e;
                color: white;
            }
            .css-18ni7ap.e8zbici2 {
                background-color: #1e1e1e;  /* Main content background */
            }
            .stButton>button {
                background-color: #444;
                color: white;
            }
            .stTextInput>div>div>input, .stSelectbox>div>div, .stCheckbox>div>div {
                background-color: #333;
                color: white;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
else:
    st.markdown(
        """
        <style>
            body {
                background-color: white;
                color: black;
            }
            .stApp {
                background-color: white;
                color: black;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

st.markdown(
    f"""
    <style>
        body {{
            background-color: {theme_bg};
            color: {theme_color};
            font-family: {st.session_state.font_style};
        }}
        .stButton button {{
            background-color: {st.session_state.accent_color};
            color: white;
            border-radius: 5px;
            font-weight: bold;
        }}
        .stSelectbox div, .stCheckbox div {{
            font-family: {st.session_state.font_style};
        }}
    </style>
    """,
    unsafe_allow_html=True
)


# Display current settings summary
st.markdown("---")
st.subheader("📋 Current Settings")
st.write(f"**Theme:** {st.session_state.theme.capitalize()}")
st.write(f"**Accent Color:** {st.session_state.accent_color}")
st.write(f"**Font Style:** {st.session_state.font_style}")
st.write(f"**Language:** {st.session_state.language}")
st.markdown("---")

