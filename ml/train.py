import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.utils.class_weight import compute_class_weight
import tensorflow as tf
import joblib
import os

df = pd.read_excel('../data/component_failure.xlsx')

df['Failure_Type'] = df['Failure_Type'].astype('category')

label_mapping = dict(enumerate(df['Failure_Type'].cat.categories))
joblib.dump(label_mapping, '../model/label_mapping.pkl')

df['Failure_Type'] = df['Failure_Type'].cat.codes

df = df.select_dtypes(include=['number'])

X = df.drop('Failure_Type', axis=1)
y = df['Failure_Type']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

joblib.dump(scaler, 'scaler.pkl')

num_classes = df['Failure_Type'].nunique()

num_classes = df['Failure_Type'].nunique()

model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dropout(0.3),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dropout(0.3),
    tf.keras.layers.Dense(num_classes, activation='softmax')
])

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

class_weights = compute_class_weight(
    class_weight='balanced',
    classes=np.unique(y_train),
    y=y_train
)

class_weights = dict(enumerate(class_weights))

model.fit(
    X_train, y_train,
    epochs=20,
    batch_size=32,
    class_weight=class_weights
)

os.makedirs('../model', exist_ok=True)
model.save('../model/failure_prediction_model.h5')

print(df['Failure_Type'].nunique())
print(X.shape)
print("Model trained and saved successfully.")