from fastapi import FastAPI
from .schemas import HouseFeatures
import joblib
import numpy as np
import pandas as pd

app = FastAPI()

# Load the trained model
model = joblib.load("models/model.pkl")


@app.get("/")
def root():
    return {"message": "California Housing API is running!"}

@app.post("/predict")
def predict(features: HouseFeatures):
    data = pd.DataFrame([features.dict().values()], columns=features.dict().keys())
    prediction = model.predict(data)[0]
    return {"prediction": float(prediction)}
