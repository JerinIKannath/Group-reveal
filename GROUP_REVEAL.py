import streamlit as st
st.set_page_config(page_title="Group Reveal ✨", page_icon="🪄")

import pandas as pd

# Load the name-group mapping file
@st.cache_data
def load_data():
    return pd.read_csv("group_data.csv")

df = load_data()

from PIL import Image
# Load the logo
logo = Image.open("logo.png")  # Make sure logo.png is in the same folder
mystery=Image.open("mystery.png")
# UI
st.image(logo, width=200)  # Adjust width if needed
# UI
st.title("🔮 Discover Your Group")
st.write("The Supreme Leader has allocated you to group. Enter your name to reveal your group!")

name_input = st.text_input("Your Name")

if name_input:
    found = False
    for team in df.columns:
        team_members = df[team].dropna().astype(str).str.strip().str.lower()
        if name_input.strip().lower() in team_members.values:
            st.success(f"🎉 You are in: **{team}**")
            st.snow() 
            st.image(mystery, width=200)
            found = True
            break
    if not found:
        st.error("😕 Name not found in any team.")
