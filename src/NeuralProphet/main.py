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
import neural_date
import forecast_list_and_dates
import plot


def main(ticker : str ='AAPL' ,forecast_period : int = 60 , number_of_training_years : int = 10):
    """ Simulation of the market 'ticker' using yahoo finance. 


    Args:
        ticker (str,optional) : ticker from yfinance (market to simulate).Default stock is Apple.
        forecast_period (int,optional) : number of days you want to predict.Default value is 60 days.
        number_of_training_years (int,optional) : number of years on which the model is trained(try Values between 1-10).Default Value is 10 years.
    """

    # Override the pandas_datareader
    
    yf.pdr_override()

    ##Daily Forecasting

    #Set the predefined variables
    
    number_of_years=number_of_training_years

    # Set the end date as today's date
    
    end_date = neural_date.get_current_date()
    date_from_years_ago = neural_date.subtract_years(end_date, number_of_years)

    # Set the start date as 10 years before the end date
    start_date =date_from_years_ago

    #Get the data

    df = pdr.get_data_yahoo(ticker,start=start_date,end=end_date)

    #Preprocess the data

    df=df.reset_index(drop=False)
    df=df[['Date','Adj Close']]
    df['Date']=pd.to_datetime(df['Date'])

    #Renaming the columns for the NeuralProphet model

    df=df.rename(columns={'Date':'ds','Adj Close':'y'})
    df['ds']=pd.to_datetime(df['ds'])

    #Fill in the missing values with linear interpolation method

    df['y']=df['y'].interpolate()
    

    #Instantiate the model with parameters

    m=NeuralProphet(changepoints_range=0.98,n_changepoints=30,batch_size=128,epochs=150)

    #Fitting the model

    m.fit(df)

    #Modify the data using .makefuture_dataframe to get the new dates with +forecast_period dates

    future=m.make_future_dataframe(df, periods=forecast_period, n_historic_predictions=True)
   

    #Predict on the future data

    forecast=m.predict(future)
    

    #If you want to plot unhashtag the following :
    
    #plot.plotting(m,forecast).show()

    #Get the values and the dates of the forecast into the correct format for putting them in a .txt afterwards
    forecast_list_and_dates.forecastdates(forecast)
    forecast_list_and_dates.forecastvalues(forecast)

if __name__=='__main__':
         main()

