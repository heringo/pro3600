
import pandas as pd
from neuralprophet import NeuralProphet
def forecastvalues(forecast : pd.DataFrame):

    """This function takes the forecast dataframe from NeuralProphet( yhat1 is the prediction column) and returns the predicted values of the forecast and put them in a list as strings
    
    Args: forecast (pd.DataFrame): The forecast dataframe
    
    Returns: The predicted values  of the forecast as a list of strings
    """
    
    forecast = forecast['yhat1'].values
    
    
    return forecast

def forecastdates(forecast : pd.DataFrame):
    """This function takes the forecast dataframe from NeuralProphet( ds is the date column) and returns the predicted dates of the forecast and put them in a list as strings
    Args: forecast (pd.DataFrame): The forecast dataframe
    
    Returns: The predicted dates of the forecast as a list of strings"""

    forecast = forecast['ds'].values
    
    forecast= pd.to_datetime(forecast)
    
    forecast=forecast.strftime("%Y-%m-%d")
    
    
    return forecast