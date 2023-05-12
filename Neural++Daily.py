# Importing necessary libraries
from neuralprophet import NeuralProphet
import numpy as np
import pandas as pd 
import yfinance as yf
import matplotlib.pyplot as plt 
import plotly
from pandas_datareader import data as pdr
import datetime
import plotly_resampler
from dateutil.relativedelta import relativedelta

 # Get the current date in the desired format
def get_current_date():
    return datetime.date.today().strftime('%Y-%m-%d')

#Function to obtain the start date by substracting a number of years
def subtract_years(date_str, years):
    date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
    new_date_obj = date_obj - datetime.timedelta(days=365*years)
    return new_date_obj.strftime('%Y-%m-%d')

# Override the pandas_datareader
yf.pdr_override()

##Daily Forecasting

#Set the predefined variables
forecast_period=120
number_of_years=10

# Set the end date as today's date
end_date = get_current_date()
ten_years_ago = subtract_years(end_date, 10)

# Set the start date as 10 years before the end date
start_date = ten_years_ago

#Get the data
df = pdr.get_data_yahoo('AMZN', start=start_date,end=end_date)

#Preprocess the data
df=df.reset_index(drop=False)
df=df[['Date','Adj Close']]
df['Date']=pd.to_datetime(df['Date'])

#Renaming the columns for the NeuralProphet model
df=df.rename(columns={'Date':'ds','Adj Close':'y'})
df['ds']=pd.to_datetime(df['ds'])

#Fill in the missing values with the linear interpolation method
df['y']=df['y'].interpolate()

#Instantiate the model with parameters
m=NeuralProphet(changepoints_range=0.95,n_changepoints=30,batch_size=128,epochs=150)

#Fitting the model
m.fit(df, freq="B")

#Modify the data using .makefuture_dataframe to get the new dates with +120 days
future=m.make_future_dataframe(df, periods=forecast_period, n_historic_predictions=len(df))

#Predict on the future data
forecast=m.predict(future)

#Plotting the data
fig=m.plot(forecast)
fig.show()

#Defining a function to get the predicted values of the forecast and put them in a list as strings
def forecastvalues(forecast):
    forecast = forecast['yhat1'].values
    return forecast

#Defining a function to get the predicted dates of the forecast and put them in a list as strings
def forecastdates(forecast):
    forecast = forecast['ds'].values
    forecast= pd.to_datetime(forecast)
    forecast=forecast.strftime("%Y-%m-%d")
    return forecast
forecastdates(forecast)
forecastvalues(forecast)

