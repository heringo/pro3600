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
def get_current_date():
    # Get the current date in the desired format
    return datetime.date.today().strftime('%Y-%m-%d')

def subtract_years(date_str, years):
    # Convert the date string to a datetime object
    date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
    # Subtract the specified number of years from the date object
    new_date_obj = date_obj - datetime.timedelta(days=365*years)
    # Convert the new date object back to a string and return it
    return new_date_obj.strftime('%Y-%m-%d')
# Override the pandas_datareader
yf.pdr_override()
#Daily Forecasting
#Set the predefined variables
forecast_period=60
number_of_years=10

# Set the end date as today's date
end_date = get_current_date()
ten_years_ago = subtract_years(end_date, 10)
# Set the start date as 10 years before the end date
start_date = ten_years_ago
print(start_date)
df = pdr.get_data_yahoo('AAPL', start=start_date,end=end_date)
df=df.reset_index(drop=False)
df=df[['Date','Adj Close']]
df['Date']=pd.to_datetime(df['Date'])
df=df.rename(columns={'Date':'ds','Adj Close':'y'})
df['ds']=pd.to_datetime(df['ds'])
df['y']=df['y'].interpolate()
m=NeuralProphet(changepoints_range=0.8,n_changepoints=5,ar_reg=1,num_hidden_layers=3,d_hidden=64)
m.fit(df, freq="B")
future=m.make_future_dataframe(df, periods=60, n_historic_predictions=len(df))
forecast=m.predict(future)
fig=m.plot(forecast)
fig.show()
def forecastvalues(forecast):
    forecast = forecast['yhat1'].values
    return forecast
def forecastdates(forecast):
    forecast = forecast['ds'].values
    forecast= pd.to_datetime(forecast)
    forecast=forecast.strftime("%Y-%m-%d")
    return forecast
#print(forecastdates(forecast))
#print(forecastvalues(forecast))

