import streamlit as st
st.set_page_config(page_title="Group Reveal ✨", page_icon="🪄")
import base64
import pandas as pd
import time
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

logo=Image.open("logo.png")

st.image(logo, width=200)
# UI
st.title("🔍 Discover Your Group")
st.write("The Supreme Leader has choosen you a path. Enter your name to reveal your destiny!")

name_input = st.text_input("Your Name")

if name_input:
    found = False
    for team in df.columns:
        team_members = df[team].dropna().astype(str).str.strip().str.lower()
        if name_input.strip().lower() in team_members.values:
            # Step 1: Show "Unveiling..." message
            placeholder = st.empty()
            placeholder.markdown("<h2 style='text-align: center; color: red;'> Unveiling your destiny...</h2>", unsafe_allow_html=True)
            time.sleep(2)
            placeholder.empty()
            
            # Step 2: Show Lightning GIF
            lightning_placeholder = st.empty()
            lightning_placeholder.image(
                "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExaHdkc2l4empma2pzZWRnbTlxNXM1MGc4NWtsempxbzZwY2ZpY2ZhciZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/fqVodOPZg9uBYvYjes/giphy.gif",
                width=450
            )

            # Play Thunder Sound
            audio_placeholder = st.empty()
            audio_placeholder.audio(thunder_sound, autoplay=True)

            time.sleep(2)
            lightning_placeholder.empty()
            audio_placeholder.empty()
            
            # Step 3: Show the final success message
            st.success(f"🎉 You are in: **{team}**")
            
            found = True
            break
    if not found:
        st.error("😕 Name not found in any team.")

