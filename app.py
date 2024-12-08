import streamlit as st
import joblib
import pandas as pd

# Load the pre-trained model
model = joblib.load('misery_index_model.pkl')

# Function to make predictions
def predict_misery_index(inputs):
    # Convert input into a DataFrame to match the model's input shape
    input_data = pd.DataFrame([inputs], columns=[
        'unemployment', 'inflation', 'temp', 'wind_speed', 'humidity', 
        'cloud_cover', 'precip', 'ocean_heat', 'co2', 'ocean_ph', 
        'sea_level', 'glacier_mass', 'arctic_ice', 'antarctic_ice'
    ])
    
    # Perform the prediction
    prediction = model.predict(input_data)
    return prediction[0]

# Function to categorize the Misery Index
def categorize_misery_index(misery_index):
    if misery_index <= 10:
        return "Low Misery Index (Stable)"
    elif misery_index <= 20:
        return "Moderate Misery Index (Some Distress)"
    else:
        return "High Misery Index (High Distress)"

# Title of the app
st.title("Misery Index Prediction")

# Explanation of the app
st.markdown("""
This app predicts the **Misery Index** based on various climatic factors. Please input the following values:
""")

# Create three columns for the input fields
col1, col2, col3 = st.columns(3)

# Input fields for the user to enter values (without max_value restrictions)
with col1:
    unemployment_rate = st.number_input("Unemployment Rate (%)", min_value=0.0, value=10.0)
    inflation_rate = st.number_input("Inflation Rate (%)", min_value=0.0, value=10.0)
    avg_temp = st.number_input("Average Temperature (°C)", min_value=-50.0, value=25.0)
    avg_wind_speed = st.number_input("Average Wind Speed (m/s)", min_value=0.0, value=5.0)
    cloud_cover = st.number_input("Cloud Cover (%)", min_value=0.0, value=50.0)

with col2:
    avg_humidity = st.number_input("Average Humidity (%)", min_value=0.0, value=60.0)
    precipitation = st.number_input("Precipitation (mm)", min_value=0.0, value=50.0)
    ocean_heat = st.number_input("Ocean Heat Content (10²² J)", min_value=0.0, value=200.0)
    co2 = st.number_input("Atmospheric CO₂ (ppm)", min_value=0.0, value=400.0)
    ocean_ph = st.number_input("Ocean pH (Acidification)", min_value=7.0, value=8.1)

with col3:
    sea_level = st.number_input("Sea Level (cm)", min_value=-100.0, value=0.0)
    glacier_mass = st.number_input("Glacier Mass Balance (Gt)", min_value=-1000.0, value=50.0)
    arctic_ice = st.number_input("Arctic Sea Ice Extent (10⁶ km²)", min_value=0.0, value=7.0)
    antarctic_ice = st.number_input("Antarctic Sea Ice Extent (10⁶ km²)", min_value=0.0, value=10.0)

# Prepare the inputs in a list
inputs = [
    unemployment_rate, inflation_rate, avg_temp, avg_wind_speed, cloud_cover,
    avg_humidity, precipitation, ocean_heat, co2, ocean_ph, sea_level, 
    glacier_mass, arctic_ice, antarctic_ice
]

# Button to make prediction
if st.button('Predict Misery Index'):
    # Predict the misery index
    predicted_value = predict_misery_index(inputs)
    
    # Categorize the misery index
    category = categorize_misery_index(predicted_value)
    
    # Display the result
    st.write(f"The predicted Misery Index is: **{predicted_value:.2f}**")
    st.write(f"Category: **{category}**")

