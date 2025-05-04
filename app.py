import streamlit as st
from pages import data_exploration, model_training, prediction_page
from data_utils import load_data

# Set the epage configurations
st.set_page_config(
    page_title= "Climate  Trend Predictor",
    page_icon= '🌦️', 
    layout= "wide"
)

# Give the Title and description
st.title("Climate Trend Analysis and Prediction")
st.markdown("Analyze the Historical Rainfall and Predict Future Trends")

#load the data
#filepath = r"/Users/rosepeterfunja/Tanzania_KIC/Assignment/capstone-project-rhysrose/data/tanzania_climate_data.csv"
filepath = "tanzania_climate_data.csv"
df = load_data(filepath)

#Check if data is loaded 
st.write("Data Loaded")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ['Data Exploration' ,'Model Training', 'Prediction'])

#Display the selected Page
if page == "Data Exploration":
    data_exploration.show(df)
elif page == "Model Training":
    model_training.show(df)
else:
    prediction_page.show(df)


