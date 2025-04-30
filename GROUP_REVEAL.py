import streamlit as st
st.set_page_config(page_title="Group Reveal ✨", page_icon="🪄")
import base64
import pandas as pd
import time
from pathlib import Path
st.markdown(
    """
    <style>
    .stApp {
        background-color: #d9d9d9;
    }
    </style>
    """,
    unsafe_allow_html=True
)
# Load the name-group mapping file
@st.cache_data
def load_data():
    return pd.read_csv("group_data.csv")

df = load_data()

from PIL import Image
# Load the logo

#logo=Image.open("logo1.png")

st.markdown(
    """
    <div style="text-align: center;">
        <img src="data:image/png;base64,{}" width="200">
    </div>
    """.format(base64.b64encode(open("logo1.png", "rb").read()).decode()),
    unsafe_allow_html=True
)
# UI
# st.title("Enter Your Realm!")
# st.write("The Supreme Leader has choosen you a path. Enter your UID to reveal your destiny!")
st.markdown(
    """
    <div style='text-align: center;'>
        <h1 style='color: black;font-size: 24px;'>Step Into Your Realm!</h1>
        <p style='color: black; font-size: 20px;'>The Supreme Leader has chosen you a path. Enter your UID to reveal your destiny!</p>
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <style>
    label {
        color: black !important;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)
name_input = st.text_input("Your UID")

if name_input:
    found = False
    for team in df.columns:
        team_members = df[team].dropna().astype(str).str.strip().str.lower()
        if name_input.strip().lower() in team_members.values:
            # Step 1: Show "Unveiling..." message
            placeholder = st.empty()
            placeholder.markdown("<h2 style='text-align: center; color: black; font-size: 24px;'> Unveiling your destiny...</h2>", unsafe_allow_html=True)
            time.sleep(2)
            placeholder.empty()
            
            # Step 2: Show Lightning GIF
            lightning_placeholder = st.empty()
            lightning_placeholder.image(
                "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExbnJqdWM2ZWx6eWx3eHJuemh3ejB4bDBtcnB1bnBncmowcW9wOXJ5biZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/bVSCpa4IoTH8s/giphy.gif",
                width=300
            )

        

            time.sleep(3)
            lightning_placeholder.empty()
           
            
            # Step 3: Show the final success message
            #st.success(f" You are in: **{team}**")
            st.markdown(
            f"""
            <div style="background-color: #d4edda; padding: 15px; border-radius: 10px; border: 1px solid #c3e6cb;">
                <h3 style="color: black; text-align: center;">🎉 You are in: <strong>{team}</strong></h3>
            </div>
            """,
            unsafe_allow_html=True
            )
            try:
                log_entry = f"{name_input.strip()},{team},{time.strftime('%Y-%m-%d %H:%M:%S')}\n"
                log_file_path = Path("access_log.csv")
                log_file_path.write_text(log_file_path.read_text() + log_entry if log_file_path.exists() else log_entry)
            except Exception as e:
                st.warning("⚠️ Access log failed to write.")
            found = True
            break
    if not found:
        st.error("😕 UID not found in any team.")

