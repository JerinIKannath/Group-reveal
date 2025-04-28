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

st.image(logo, width=300)
# UI
st.title("🔍 Discover Your Group")
st.write("The Supreme Leader has choosen you a path. Enter your name to reveal your destiny!")

name_input = st.text_input("Your Name")

if name_input:
    found = False
    for team in df.columns:
        team_members = df[team].dropna().astype(str).str.strip().str.lower()
        if name_input.strip().lower() in team_members.values:
            placeholder = st.empty()
            placeholder.markdown("<h2 style='text-align: center; color: red;'>🔮 Unveiling your destiny...</h2>", unsafe_allow_html=True)
            time.sleep(2)
            placeholder.empty()
            st.success(f"🎉 You are in: **{team}**")
            
            # Replace st.snow() with a lightning GIF
            st.image("https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExaHdkc2l4empma2pzZWRnbTlxNXM1MGc4NWtsempxbzZwY2ZpY2ZhciZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/fqVodOPZg9uBYvYjes/giphy.gif", width=300)

            found = True
            break
    if not found:
        st.error("😕 Name not found in any team.")
