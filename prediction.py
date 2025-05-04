import numpy as np
import pandas as pd

# Make prediction
def make_prediction(model, year, month, avg_temp, max_temp, min_temp):
    """
    Make prediction of Rainfall for a given month and year

    Parameters:
        model: Trained machine learning model
        year (int): Year of prediction
        month (int): Month of prediction (1-12)
        avg_temp (float): Average temperature in Celsius
        max_temp (float): Maximum temperature in Celsius
        min_temp (float): Minimum temperature in Celsius

    Returns:
        float: Predicted total rainfall in mm
    """
    features = np.array([[year, month, avg_temp, max_temp, min_temp]])
    prediction = model.predict(features)
    return prediction[0]

# GEt the historical context
def get_historical_context(df, month):
    """
    Get the historical context
    """
    years = df['Year'].unique()
    hist_temps = []

    for year in years:
        month_data = df[(df['Year'] == year) & (df['Month'] == month)]
        if not month_data.empty:
            hist_temps.append((year, month_data['Total_Rainfall_mm'].values[0]))

    return hist_temps

def get_historical_average(df, month):
    """
    Get historical Average rain for a given monthecho "# Rainfall_Changes_Tanzania" >> README.md
    """
    return df[df['Month'] == month]['Total_Rainfall_mm'].mean()