import streamlit as st
import random
import json

# Load events
with open("events.json", "r") as f:
    events = json.load(f)

# Pick one event for the session
if "target" not in st.session_state:
    event = random.choice(events)
    st.session_state.target = event
    st.session_state.attempts = 0
    st.session_state.message = ""

event = st.session_state.target

st.title("My boyfriend guesses years")
st.subheader(f"What year did this happen?")
st.markdown(f"**🗓️ {event['event']}**")

guess = st.number_input("Your guess (year):", min_value=0, max_value=2100, step=1)
if st.button("Submit"):
    st.session_state.attempts += 1
    if guess < event["year"]:
        st.session_state.message = "📉 Too early!"
    elif guess > event["year"]:
        st.session_state.message = "📈 Too late!"
    else:
        st.session_state.message = f"✅ Correct! It happened in {event['year']}."
st.write(st.session_state.message)
st.write(f"Attempts: {st.session_state.attempts}")

if st.button("🔄 New event"):
    st.session_state.target = random.choice(events)
    st.session_state.attempts = 0
    st.session_state.message = ""
