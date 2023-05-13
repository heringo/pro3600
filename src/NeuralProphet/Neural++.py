# Importing necessary libraries
from neuralprophet import NeuralProphet
import numpy as np
import pandas as pd 
import yfinance as yf
import matplotlib.pyplot as plt 
import plotly
from pandas_datareader import data as pdr
import yahoo_fin.stock_info as si
import datetime
import plotly_resampler

# Override the pandas_datareader
yf.pdr_override()


##Minute Forecasting

#Set the appropriate forecast period
forecast_period=60
number_of_days=1

 # Set the end date as today's date
end_date = datetime.datetime.now().strftime("%m/%d/%Y")
 
 # Set the start date as 7 days before the end date
start_date = (datetime.datetime.now() - datetime.timedelta(days=number_of_days)).strftime("%m/%d/%Y")

 # Get the minute data for a specific stock for the last 7 days
stock_data = si.get_data("SOI.PA", start_date=start_date, end_date=end_date, interval="1m")
 
 # Reformat the data to only include the Date and Close columns
stock_data = stock_data.reset_index(drop=False)
stock_data = stock_data[['index', 'close']]

# Rename the columns to match the Prophet API
stock_data = stock_data.rename(columns={'index': 'ds', 'close': 'y'})

# Convert the Date column to a datetime type
stock_data['ds'] = pd.to_datetime(stock_data['ds'])

#Filter the data
date=stock_data['ds'].max()-datetime.timedelta(minutes=forecast_period)
stock_data1 = stock_data.loc[stock_data['ds'] < date, ['ds', 'y']]

#Initialize the model and fit the data
m=NeuralProphet(changepoints_range=0.95,ar_reg=0.5,num_hidden_layers=5,d_hidden=64)
m.fit(stock_data1, freq="min")
future=m.make_future_dataframe(stock_data1, periods=forecast_period, n_historic_predictions=len(stock_data))
forecast=m.predict(future)
#fig=m.plot(forecast)
#fig.show()

#List of forecast values
def forecastvalues(forecast):
    forecast = forecast['yhat1'].values
    return forecast
def forecastdates(forecast):
    forecast = forecast['ds'].values
    forecast= pd.to_datetime(forecast)
    forecast=forecast.strftime("%Y-%m-%dT%H:%M:%S")
    return forecast
actuals = stock_data.set_index('ds').iloc[-len(forecast):]['y'].reset_index()
actuals['y'] = actuals['y'].interpolate()
fig = m.plot(forecast)
fig.update_traces(name='Forecast', showlegend=True)
fig.add_scatter(x=actuals['ds'], y=actuals['y'], mode='lines', name='Actuals')
fig.show()
