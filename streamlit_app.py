import streamlit as st

st.title("The Baseline Protocol")
st.subheader("Official Vetting System")

st.write("---")
st.write("This is a logic and lifestyle gate. Low effort entries will be discarded by AI.")

# Tier 1: Lifestyle
st.header("Phase 1: Lifestyle & Discipline")
cooking = st.selectbox("Your approach to dinner:", ["Ordering out", "Microwave meals", "Cooking from scratch (Mediterranean/High-protein)"])
gym = st.text_area("Describe your physical discipline (weight training, running, etc.):")

# Tier 2: The Logic Check
st.header("Phase 2: Strategy & Influence")
logic_prompt = st.text_area("In a high-stakes environment, do you rely on GTO-based math or psychological intuition? Explain.")

# Tier 3: The Authenticity Audit
st.header("Phase 3: Humility Check")
humility = st.text_area("What is something you are genuinely humble about? No 'boss' talk allowed.")

if st.button("Submit for AI Assessment"):
    if not gym or not logic_prompt or not humility:
        st.error("Incomplete data. Discipline required.")
    else:
        st.success("Analysis in progress. Results will be reported to the administrator.")
      
