
import pandas as pd
from neuralprophet import NeuralProphet
def forecastvalues(forecast : pd.DataFrame,forecast_period : int = 60):

    """This function takes the forecast dataframe from NeuralProphet( yhat1 is the prediction column) and returns the predicted values of the forecast and put them in a list as strings
    
    Args: forecast (pd.DataFrame): The forecast dataframe
    
    Returns: The predicted values  of the forecast as a list of strings
    """
    yhat = pd.concat([forecast['yhat1'][:-forecast_period],forecast[f'yhat{forecast_period}'].tail(forecast_period)], ignore_index=True)
    yhat=yhat.reset_index(drop=True)
    yhat=yhat.interpolate()

    forecast_ds_reset = forecast['ds'].reset_index(drop=True)

    result = pd.DataFrame({'ds': forecast_ds_reset, 'yhat': yhat})
    result =result['yhat'].values
    
    
    return result

def forecastdates(forecast : pd.DataFrame):
    """This function takes the forecast dataframe from NeuralProphet( ds is the date column) and returns the predicted dates of the forecast and put them in a list as strings
    Args: forecast (pd.DataFrame): The forecast dataframe
    
    Returns: The predicted dates of the forecast as a list of strings"""

    forecast = forecast['ds'].values
    
    forecast= pd.to_datetime(forecast)
    
    forecast=forecast.strftime("%Y-%m-%d")
    
    
    return forecast