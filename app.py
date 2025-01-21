import streamlit as st
import joblib
import pandas as pd

# Load the pre-trained model
model = joblib.load('misery_index_model.pkl')
print(model.feature_names_in_)
# Function to make predictions
def predict_misery_index(inputs):
    # Convert input into a DataFrame to match the model's input shape
    input_data = pd.DataFrame([inputs], columns=[
        'unemployment', 'inflation', 'climate_index'
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
This app predicts the **Misery Index** based on **Unemployment Rate**, **Inflation Rate**, and **Climatic Factors**. Please input the following values:
""")

# Input fields for the user to enter values
unemployment = st.number_input("Unemployment Rate (%)", min_value=0.0, value=10.0)
inflation = st.number_input("Inflation Rate (%)", min_value=0.0, value=10.0)

# Combine climatic factors into a single input, e.g., average of climatic variables or custom input
climate = st.number_input("Climate", min_value=-100.0, value=25.0)

# Prepare the inputs in a list (only unemployment, inflation, and combined climate)
inputs = [
    unemployment, inflation, climate
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
