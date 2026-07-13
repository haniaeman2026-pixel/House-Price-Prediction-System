from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import joblib
import os

# =====================================================
# FastAPI Configuration
# =====================================================

app = FastAPI(
    title="House Price Prediction API",
    description="A Machine Learning API built with FastAPI to predict house prices based on house area.",
    version="2.0.0"
)

# =====================================================
# Load Trained Model
# =====================================================

MODEL_PATH = "model/house_price_model.pkl"

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model not found: {MODEL_PATH}")

model = joblib.load(MODEL_PATH)

# =====================================================
# Input Schema
# =====================================================

class HouseInput(BaseModel):
    area: float = Field(
        ...,
        gt=0,
        description="House Area in Square Feet",
        example=1500
    )

# =====================================================
# Root Endpoint
# =====================================================

@app.get("/", tags=["Home"])
def home():
    return {
        "message": "🏡 House Price Prediction API is Running Successfully",
        "developer": "Hania Eman",
        "version": "2.0.0"
    }

# =====================================================
# Health Check
# =====================================================

@app.get("/health", tags=["Health"])
def health():
    return {
        "status": "Healthy",
        "model_loaded": True
    }

# =====================================================
# Prediction Endpoint
# =====================================================

@app.post("/predict", tags=["Prediction"])
def predict(data: HouseInput):
    try:
        prediction = model.predict([[data.area]])

        return {
            "success": True,
            "input": {
                "area": data.area
            },
            "predicted_price": round(float(prediction[0]), 2),
            "currency": "PKR"
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Prediction Failed: {str(e)}"
        )