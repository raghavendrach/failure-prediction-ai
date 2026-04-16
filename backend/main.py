from fastapi import FastAPI
import numpy as np
import joblib
import tensorflow as tf

app = FastAPI()

model = tf.keras.models.load_model('../model/failure_prediction_model.h5')
scaler = joblib.load('../ml/scaler.pkl')
label_mapping = joblib.load('../model/label_mapping.pkl')

@app.post("/")
def home():
    return {"message": "Welcome to the Component Failure Prediction API!"}

@app.post("/predict/")
def predict(data: dict):
    values = list(data.values())
    arr = np.array(values).reshape(1, -1)

    arr = scaler.transform(arr)

    prediction = model.predict(arr)
    predicted_class = int(np.argmax(prediction))
    predicted_label = label_mapping[predicted_class]


    return {"predicted_failure_type": predicted_class,"label": predicted_label}