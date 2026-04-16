## 📸 Project Demo

![App Screenshot](frontend-screenshot.png)

# ⚡ AI-Based Component Failure Prediction System

## 📌 Overview

This project predicts industrial component failure types using an Artificial Neural Network (ANN).
It is built as an end-to-end machine learning system with backend API and frontend UI.

---

## 🚀 Features

* Multi-class failure prediction (0–4 categories)
* Data preprocessing & feature scaling
* ANN model using TensorFlow/Keras
* FastAPI backend for real-time predictions
* Streamlit UI for user interaction

---

## 🧠 Tech Stack

* Python
* TensorFlow / Keras
* Scikit-learn
* FastAPI
* Streamlit

---

## 📂 Project Structure

failure-prediction-ai/
│
├── data/
├── ml/
├── backend/
├── frontend/
├── model/
└── README.md

---

## ▶️ How to Run

### 1. Train Model

cd ml
python train.py

### 2. Run Backend

cd backend
python -m uvicorn main:app --reload

### 3. Run Frontend

cd frontend
streamlit run app.py

---

## 📊 Output

The system predicts the failure type and displays a human-readable label (e.g., Mechanical Failure).

---

## 🎯 Future Improvements

* Improve model accuracy
* Deploy on cloud (Render / Streamlit Cloud)
* Add real-time sensor integration

---

## 👨‍💻 Author

Raghavendra
