import yfinance as yf
from plotly.offline import plot, iplot
import plotly
import plotly_resampler as FigureResampler
import pandas as pd
#import matplotlib.pyplot as plt
import yfinance as yf
import math

from scipy.stats import norm
import numpy as np
import pandas_market_calendars as mcal
import numpy as np
import pandas as pd 



def brownian(ticker, start_day_train,end_day_train,start_day_brownian,end_day_pred):
    stock = yf.download(ticker, start_day_train, end_day_train)
    # Période pour laquelle on telecharge les données d'entrainement
    stock_total = yf.download(ticker, start_day_brownian, end_day_train)
    # Pour avoir les dates futures d'ouverture du marché
    nyse = mcal.get_calendar('NYSE')
    dates_stock_total = nyse.schedule(
        start_date=start_day_brownian, end_date=end_day_pred).index
    dates_pred = [date.strftime('%Y-%m-%d') for date in dates_stock_total]
    volatility = math.sqrt(252) * stock['Close'].pct_change(1).std()
    drift = stock["Close"].pct_change().dropna().mean()
    S0 = stock_total["Close"][0]
    sigma = volatility
    mu = drift
    T = 1
    N_train = stock_total["Close"].size
    N_total = len(dates_pred)
    deltat = T/N_train
    i = 10000
    S = np.zeros([N_total, i])

    for y in range(0, i):
        S[0, y] = S0
        for x in range(0, N_total - 1):
            S[x+1, y] = S[x, y]*(np.exp((mu-(sigma**2)/2)*deltat +
                                        sigma*np.random.normal(0, np.sqrt(deltat))))

    min_mape = np.mean(np.abs(
        (stock_total["Close"] - S[0:N_train, 0])/stock_total["Close"]))*100
    for y in range(1, i):
        mape = np.mean(np.abs(
            (stock_total["Close"] - S[0:N_train, y])/stock_total["Close"]))*100
        if mape < min_mape:
            min_mape = mape
            S_plot = S[:, y]
    return (S_plot,stock,dates_pred)
