import streamlit as st 
import joblib


model=joblib.load('model.joblib')

st.title("NEWS CATEGORY PREDICTION")
st.markdown('#### enter news below')
input_text =st.text_area(
    label="",max_chars=1000,height=300
)

if st.button("predict Category "):
    prediction=model.predict([input_text])[0]
    st.success(f"Predicted category is {prediction}")