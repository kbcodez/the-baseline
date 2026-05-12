import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="The Baseline Protocol", page_icon="⚖️")

# Connect to your Google Sheet
conn = st.connection("gsheets", type=GSheetsConnection)

st.title("The Baseline Protocol ⚖️")
st.write("Welcome. This is a logic and lifestyle gate for serious connection.")

st.divider()

# Identification
contact = st.text_input("Twitter/Instagram/Telegram Handle (So I can find you):")

# Section 1: Lifestyle
st.header("Discipline & Lifestyle")
gym = st.text_area("Describe your relationship with physical grit (Weight training, running, etc.):")
cooking = st.select_slider(
    "How often do you cook from scratch?",
    options=["Rarely/Never", "On weekends", "Most nights", "Every day"]
)

st.divider()

# Section 2: Mindset
st.header("Strategy & Mindset")
logic = st.radio(
    "Primary approach to high-stakes decisions:",
    ["Intuition and 'The Room'", "Data and Logic", "A calculated balance"]
)
strategy_detail = st.text_area("Explain your reasoning:")

st.divider()

# Section 3: Authenticity
st.header("Authenticity Audit")
humility = st.text_area("What is something you’ve failed at recently that taught you something valuable?")

if st.button("Submit for AI Vetting"):
    if not contact or not gym or not strategy_detail or not humility:
        st.warning("Incomplete application. Depth is a requirement.")
    else:
        # Create a dataframe for the new entry
        new_data = pd.DataFrame([{
            "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Contact": contact,
            "Grit": gym,
            "Cooking": cooking,
            "Mindset": logic,
            "Strategy_Detail": strategy_detail,
            "Humility": humility
        }])
        
        # Append to the Google Sheet
        existing_data = conn.read(worksheet="Sheet1")
        updated_df = pd.concat([existing_data, new_data], ignore_index=True)
        conn.update(worksheet="Sheet1", data=updated_df)
        
        st.balloons()
        st.success("Your application has been logged. The AI will assess your sincerity.")
        
