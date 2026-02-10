import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Health Disease Risk Predictor", layout="centered")

st.title("🩺 Health Disease Risk Predictor")
st.write("Predict health disease risk based on lifestyle and health indicators.")

# Load model
@st.cache_resource
def load_model():
    return joblib.load("model.pkl")

model = load_model()

st.header("Enter Health Details")

age = st.number_input("Age", min_value=1, max_value=120, value=30)
bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, value=22.0)
bp = st.number_input("Blood Pressure", min_value=50, max_value=200, value=120)
glucose = st.number_input("Glucose Level", min_value=50, max_value=300, value=100)
cholesterol = st.number_input("Cholesterol", min_value=100, max_value=400, value=180)
smoking = st.selectbox("Smoking", ["No", "Yes"])
alcohol = st.selectbox("Alcohol Consumption", ["No", "Yes"])
physical_activity = st.selectbox("Physical Activity", ["Low", "Moderate", "High"])

if st.button("Predict Risk"):
    input_data = pd.DataFrame({
        "age": [age],
        "bmi": [bmi],
        "bp": [bp],
        "glucose": [glucose],
        "cholesterol": [cholesterol],
        "smoking": [1 if smoking == "Yes" else 0],
        "alcohol": [1 if alcohol == "Yes" else 0],
        "physical_activity": [
            0 if physical_activity == "Low" else
            1 if physical_activity == "Moderate" else 2
        ]
    })

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("⚠️ High Disease Risk Detected")
        st.write("Recommendations:")
        st.markdown("""
        - Maintain a balanced diet  
        - Exercise regularly  
        - Avoid smoking & alcohol  
        - Monitor BP, glucose, cholesterol  
        - Consult a doctor  
        """)
    else:
        st.success("✅ Low Disease Risk")
        st.write("Keep maintaining a healthy lifestyle! 💪")
