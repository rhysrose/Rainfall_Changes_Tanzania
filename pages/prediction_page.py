import streamlit as st
import numpy as np
from model_utils import load_model
from visualization import plot_prediction_context
from prediction import make_prediction, get_historical_average, get_historical_context
def show(df):
    """Display the prediction page"""
    st.header("Rainfall Predictions")

    # Check if the model exists
    if 'model' not in st.session_state:
        model = load_model()
        if model is None:
            st.warning("No trained Model found. Please go to the model training page first")
            st.stop()
        st.session_state['model'] = model
        st.session_state['model_type'] = "Pre-trained model"

    #Show the model that is being used
    st.info(f"Using {st.session_state['model_type']} for predictions")

    # Prediction input
    st.subheader("Select the date for predictiion")
    pred_year = st.slider("Year", 2010, 2030, 2025)
    pred_month = st.slider("Month", 1, 12, 6)
    avg_temp = st.number_input("Average Temperature (°C)", value=25.0)
    max_temp = st.number_input("Max Temperature (°C)", value=30.0)
    min_temp = st.number_input("Min Temperature (°C)", value=20.0)

    # Make prediction
    if st.button("Predict Rainfall"):
        # Get model
        model = st.session_state['model']

        # Make prediction
        prediction = make_prediction(model, pred_year, pred_month, avg_temp, max_temp, min_temp)

        # Display the results
        st.success(f"Predicted Rainfall for {pred_year}-{pred_month:02d} : {prediction:.2f} C")

        # Give the historical comparison
        hist_avg = get_historical_average(df, pred_month)

        st.write(f"Historical average for month {pred_month}: {hist_avg:.2f}C")
        
        # Calculate the difference 
        diff = prediction - hist_avg
        if diff > 0:
            st.write(f"Prediction is {diff:.2f}C **higher** than historical average")
        else:
            st.write(f"Prediction is {abs(diff):.2f}C **Lower** than historical average")

        # Visualize
        st.subheader("Prediction in the Historical Context")

        # GEt the historical context
        hist_temps = get_historical_context(df, pred_month)

        # plot prediction context
        fig = plot_prediction_context(hist_temps, pred_year, pred_month, prediction)
        st.pyplot(fig)