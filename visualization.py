import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def plot_time_series(df):
    """
    Plot the rainfall over time
    """
    fig, ax = plt.subplots(figsize = (10,6))
    ax.plot(df['Date'], df['Total_Rainfall_mm'])
    ax.set_xlabel("Date")
    ax.set_ylabel("Rainfal in mm")
    ax.set_title("Monthly Average Rainfall")
    ax.grid(True)
    return fig

def plot_seasonal_patterns(df):
    """
    Plot monthly rainfall distributions
    """ 
    fig, ax = plt.subplots(figsize = (10,6))
    sns.boxplot( x = 'Month', y = 'Total_Rainfall_mm', data = df, ax = ax)
    ax.set_xlabel("Month")
    ax.set_ylabel("Rainfal in mm")
    ax.set_title("Monthly Rainfall Distributions")
    return fig

def plot_yearly_trends(df):
    """
    Plot the yearly average  rainfall 
    """
    year_avg = df.groupby('Year')['Total_Rainfall_mm'].mean().reset_index()
    fig, ax = plt.subplots(figsize = (10,6))
    ax.plot(year_avg['Year'],year_avg['Total_Rainfall_mm'], marker = 'o')
    ax.set_xlabel("Year")
    ax.set_ylabel("Rainfal in mm")
    ax.set_title("Yearly Average Rainfall")
    ax.grid(True)
    return fig

def plot_actual_vs_Predicted_Rainfall(y_test, y_pred):
    """
    Plt the actual vs predicted values
    """
    fig, ax = plt.subplot(figsize = (10,6))
    ax.scatter(y_test, y_pred, alpha = 0.7 )
    ax.plot([min(y_test), max(y_test)],[min(y_test), max(y_test)], 'r--' )
    ax.set_xlabel("Actual Rainfall")
    ax.set_ylabel("Predicted Rainfall")
    ax.set_title("Actual vs Predicted Rainfall")
    return fig

def plot_prediction_context(hist_rainfall, pred_year, pred_month, prediction):
    """
    Plot the prediction in historical context
    """
    years_hist, rainfall_hist = zip(*hist_rainfall)

    fig, ax = plt.subplots(figsize = (10, 6))
    # Plot the historical data for that month
    ax.scatter(years_hist, rainfall_hist, label = f"Historical (Month {pred_month})", color = 'blue')
    ax.plot(years_hist, rainfall_hist, 'b--', alpha = 0.6)

    # Plot the prediction
    ax.scatter([pred_year], [prediction], color = 'red', s = 100, label = 'Prediction')
    # Add a trend line
    z = np.polyfit(years_hist, rainfall_hist, 1)
    p = np.poly1d(z)
    ax.plot(range(2010, pred_year+1), p(range(2010, pred_year + 1)), 'g-', label = 'Trend')
    ax.set_xlabel("Year")
    ax.set_ylabel(f"Rainfall for month {pred_month} in C")
    ax.set_title("Historical Context")
    ax.legend()
    ax.grid(True)
    return fig 