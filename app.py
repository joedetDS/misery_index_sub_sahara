import streamlit as st
import joblib
import pandas as pd
import datetime

# Load the pre-trained model
model = joblib.load('misery_index_model.pkl')

# Title of the app
st.title("Misery Index Prediction")

# Explanation of the app
st.markdown("""
This app predicts the **Misery Index** based on **Unemployment Rate**, **Inflation Rate**, **Climatic Factors**, and a **Year**. 
Enter the required values to get the prediction.
""")

# Input fields for the user to enter values
year = st.number_input(
    "Year", 
    min_value=datetime.datetime.now().year, 
    value=datetime.datetime.now().year, 
    step=1
)
unemployment = st.number_input("Unemployment Rate (%)", min_value=0.0, value=10.0)
inflation = st.number_input("Inflation Rate (%)", min_value=0.0, value=10.0)
climate_index = st.number_input("Climate Index", min_value=-100.0, value=25.0)

# Prepare the inputs for prediction
inputs = [unemployment, inflation, climate_index]

# Button to make prediction
if st.button('Predict Misery Index'):
    # Convert input into a DataFrame to match the model's input shape
    input_data = pd.DataFrame([inputs], columns=['unemployment', 'inflation', 'climate_index'])
    
    # Predict the misery index
    predicted_value = model.predict(input_data)[0]
    
    # Display the result
    st.write(f"The predicted Misery Index for the year **{int(year)}** is: **{predicted_value:.2f}**")
