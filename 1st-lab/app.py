import streamlit as st
import joblib

# Load the model
model = joblib.load('model.joblib')

st.title("Iris Flower Classifier🌻")

SepalLengthCm = st.number_input("Enter Sepal Length")
SepalWidthCm = st.number_input("Enter Sepal Width")
PetalLengthCm = st.number_input("Enter Petal Length")
PetalWidthCm = st.number_input("Enter Petal Width")


sample = [[SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm]]

if st.button("Predict"):
    answer = model.predict(sample)[0]
    st.success(f"Predicted species is {answer}")