import streamlit as st
import random
import json

with open("events.json", "r") as f:
    events = json.load(f)

# Pick one event for the session
if "target" not in st.session_state:
    event = random.choice(events)
    st.session_state.target = event
    st.session_state.attempts = 0
    st.session_state.message = ""
    st.session_state.score = 0

event = st.session_state.target

st.title("My boyfriend guesses years")
st.subheader(f"guess.")
st.markdown(f"**{event['event']}**")

   """if st.session_state.attempts == 6:
            st.session_state.message = f"Boo loser. It was {event["year"]}."
            st.session_state.target = random.choice(events)
            st.session_state.attempts = 0
            st.session_state.score -= 1
            st.session_state.message = ""
"""

guess = st.number_input("Your guess (year):", min_value=0, max_value=2100, step=1)
if st.button("Submit"):
    st.session_state.attempts += 1
    if guess != event["year"]:
        gap = abs(event["year"] - guess)
        if gap > 200:
            st.session_state.message = "200+ years off."
        elif gap > 40:
            st.session_state.message = "41-200 years off."
        elif gap > 10:
            st.session_state.message = "11-40 years off."
        elif gap > 2:
            st.session_state.message = "3-10 years off."
        else:
            st.session_state.message = "1-2 years off."
    else:
        st.session_state.message = "Nice. You get 2 points for being cute."
        st.session_state.score += 2

st.write(st.session_state.message)
st.write(f"Attempts: {st.session_state.attempts}")

if st.button("Skip(but I will deduct one point)"):
    st.session_state.target = random.choice(events)
    st.session_state.attempts = 0
    st.session_state.score -= 1
    st.session_state.message = ""
