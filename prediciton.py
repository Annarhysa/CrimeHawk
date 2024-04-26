import numpy as np
import pandas as pd
import ipywidgets as widgets
from IPython.display import display
from prophet import Prophet
import matplotlib.pyplot as plt
import datetime
import warnings
warnings.filterwarnings("ignore")


def pred(data):

    # Ensure 'YEAR' is in a proper date format
    data['YEAR'] = pd.to_datetime(data['YEAR'].astype(str) + "-01-01")

    # Get the current date
    current_date = datetime.datetime.now()

    # Extend the data to include at least the current date
    latest_date = data['YEAR'].max()
    if latest_date < current_date:
        current_row = pd.DataFrame({
            'STATE/UT': ["UNKNOWN"],  # Use an appropriate value for your context
            'YEAR': [current_date],
            'TOTAL IPC CRIMES': [0]  # Default value; adjust as needed
        })
        data = pd.concat([data, current_row], ignore_index=True)

    # Group by year and sum total IPC crimes
    crime_ts = data.groupby(['YEAR'])['TOTAL IPC CRIMES'].sum().reset_index()

    # Rename columns for Prophet
    crime_ts.rename(columns={'YEAR': 'ds', 'TOTAL IPC CRIMES': 'y'}, inplace=True)

    # Create a Prophet model
    model = Prophet()

    # Fit the model
    model.fit(crime_ts)

    # Generate future dates for prediction
    # We use the current date and add the desired number of future days
    future_dates = pd.date_range(current_date, periods=7, freq='D')

    # Convert to DataFrame with 'ds' column for Prophet
    future_dates_df = pd.DataFrame({'ds': future_dates})

    # Predict future values
    forecast = model.predict(future_dates_df)

    return model,forecast

#fig2 = model.plot_components(forecast)
#plt.show()