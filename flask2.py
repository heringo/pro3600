from flask import Flask, redirect, url_for, render_template, request
#import plotly.graph_objs as go
from plotly.offline import plot, iplot
#import plotly
#import plotly_resampler as FigureResampler
import pandas as pd
#import matplotlib.pyplot as plt
import yfinance as yf
import math
#import scipy
from scipy.stats import norm
import numpy as np
import pandas_market_calendars as mcal
from datetime import timedelta, datetime

# ---------------------------------------------------------------


def brownian(ticker):

    # Define the ticker list

    # Extract the necessary data
    start_day_train = "2023-01-02"
    end_day_train = "2023-04-05"
    end_day_test = "2023-04-17"

    stock_train = yf.download(ticker, start_day_train, end_day_train)
    #stock_test = yf.download(ticker, start_day_test, end_day_test)
    #stock_total = yf.download(ticker, start_day_train, end_day_test)

    nyse = mcal.get_calendar('NYSE')
    dates_stock_train = nyse.schedule(
        start_date=start_day_train, end_date=end_day_train).index
    dates_stock_total = nyse.schedule(
        start_date=start_day_train, end_date=end_day_test).index
    # dates_stock_test = nyse.schedule(
    # start_date=start_day_test, end_date=end_day_test).index

    stock_train['Daily Return'] = stock_train['Close'].pct_change(1)
    daily_volatility_stock = stock_train['Daily Return'].std()
    #monthly_volatility_stock = math.sqrt(21) * daily_volatility_stock
    annual_volatility_stock = math.sqrt(252) * daily_volatility_stock
    volatility = annual_volatility_stock

    returns_train = stock_train["Close"].pct_change().dropna()
    drift = returns_train.mean()

    S0 = stock_train["Close"][0]  # initial stock price
    # r = 0.05  # risk-free interest rate
    sigma = volatility   # volatility in market
    mu = drift  # drift
    T = 1  # time in years
    # number of steps within each simulation
    # N_total = stock_total["Adj Close"].index.size
    N_total = dates_stock_total.size
    # N_train = stock_train["Adj Close"].index.size
    N_train = dates_stock_train.size
    deltat = T/N_train  # time step
    i = 1000  # number of simulations

    # Simulations with GBM using the parameters
    S = np.zeros([N_total, i])
    stock_array = pd.DataFrame(stock_train).to_numpy()

    for y in range(0, i):
        S[0, y] = S0
        for x in range(0, N_total - 1):
            S[x+1, y] = S[x, y]*(np.exp((mu-(sigma**2)/2)*deltat +
                                        sigma*np.random.normal(0, np.sqrt(deltat))))

    # Plotting the simulation with minimal MAPE

    min_mape = np.mean(np.abs(
        (stock_train["Close"] - S[0:N_train-1, 0])/stock_train["Close"]))*100
    for y in range(1, i):
        mape = np.mean(np.abs(
            (stock_train["Close"] - S[0:N_train-1, y])/stock_train["Close"]))*100
        if mape < min_mape:
            min_mape = mape
            S_plot = S[:, y]

    # Creating a trace for the `S_plot` data
    trace1 = {
        'x': dates_stock_total,
        'y': S_plot,
        'name': 'Brownian Simulation',
        'type': 'scatter'
    }

    # Creating a trace for the `stock_train["Adj Close"]` data
    trace2 = {
        'x': dates_stock_total,
        'y': stock_train["Close"],
        'name': 'Closing Price',
        'type': 'scatter'
    }

    # Creating a layout for the plot
    layout = {
        'title': {'text': ticker + ' Stock Price Simulation with GMB',
                  'x': 0.5,
                  'y': 0.9,
                  'xanchor': 'center',
                  'yanchor': 'top'},
        'xaxis': {'title': 'Date'},
        'yaxis': {'title': 'Close Price'}
    }

    # Creating the figure and plotting the data
    fig = {'data': [trace1, trace2], 'layout': layout}
    #html_content = plot(fig, output_type='div')
    #file_path = 'CS/Python/templates/tim_graph.html'

    """with open(file_path, 'w') as f:
        f.write(html_content)"""
    return S_plot, stock_train["Close"], dates_stock_total

# -----------------------------------------------------------------


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        stock = request.form["searchInput"]
        return redirect(url_for("stock_graph", st=stock))
    else:
        return render_template("tim.html")


@app.route("/<st>", methods=["POST", "GET"])
def stock_graph(st):
    a, b, c = brownian(st)
    return render_template("tim_graph.html")


if __name__ == "__main__":
    app.run(debug=True)
