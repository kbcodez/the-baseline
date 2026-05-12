import streamlit as st

# Page Config for a cleaner look
st.set_page_config(page_title="The Baseline Protocol", page_icon="⚖️")

# Custom CSS for a more "inviting" feel
st.markdown("""
    <style>
    .main { background-color: #fdfcfb; }
    h1 { color: #2c3e50; font-family: 'Helvetica Neue', sans-serif; }
    </style>
    """, unsafe_input=True)

st.title("The Baseline Protocol ⚖️")
st.write("Welcome. This is a space for genuine connection and shared values. Let's see if our baselines align.")

with st.container():
    st.subheader("Discipline & Lifestyle")
    gym = st.text_area("Tell me about your relationship with physical grit. How do you challenge yourself physically?")
    cooking = st.select_slider(
        "How often do you cook from scratch?",
        options=["Rarely/Never", "On weekends", "Most nights", "It's my therapy"]
    )

st.divider()

with st.container():
    st.subheader("Strategy & Mindset")
    st.write("In high-pressure situations, how do you make decisions?")
    logic = st.radio(
        "Choose your primary approach:",
        ["I trust my gut and read the room.", 
         "I look at the data and logic first.", 
         "A calculated balance of both."]
    )
    strategy_detail = st.text_area("Why does that approach work for you?")

st.divider()

with st.container():
    st.subheader("The Authenticity Check")
    humility = st.text_area("What is something you’ve failed at recently that taught you something valuable?")

if st.button("Submit for Review"):
    if not gym or not strategy_detail or not humility:
        st.warning("Please fill out all fields—depth matters.")
    else:
        st.balloons()
        st.success("Thank you for your honesty. Your responses have been sent for assessment.")
        
