import streamlit as st

st.set_page_config(page_title="Tat Helper", page_icon="🎮", layout="centered")

st.title("Tat Helper")
st.caption("Girl, what the fuck do you want?")

# Remember choices between clicks
if "step" not in st.session_state:
    st.session_state.step = 1
if "prefs" not in st.session_state:
    st.session_state.prefs = {}

def choose(key, value):
    st.session_state.prefs[key] = value
    st.session_state.step += 1

def reset():
    st.session_state.step = 1
    st.session_state.prefs = {}

# STEP 1: Food
if st.session_state.step == 1:
    st.subheader("Food vibe?")
    c1, c2, c3 = st.columns(3)
    if c1.button("🍲 Eat in"):
        choose("food", "eat_in")
    if c2.button("🛍️ Eat out"):
        choose("food", "eat_out")
    if c3.button("🤷 Either"):
        choose("food", "either")

# STEP 2: Energy
elif st.session_state.step == 2:
    st.subheader("Energy level?")
    c1, c2, c3 = st.columns(3)
    if c1.button("🐢 Low"):
        choose("energy", "low")
    if c2.button("🙂 Medium"):
        choose("energy", "medium")
    if c3.button("🔥 High"):
        choose("energy", "high")

# STEP 3: Results (for now)
else:
    st.subheader("✅ Choices so far")
    st.write(st.session_state.prefs)

    col1, col2 = st.columns(2)
    if col1.button("🔁 Restart"):
        reset()
    if col2.button("⬅️ Back one step"):
        st.session_state.step = max(1, st.session_state.step - 1)

