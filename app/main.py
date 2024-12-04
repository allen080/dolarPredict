from fastapi import FastAPI
import numpy as np
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
import pandas as pd

app = FastAPI()

model = load_model("model.pkl")
scaler = MinMaxScaler(feature_range=(0, 1))

@app.get("/")
def read_root():
    return {"message": "API de verificação do valor do Dólar"}

@app.post("/predict/")
def predict(prices: list):
    # pre processamento dos dados
    prices = np.array(prices).reshape(-1, 1)
    scaled_prices = scaler.fit_transform(prices)
    X_input = np.reshape(scaled_prices, (1, len(prices), 1))
    
    # realizando a previsão do valor
    prediction = model.predict(X_input)
    scaled_prediction = scaler.inverse_transform(prediction)
    return {"prediction": float(scaled_prediction[0][0])}
