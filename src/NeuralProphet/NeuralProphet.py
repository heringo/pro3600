import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly_resampler
# Load the dataset using pandas
data = pd.read_csv("/Users/theoniemann/Downloads/AAPL.csv") 
# Select only the important features i.e. the date and price
data = data[["Date","Close"]] 
data= data.dropna() # drop the rows with missing values
# select Date and Price
# Rename the features: These names are NEEDED for the model fitting
data = data.rename(columns = {"Date":"ds","Close":"y"}) #renaming the columns of the dataset
from neuralprophet import NeuralProphet
# m = NeuralProphet() # default model
# our model
m = NeuralProphet()
metrics = m.fit(data)  # fit the model using all data
# with cross-validation
# metrics = m.fit(data, 
#                 freq="D",
#                 valid_p=0.2, # validation proportion of data (20%)
#                 epochs=100)
# Predict on the future
forecast = m.predict(data)
future = m.make_future_dataframe(data, periods=60, n_historic_predictions=len(data))
predictions = m.predict(future)
# Plot the predictions
fig = m.plot(predictions)
fig.show()
fig2 = m.plot_components(predictions)
fig2.show()
