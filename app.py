import streamlit as st
import joblib
import pandas as pd

# Load the pre-trained model
model = joblib.load('misery_index_model.pkl')

# Function to make predictions
def predict_misery_index(inputs):
    # Convert input into a DataFrame to match the model's input shape and feature order
    input_data = pd.DataFrame([inputs], columns=[
        'inflation', 'unemployment', 'climate_index'  # Match the order in feature_names_in_
    ])
    
    # Perform the prediction
    prediction = model.predict(input_data)
    return prediction[0]

# Title of the app
st.title("Misery Index Prediction")

# Explanation of the app
st.markdown("""
This app predicts the **Misery Index** based on **Unemployment Rate**, **Inflation Rate**, and **Climatic Factors**. Please input the following values:
""")

# Input fields for the user to enter values
unemployment = st.number_input("Unemployment Rate (%)", min_value=0.0, value=10.0)
inflation = st.number_input("Inflation Rate (%)", min_value=0.0, value=10.0)

# Combine climatic factors into a single input, e.g., average of climatic variables or custom input
climate_index = st.number_input("Climate Index", min_value=-100.0, value=25.0) 

# Prepare the inputs in the correct order as required by the model
inputs = [
    inflation, unemployment, climate_index  # Match the model's expected feature order
]

# Button to make prediction
if st.button('Predict Misery Index'):
    # Predict the misery index
    predicted_value = predict_misery_index(inputs)
    
    # Display the result
    st.write(f"The predicted Misery Index is: **{predicted_value:.2f}**")
