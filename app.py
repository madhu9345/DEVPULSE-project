import streamlit as st
import numpy as np
import pickle

st.set_page_config(page_title="DevPulse", layout="centered")
st.title("🧠 DevPulse - Developer Productivity Assistant")

# Load model
model = pickle.load(open('dev_model.pkl', 'rb'))

st.markdown("#### Simulate your coding behavior 👇")

typing_speed = st.slider("Typing Speed (chars/sec)", 0.0, 10.0, 3.0)
pause_time = st.slider("Max Idle Time (seconds)", 0.0, 30.0, 5.0)
errors = st.slider("Errors per minute", 0, 25, 5)

# Predict
input_data = np.array([[typing_speed, pause_time, errors]])
prediction = model.predict(input_data)[0]

st.markdown(f"### 💡 Productivity Status: **{prediction}**")

if prediction == "Needs Break":
    st.warning("🔔 Suggestion: Take a short break and refresh.")
elif prediction == "Tired":
    st.info("⚠️ Suggestion: Stretch or rest briefly.")
else:
    st.success("✅ You're doing great! Keep going!")
