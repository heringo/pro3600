import plotly
from neuralprophet import NeuralProphet
import pandas as pd
def plotting(m : NeuralProphet,forecast : pd.DataFrame):
    """This function takes the model from NeuralProphet and the forecast and uses NeuralProphetplot to create a figure which will be plotted in main

    Args: m (NeuralProphet) the NeuralProphet model instantiated
           forecast (pd.DataFrame): The forecast dataframe

    Returns: fig (Figure : Any) The figure from plotly which will be plotted
    """
    
    fig=m.plot(forecast)
    
    
    return fig