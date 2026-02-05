import streamlit as st
import joblib
import os
# Load trained model
st.title("❤️ Heart Disease Prediction App")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model.joblib")

st.write("📁 Looking for model at:", MODEL_PATH)

if not os.path.exists(MODEL_PATH):
    st.error("❌ model.joblib not found in app directory")
    st.stop()

model = joblib.load(MODEL_PATH)

age = st.number_input("Age", min_value=1, max_value=120)
sex = st.number_input("Sex (1 = Male, 0 = Female)")
cp = st.number_input("Chest Pain Type (0–3)")
trestbps = st.number_input("Resting Blood Pressure")
chol = st.number_input("Serum Cholesterol")
fbs = st.number_input("Fasting Blood Sugar > 120 (1 = Yes, 0 = No)")
restecg = st.number_input("Resting ECG (0–2)")
thalach = st.number_input("Maximum Heart Rate Achieved")
exang = st.number_input("Exercise Induced Angina (1 = Yes, 0 = No)")
oldpeak = st.number_input("ST Depression")
slope = st.number_input("Slope (0–2)")
ca = st.number_input("Number of Major Vessels (0–4)")
thal = st.number_input("Thal (0 = Normal, 1 = Fixed, 2 = Reversible)")

sample = [[
    age, sex, cp, trestbps, chol, fbs,
    restecg, thalach, exang, oldpeak,
    slope, ca, thal
]]

if st.button("Predict"):
    prediction = model.predict(sample)[0]

    if prediction == 1:
        st.error("⚠️ High chance of Heart Disease")
    else:
        st.success("✅ Low chance of Heart Disease")
