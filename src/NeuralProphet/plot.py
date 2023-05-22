import plotly.express as px
from neuralprophet import NeuralProphet
import pandas as pd
def plotting(m : NeuralProphet,forecast : pd.DataFrame,forecast_period : int = 60):
    """This function takes the model from NeuralProphet and the forecast and uses NeuralProphetplot to create a figure which will be plotted in main

    Args: m (NeuralProphet) the NeuralProphet model instantiated
           forecast (pd.DataFrame): The forecast dataframe

    Returns: fig (Figure : Any) The figure from plotly which will be plotted
    """
    
    yhat=pd.concat([forecast['yhat1'][:-forecast_period],forecast[f'yhat{forecast_period}'].tail(forecast_period)],ignore_index=True)
    yhat=yhat.reset_index(drop=True)
    yhat=yhat.interpolate()

    forecast_ds_reset = forecast['ds'].reset_index(drop=True)

    result = pd.DataFrame({'ds': forecast_ds_reset, 'yhat': yhat})
    fig=px.line(result,x='ds',y='yhat')
    return fig