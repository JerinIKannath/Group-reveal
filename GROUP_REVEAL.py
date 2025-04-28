import streamlit as st
st.set_page_config(page_title="Group Reveal ✨", page_icon="🪄")
import base64
import pandas as pd
import time
def set_background(image_file):
    with open(image_file, "rb") as img_file:
        encoded_string = base64.b64encode(img_file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: 
                linear-gradient(rgba(255, 255, 255, 0.75), rgba(255, 255, 255, 0.75)), 
                url("data:image/png;base64,{encoded_string}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
            font-weight: bold;
        }}
        .css-10trblm, .css-1d391kg, .st-bv, .st-c9, .st-co, .st-emotion-cache-1c7y2kd {{
            font-weight: bold !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Call it early in your script
set_background("logo.png")
# Load the name-group mapping file
@st.cache_data
def load_data():
    return pd.read_csv("group_data.csv")

df = load_data()

from PIL import Image
# Load the logo

mystery=Image.open("mystery.png")
# UI

# UI
st.title("🔍 Discover Your Group")
st.write("The Supreme Leader has allocated you to group. Enter your name to reveal your group!")

name_input = st.text_input("Your Name")

if name_input:
    found = False
    for team in df.columns:
        team_members = df[team].dropna().astype(str).str.strip().str.lower()
        if name_input.strip().lower() in team_members.values:
            placeholder = st.empty()
            placeholder.markdown("<h2 style='text-align: center; color: purple;'>🔮 Unveiling your destiny...</h2>", unsafe_allow_html=True)
            time.sleep(2)
            placeholder.empty()
            st.success(f"🎉 You are in: **{team}**")
            st.snow() 
            st.image(mystery, width=200)
            found = True
            break
    if not found:
        st.error("😕 Name not found in any team.")
