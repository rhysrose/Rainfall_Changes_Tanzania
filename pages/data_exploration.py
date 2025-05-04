import streamlit as st
from visualization import plot_time_series, plot_seasonal_patterns, plot_yearly_trends

def show(df):
    """
    Display the data exploration page

    """
    st.header(" Data Exploration")

    # Show the raw data
    st.subheader("Raw Temperature and rainfall Data ")
    st.dataframe(df.head(10))

    # Show the basic statistics
    st.subheader("Statistical Summary")
    st.write(df['Total_Rainfall_mm'].describe())

    # Time series plot
    st.subheader("Rainfall over time")
    fig = plot_time_series(df)
    st.pyplot(fig)

    # Plot the seasonal plot
    st.subheader("Seasonal Rainfall Patterns")
    fig = plot_seasonal_patterns(df)
    st.pyplot(fig)

    # Plot the yearly average trends
    st.subheader("Yearly Average Rainfalls")
    fig = plot_yearly_trends(df)
    st.pyplot(fig)