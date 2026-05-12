import streamlit as st

# Page Config
st.set_page_config(page_title="The Baseline Protocol", page_icon="⚖️")

# Header section
st.title("The Baseline Protocol ⚖️")
st.write("Welcome. This is a space for genuine connection and shared values. Let's see if our baselines align.")

st.divider()

# Section 1: Lifestyle
st.header("Discipline & Lifestyle")
gym = st.text_area("How do you challenge yourself physically? (Weight training, running, etc.)")
cooking = st.select_slider(
    "How often do you cook from scratch?",
    options=["Rarely/Never", "On weekends", "Most nights", "Every day"]
)

st.divider()

# Section 2: Mindset
st.header("Strategy & Mindset")
st.write("In high-pressure situations, how do you make decisions?")
logic = st.radio(
    "Primary approach:",
    ["I trust my gut and read the room.", 
     "I look at the data and logic first.", 
     "A calculated balance of both."]
)
strategy_detail = st.text_area("Why does that approach work for you?")

st.divider()

# Section 3: Authenticity
st.header("Authenticity Audit")
humility = st.text_area("What is something you’ve failed at recently that taught you something valuable?")

# Submission
if st.button("Submit for Review"):
    if not gym or not strategy_detail or not humility:
        st.warning("Please fill out all fields—depth matters.")
    else:
        st.balloons()
        st.success("Responses submitted. Thank you for your honesty.")
        
