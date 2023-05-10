import yfinance as yf
from flask import Flask, request, render_template
import subprocess
import plotly.offline as pyo
import plotly.graph_objs as go
from plotly.offline import plot, iplot
import plotly
import plotly_resampler as FigureResampler
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import math
import scipy
from scipy.stats import norm
import numpy as np
import pandas_market_calendars as mcal
from datetime import timedelta, datetime

# ---------------------------------------------------------------
import datetime
auj = datetime.date.today()


app = Flask(__name__)


@app.route('/')
def home():
    php_output = subprocess.check_output(
        ['php', './theoleboss.php'])
    return php_output


@app.route('/result', methods=['POST'])
def result():
    ticker = request.form['inputValue']
    start_day_train = '2015-01-01'
    start_day_brownian = '2023-01-01'
    end_day_train = auj
    end_day_pred = "2023-06-01"

    # Période pour laquelle on telecharge tourtes les données jusqu'à aujourdhui
    stock = yf.download(ticker, start_day_train, end_day_train)
    # Période pour laquelle on telecharge les données d'entrainement
    stock_total = yf.download(ticker, start_day_brownian, end_day_train)
    # Pour avoir les dates futures d'ouverture du marché
    nyse = mcal.get_calendar('NYSE')
    dates_stock_total = nyse.schedule(
        start_date=start_day_brownian, end_date=end_day_pred).index
    dates_pred = [date.strftime('%Y-%m-%d') for date in dates_stock_total]
###################################################################################
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
        (stock_total["Close"] - S[0:N_train-1, 0])/stock_total["Close"]))*100
    for y in range(1, i):
        mape = np.mean(np.abs(
            (stock_total["Close"] - S[0:N_train-1, y])/stock_total["Close"]))*100
        if mape < min_mape:
            min_mape = mape
            S_plot = S[:, y]
#########################################################################

    values = stock.iloc[:, 4]
    op = stock.iloc[:, 0]
    hi = stock.iloc[:, 1]
    lo = stock.iloc[:, 2]
    cl = stock.iloc[:, 3]
    # SMA
    stock['ewma'] = stock['Close'].ewm(span=30).mean()
    # Bollinger Bands
    stock['bollinger_up'] = cl.rolling(20).mean() + cl.rolling(20).std() * 2
    stock['bollinger_down'] = cl.rolling(20).mean() - cl.rolling(20).std() * 2
    # RSI
    change = cl.diff()
    change.dropna(inplace=True)
    change_up = change.copy()
    change_down = change.copy()
    change_up[change_up < 0] = 0
    change_down[change_down > 0] = 0
    stock['rsi'] = 100 * change_up.rolling(14).mean() / (
        change_up.rolling(14).mean() + change_down.rolling(14).mean().abs())
    # MACD
    exp1 = cl.ewm(span=12, adjust=False).mean()
    exp2 = cl.ewm(span=26, adjust=False).mean()
    stock["macd"] = exp1 - exp2
    stock['signal'] = stock['macd'].ewm(span=9, adjust=False).mean()
    stock["hist"] = stock['macd'] - stock['signal']
    # SO
    stock["highroll"] = hi.rolling(14).max()
    stock["lowroll"] = lo.rolling(14).min()
    stock["%K"] = ((cl - stock['lowroll']) /
                   (stock['highroll']-stock['lowroll'])) * 100
    stock["%D"] = stock["%K"].rolling(3).mean()

    # Dates
    date = stock.index[0:len(values)]

    ordo = open("./templates/ordo.txt", "w")
    absi = open("./templates/absi.txt", "w")
    absi_pred = open("./templates/absi_pred.txt", "w")
    ope = open("./templates/open.txt", "w")
    close = open("./templates/close.txt", "w")
    low = open("./templates/low.txt", "w")
    high = open("./templates/high.txt", "w")
    ewma = open("./templates/ewma.txt", "w")
    bolup = open("./templates/bolup.txt", "w")
    boldown = open("./templates/boldown.txt", "w")
    rsi = open("./templates/rsi.txt", "w")
    macd = open("./templates/macd.txt", "w")
    signal = open("./templates/signal.txt", "w")
    hist = open("./templates/hist.txt", "w")
    fastso = open("./templates/fastso.txt", "w")
    slowso = open("./templates/slowso.txt", "w")
    brownian = open("./templates/brownian.txt", "w")
    for i in range(len(dates_pred)):
        absi_pred.write(dates_pred[i]+'\n')
    for i in range(len(values)):
        newo = str(values[i])
        newop = str(op[i])
        newhi = str(hi[i])
        newlo = str(lo[i])
        newcl = str(cl[i])
        newewma = str(stock["ewma"][i])
        newbolup = str(stock['bollinger_up'][i])
        newboldown = str(stock['bollinger_down'][i])
        newrsi = str(stock['rsi'][i])
        newmacd = str(stock['macd'][i])
        newsignal = str(stock['signal'][i])
        newhist = str(stock['hist'][i])
        newfastso = str(stock['%K'][i])
        newslowso = str(stock['%D'][i])
        if i < S_plot.size:
            newbrownian = str(S_plot[i])
            brownian.write(newbrownian+'\n')
        newa = str(date[i]).split()[0]
        ordo.write(newo+'\n')
        ope.write(newop+'\n')
        close.write(newcl+'\n')
        low.write(newlo+'\n')
        high.write(newhi+'\n')
        absi.write(newa+'\n')
        ewma.write(newewma+'\n')
        bolup.write(newbolup+'\n')
        boldown.write(newboldown+'\n')
        rsi.write(newrsi+'\n')
        macd.write(newmacd+'\n')
        signal.write(newsignal+'\n')
        hist.write(newhist+'\n')
        fastso.write(newfastso+'\n')
        slowso.write(newslowso+'\n')
    ordo.close()
    ope.close()
    high.close()
    low.close()
    close.close()
    absi.close()
    absi_pred.close()
    ewma.close()
    bolup.close()
    boldown.close()
    rsi.close()
    macd.close()
    signal.close()
    hist.close()
    fastso.close()
    slowso.close()
    brownian.close()
    php_output = subprocess.check_output(
        ['php', './theoleboss.php'])
    return php_output


if __name__ == '__main__':
    app.run(debug=True)
