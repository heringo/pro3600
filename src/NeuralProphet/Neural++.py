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

# Daily Forecasting
#df = pdr.get_data_yahoo('AAPL', start='2010-01-01',end='2023-05-08')
# df=df.reset_index(drop=False)
#df=df[['Date','Adj Close']]
# df['Date']=pd.to_datetime(df['Date'])
#df=df.rename(columns={'Date':'ds','Adj Close':'y'})
# m=NeuralProphet()
#m.fit(df, freq="D")
#future=m.make_future_dataframe(df, periods=60, n_historic_predictions=len(df))
# forecast=m.predict(future)
# fig=m.plot(forecast)
# fig.show()

# Minute Forecasting
# set the appropriate forecast period
forecast_period = 60
# Set the end date as today's date

# Set the end date as today's date
end_date = datetime.datetime.now().strftime("%m/%d/%Y")
# Set the start date as 7 days before the end date
start_date = (datetime.datetime.now() -
              datetime.timedelta(days=7)).strftime("%m/%d/%Y")
# Get the minute data for a specific stock for the last 7 days
stock_data = si.get_data("AAPL", start_date=start_date,
                         end_date=end_date, interval="1m")
# Reformat the data to only include the Date and Close columns
stock_data = stock_data.reset_index(drop=False)

stock_data = stock_data[['index', 'close']]
# Rename the columns to match the Prophet API
stock_data = stock_data.rename(columns={'index': 'ds', 'close': 'y'})
# Convert the Date column to a datetime type
stock_data['ds'] = pd.to_datetime(stock_data['ds'])
# Filter the data
date = stock_data['ds'].max()-datetime.timedelta(minutes=forecast_period)
stock_data1 = stock_data.loc[stock_data['ds'] < date, ['ds', 'y']]
# Initialize the model and fit the data
m = NeuralProphet(changepoints_range=0.90, seasonality_mode='multiplicative',
                  daily_seasonality=4, ar_reg=0.25, num_hidden_layers=3, d_hidden=64)
m.fit(stock_data1, freq="min")
future = m.make_future_dataframe(
    stock_data1, periods=forecast_period, n_historic_predictions=len(stock_data))
forecast = m.predict(future)
# fig=m.plot(forecast)
# fig.show()

# List of forecast values


def forecastvalues(forecast):
    forecast = forecast['yhat1'].values
    return forecast


def forecastdates(forecast):
    forecast = forecast['ds'].values
    forecast = pd.to_datetime(forecast)
    forecast = forecast.strftime("%Y-%m-%dT%H:%M:%S")
    return forecast


# print(forecastdates(forecast))
# print(forecastvalues(forecast))
actuals = stock_data.set_index('ds').iloc[-len(forecast):]['y'].reset_index()
actuals['y'] = actuals['y'].interpolate()
fig = m.plot(forecast)
fig.update_traces(name='Forecast', showlegend=True)
fig.add_scatter(x=actuals['ds'], y=actuals['y'], mode='lines', name='Actuals')
fig.show()

# Write the forecast values and dates to txt files

# def write_forecastvalues_to_txt(forecast, file_path):

# with open(file_path, 'w') as f:
# for val in forecast:
# f.write(f"{val}\n")
#write_forecastvalues_to_txt(forecastvalues(forecast), './ProjetInfo/pro3600/forecast.txt')

# def write_forecastdates_to_txt(forecast, file_path):

# with open(file_path, 'w') as f:
# for val in forecast:
# f.write(f"{val}\n")
#write_forecastdates_to_txt(forecastdates(forecast), './ProjetInfo/pro3600/forecastdates.txt')
