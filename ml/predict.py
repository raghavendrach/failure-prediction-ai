import numpy as np
import joblib
import tensorflow as tf

model = tf.keras.models.load_model('../model/failure_prediction_model.h5')
scalar = joblib.load('scaler.pkl')

sample = np.array([[70, 220, 30]])

sample = scalar.transform(sample)

print("Predicted failure probability:", model.predict(sample)[0][0])

