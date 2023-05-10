# Projet info TSP

import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import math
import scipy
from scipy.stats import norm
import numpy as np
import pandas_market_calendars as mcal
from datetime import timedelta, datetime


# -------------------------------------------------
# Partie 1 : données historiques d'une action

# Define the ticker list
tickers_list = ['INTC']

# Extract the necessary data
start_day_train = "2022-10-01"
end_day_train = "2023-03-15"
start_day_test = "2023-03-15"
end_day_test = "2023-04-10"

stock_train = yf.download(tickers_list, start_day_train, end_day_train)
stock_test = yf.download(tickers_list, start_day_test, end_day_test)
stock_total = yf.download(tickers_list, start_day_train, end_day_test)

nyse = mcal.get_calendar('NYSE')
dates_stock_train = nyse.schedule(
    start_date=start_day_train, end_date=end_day_train).index
dates_stock_total = nyse.schedule(
    start_date=start_day_train, end_date=end_day_test).index
dates_stock_test = nyse.schedule(
    start_date=start_day_test, end_date=end_day_test).index

# -----------------------------------------------------------------------
# Partie 2 : Calcul de la volatitlité et du drift


def volatility():
    stock_train['Daily Return'] = stock_train['Adj Close'].pct_change(1)
    daily_volatility_stock = stock_train['Daily Return'].std()
    monthly_volatility_stock = math.sqrt(21) * daily_volatility_stock
    annual_volatility_stock = math.sqrt(252) * daily_volatility_stock
    return (annual_volatility_stock)


def drift():
    returns_train = stock_train["Adj Close"].pct_change().dropna()
    return (returns_train.mean())
# -----------------------------------------------------------------------
# Partie 3: Simulations à comparer avec les données historiques d'une action


# Initialisation des paramètres pour les simulations

S0 = stock_train["Adj Close"][0]  # initial stock price
r = 0.05  # risk-free interest rate
sigma = volatility()   # volatility in market
mu = drift()  # drift
T = 1  # time in years
# number of steps within each simulation
#N_total = stock_total["Adj Close"].index.size
N_total = dates_stock_total.size
#N_train = stock_train["Adj Close"].index.size
N_train = dates_stock_train.size
deltat = T/N_train  # time step
i = 10000  # number of simulations
discount_factor = np.exp(-r*T)  # discount factor


# Simulations with GBM using the parameters
S = np.zeros([N_total, i])
stock_array = pd.DataFrame(stock_train).to_numpy()

for y in range(0, i):
    S[0, y] = S0
    for x in range(0, N_total - 1):
        S[x+1, y] = S[x, y]*(np.exp((mu-(sigma**2)/2)*deltat +
                             sigma*np.random.normal(0, np.sqrt(deltat))))
    #plt.plot(year_dates_stock, S[:, y])

# Plotting the simulation with minimal MAPE

min_mape = np.mean(np.abs(
    (stock_train["Adj Close"] - S[0:N_train-1, 0])/stock_train["Adj Close"]))*100
for y in range(1, i):
    mape = np.mean(np.abs(
        (stock_train["Adj Close"] - S[0:N_train-1, y])/stock_train["Adj Close"]))*100
    if mape < min_mape:
        min_mape = mape
        S_plot = S[:, y]
# print(min_mape)

# Plotting the simulation(s) graph(s) for the training and testing period
plt.plot(dates_stock_total[: dates_stock_total.size], S_plot)
# Plotting the real stock graph for the trainign and testing period
plt.plot(stock_train["Adj Close"], "black")
# Adding a vertical line between the trainign and testing period
plt.axvline(x=dates_stock_train[-1], color='red', linestyle='--')
# Adding title and showing the result
plt.xlabel('Time')
plt.ylabel('Stock Price')
plt.show()


# Calculating and plottingthe "mean of the simulations"
'''Smoy = np.sum(S, axis=1)/i
plt.plot(year_dates_stock, Smoy)
plt.plot(stock_test["Adj Close"], "black")
plt.xlabel('Time')
plt.ylabel('Stock Price')
plt.show()'''

# -----------------------------------------------------------------------
# Espace de travail


# Jusqu'ou on peut prédire ; faire varier les parametres en faisant les simulations ; faire la différence autrement que l'EQM
# Bien deéfinir "l'accuracy" et justifier le choix
