import streamlit as st
import requests

st.set_page_config(page_title="California Housing Predictor", layout="centered")

st.title("🏠 California Housing Price Predictor")

st.markdown("Enter the house features below and get the predicted price:")

# User input sliders / fields
MedInc = st.number_input("Median Income (MedInc)", value=8.3252)
HouseAge = st.number_input("House Age", value=41)
AveRooms = st.number_input("Average Rooms (AveRooms)", value=6.9841)
AveBedrms = st.number_input("Average Bedrooms (AveBedrms)", value=1.0238)
Population = st.number_input("Population", value=322)
AveOccup = st.number_input("Average Occupancy (AveOccup)", value=2.5556)
Latitude = st.number_input("Latitude", value=37.88)
Longitude = st.number_input("Longitude", value=-122.23)

# When button is clicked
if st.button("Predict Price"):
    data = {
        "MedInc": MedInc,
        "HouseAge": HouseAge,
        "AveRooms": AveRooms,
        "AveBedrms": AveBedrms,
        "Population": Population,
        "AveOccup": AveOccup,
        "Latitude": Latitude,
        "Longitude": Longitude
    }
    
    try:
        # Call FastAPI predict endpoint
        response = requests.post("http://127.0.0.1:8000/predict", json=data)
        prediction = response.json()["prediction"]
        st.success(f"🏡 Predicted Price: {prediction:.2f}")
    except Exception as e:
        st.error(f"Error: {e}")
