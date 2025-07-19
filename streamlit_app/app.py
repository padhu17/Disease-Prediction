import streamlit as st
import joblib

# Load model and symptom encoder
model = joblib.load("model/best_model.pkl")
mlb = joblib.load("model/mlb.pkl")
all_symptoms = list(mlb.classes_)

# UI layout
st.set_page_config(page_title="Disease Predictor", layout="centered")
st.title("🩺 Disease Prediction App")
st.markdown("Select your symptoms from the list below:")

# Multi-select or checkboxes
selected_symptoms = st.multiselect("Symptoms", all_symptoms)

if st.button("Predict"):
    if len(selected_symptoms) < 1:
        st.warning("Please select at least one symptom.")
    else:
        # Prepare input
        encoded_input = mlb.transform([selected_symptoms])
        prediction = model.predict(encoded_input)[0]
        confidence = max(model.predict_proba(encoded_input)[0])

        # Show result
        st.success(f"### ✅ Predicted Disease: `{prediction}`")
        st.write(f"🔬 **Confidence Score:** `{round(confidence, 4)}`")
