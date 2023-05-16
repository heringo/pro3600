import yfinance as yf
import pandas as pd
from scipy.stats import norm
from datetime import datetime
import datetime
from neuralprophet import NeuralProphet
import numpy as np
import pandas as pd 
from pandas_datareader import data as pdr
import datetime



def neural(ticker):
    # Override the pandas_datareader
    yf.pdr_override()

    # Daily Forecasting
    # Set the predefined variables
    forecast_period = 60
    number_of_years = 10

    # Set the end date as today's date
    auj = datetime.date.today()
    end_date = auj.strftime('%Y-%m-%d')

    # Set the start date as 10 years before the end date
    date_obj = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()
    new_date_obj = date_obj - datetime.timedelta(days=365*number_of_years)
    ten_years_ago = new_date_obj.strftime('%Y-%m-%d')
    start_date = ten_years_ago

    df = pdr.get_data_yahoo(ticker, start=start_date, end=end_date)
    df = df.reset_index(drop=False)
    df = df[['Date', 'Adj Close']]
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.rename(columns={'Date': 'ds', 'Adj Close': 'y'})
    df['ds'] = pd.to_datetime(df['ds'])
    df['y'] = df['y'].interpolate()

    m = NeuralProphet()
    m.fit(df, freq="B")

    future = m.make_future_dataframe(df, periods=forecast_period, n_historic_predictions=len(df))
    forecast = m.predict(future)

    forecast_values = forecast['yhat1'].values
    forecast_dates = forecast['ds'].dt.strftime("%Y-%m-%d")
    return (forecast_values, forecast_dates)

