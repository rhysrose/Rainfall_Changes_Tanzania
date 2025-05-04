#Import Libraries
import pandas as pd
import numpy as np
import streamlit as st

#load the data
#filepath = r"/Users/rosepeterfunja/Tanzania_KIC/Assignment/capstone-project-rhysrose/data/tanzania_climate_data.csv"
filepath = "/data/tanzania_climate_data.csv"
@st.cache_data
def load_data(filepath):
    """
    Load the climate CSV data from the given filepath

    Parameters:
    filepath(str): Path to the CSV file

    Returns:
    pd.DataFrame: loaded and cached Dataframe
    """

    try:
        data = pd.read_csv(filepath)
        # Create a Date column by combining Year and Month
        data['Date'] = pd.to_datetime(data[['Year', 'Month']].assign(DAY=1))
        return data
    except FileNotFoundError:
        st.error(f"File not found: {filepath}")
        return pd.DataFrame()
    except Exception as e:
        st.error(f"An error occured: {e}")
        return pd.DataFrame()
    

def prepare_features(df):
    """
    Prepare the Features for model training
    """
    X = df[['Year','Month','Average_Temperature_C','Max_Temperature_C','Min_Temperature_C']].values
    y = df[['Total_Rainfall_mm']].values
    return X, y
