"""
FastAPI application for serving the zoologist model.
"""
import os

import pandas as pd
from fastapi import FastAPI
from src.zoologist.predict import MODEL_PATH, load_model



# FastAPI instance
app = FastAPI()



# Root endpoint
@app.get("/")
def root():
    """Root endpoint returning a greeting."""
    return {"greeting": "hello"}


# Dummy endpoint
@app.get("/dummy")
def dummy(number: int):
    """Dummy endpoint that returns the square of the input number."""
    return {"result": number ** 2}


@app.get("/predict")
def predict(island:str, bill_length_mm:float, bill_depth_mm:float, flipper_length_mm:float, body_mass_g:float, sex:str):

    model = load_model(MODEL_PATH)

    X_pred = pd.DataFrame([{"island": island,
            "bill_length_mm": bill_length_mm,
            "bill_depth_mm": bill_depth_mm,
            "flipper_length_mm": flipper_length_mm,
            "body_mass_g": body_mass_g,
            "sex": sex}])

    prediction = model.predict(X_pred)


    return {"prediction": str(prediction[0])}
