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
from dateutil.relativedelta import relativedelta

# Override the pandas_datareader
yf.pdr_override()
#Daily Forecasting
forecast_period=60
number_of_years=10
# Set the end date as today's date
end_date = datetime.datetime.now().strftime("%Y-%m-%d")
# Set the start date as 10 years before the end date
start_date = (datetime.datetime.now() - relativedelta(year=number_of_years)).strftime("%Y-%m-%d")
df = pdr.get_data_yahoo('AAPL', start=start_date,end=end_date)
df=df.reset_index(drop=False)
df=df[['Date','Adj Close']]
df['Date']=pd.to_datetime(df['Date'])
df=df.rename(columns={'Date':'ds','Adj Close':'y'})
df['ds']=pd.to_datetime(df['ds'])
df['y']=df['y'].interpolate()
m=NeuralProphet(changepoints_range=0.95,ar_reg=0.5,num_hidden_layers=5,d_hidden=64)
m.fit(df, freq="B")
future=m.make_future_dataframe(df, periods=forecast_period, n_historic_predictions=len(df))
forecast=m.predict(future)
fig=m.plot(forecast)
fig.show()
def forecastvalues(forecast):
    forecast = forecast['yhat1'].values
    return forecast
def forecastdates(forecast):
    forecast = forecast['ds'].values
    forecast= pd.to_datetime(forecast)
    forecast=forecast.strftime("%Y-%m-%dT%H:%M:%S")
    return forecast
#print(forecastdates(forecast))
#print(forecastvalues(forecast))