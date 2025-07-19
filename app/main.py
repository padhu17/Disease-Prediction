from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load model and encoder
model = joblib.load("model/best_model.pkl")
mlb = joblib.load("model/mlb.pkl")

app = FastAPI(title="Disease Prediction API")

# Pydantic request body model
class SymptomInput(BaseModel):
    symptoms: list[str]

@app.get("/")
def root():
    return {"message": "Welcome to the Disease Prediction API!"}

@app.get("/symptoms")
def get_symptoms():
    return {"symptoms": list(mlb.classes_)}

@app.post("/predict-disease")
def predict_disease(data: SymptomInput):
    input_symptoms = [sym.lower().strip().replace("_", " ") for sym in data.symptoms]
    
    try:
        encoded = mlb.transform([input_symptoms])
    except ValueError:
        return {"error": "One or more symptoms are not recognized. Use /symptoms to see valid options."}
    
    prediction = model.predict(encoded)[0]
    probabilities = model.predict_proba(encoded)[0]
    confidence = float(np.max(probabilities))

    return {
        "predicted_disease": prediction,
        "confidence_score": round(confidence, 4),
        "input_symptoms": input_symptoms
    }
