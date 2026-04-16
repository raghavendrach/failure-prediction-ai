import streamlit as st
import requests

st.title("Component Failure Prediction System")

inputs = {
    "Generator_bearing_temperature": st.number_input("Generator Bearing Temperature"),
    "Gear_oil_temperature": st.number_input("Gear Oil Temperature"),
    "Ambient_temperature": st.number_input("Ambient Temperature"),
    "Rotor_Speed": st.number_input("Rotor Speed"),
    "Nacelle_temperature": st.number_input("Nacelle Temperature"),
    "Bearing_temperature": st.number_input("Bearing Temperature"),
    "Generator_speed": st.number_input("Generator Speed"),
    "Yaw_angle": st.number_input("Yaw Angle"),
    "Wind_direction": st.number_input("Wind Direction"),
    "Wheel_hub_temperature": st.number_input("Wheel Hub Temperature"),
    "Gear_box_inlet_temperature": st.number_input("Gear Box Inlet Temperature"),
    "f12": st.number_input("Extra Feature 12"),
    "f13": st.number_input("Extra Feature 13"),
    "f14": st.number_input("Extra Feature 14")
}


if st.button("Predict"):
    response = requests.post("http://localhost:8000/predict/", json=inputs)

    result = response.json()
    
    st.success(f"Failure Type: {result['label']}")