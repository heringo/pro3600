# Projet info TSP

import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import math
import scipy
from scipy.stats import norm
import numpy as np

# -------------------------------------------------
# Partie 1 : données historiques d'une action

# Define the ticker list
tickers_list = ['AAPL']

# Extract the necessary data
start_day = "2022-01-01"
end_day = "2023-01-01"
stock = yf.download(tickers_list, start_day, end_day)
stock_price = yf.download(tickers_list, start_day, end_day)["Adj Close"]


# On calcule la valeur de la volatilité sigma d'un certain stock
def volatility():
    stock['daily_returns'] = (stock['Close'].pct_change())*100
    stock.dropna(inplace=True)
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.spines[['top', 'right', 'left', 'bottom']].set_visible(False)
    daily_volatility_stock = stock['daily_returns'].std()
    monthly_volatility_stock = math.sqrt(21) * daily_volatility_stock
    annual_volatility_stock = math.sqrt(252) * daily_volatility_stock
    return (0.5 + annual_volatility_stock / 100)

# -----------------------------------------------------------------------
# Partie 2 : Simulations à comparer avec les données historiques d'une action


# Initialisation des paramètres pour les simulations

S0 = stock_price[0]  # initial stock price
K = 152  # strike price
r = 0.025  # risk-free interest rate
sigma = volatility()  # volatility in market
T = 1  # time in years
N = stock_price.index.size  # number of steps within each simulation
deltat = T/N  # time step
i = 5  # number of simulations
discount_factor = np.exp(-r*T)  # discount factor

# Calculs et plot

S = np.zeros([N, i])
stock_array = pd.DataFrame(stock).to_numpy()
year_dates_stock = stock_price.index
t = range(0, N, 1)


for y in range(0, i):
    S[0, y] = S0
    for x in range(0, N-1):
        S[x+1, y] = S[x, y]*(np.exp((r-(sigma**2)/2)
                                    * deltat + sigma*deltat*np.random.normal(0, 1)))
    plt.plot(year_dates_stock, S[:, y])

plt.plot(stock_price, "black")
plt.xlabel('Time')
plt.ylabel('Stock Price')
plt.show()

# -----------------------------------------------------------------------
# Espace de travail
