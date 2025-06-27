import streamlit as st
import joblib
import numpy as np

# Load your trained model
#model = joblib.load("student_pass_model.pkl")

st.title("Student Exam Success Predictor")

# User input
study_time = st.slider("Study Time (hrs/week)", 0, 20, 5)
absences = st.slider("Number of Absences", 0, 30, 5)
health = st.slider("Health (1 = poor, 5 = excellent)", 1, 5, 3)

# Convert to model input
input_data = np.array([[study_time, absences, health]])
#prediction = model.predict(input_data)[0]

# Display result
#st.write("Prediction:", "✅ Likely to Pass" if prediction else "❌ At Risk of Failing")
