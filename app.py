import streamlit as st
import numpy as np
import pickle

# Load your trained model (update file name if needed)
model = pickle.load(open("model.pkl", "rb"))

st.title("AQI Prediction Web App")

pm25 = st.slider("PM2.5", 0, 500, 50)
pm10 = st.slider("PM10", 0, 500, 50)
no2 = st.slider("NO2", 0, 200, 20)
so2 = st.slider("SO2", 0, 200, 10)
co = st.slider("CO", 0.0, 10.0, 1.0)
o3 = st.slider("O3", 0, 200, 30)
temp = st.slider("Temperature (°C)", -10, 50, 25)
humidity = st.slider("Humidity (%)", 0, 100, 50)
wind = st.slider("Wind Speed (m/s)", 0, 20, 2)

if st.button("Predict AQI"):
    data = np.array([[pm25, pm10, no2, so2, co, o3, temp, humidity, wind]])
    result = model.predict(data)[0][0]

    st.success(f"Predicted AQI: {result:.2f}")

