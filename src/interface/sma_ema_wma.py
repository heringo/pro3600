import numpy as np
import pandas as pd
import pandas_datareader as pdr
import matplotlib.pyplot as plt
import yfinance as yf

# Calcul du SMA (Simple Moving Average)


def get_sma(prices, rate):
    return prices.rolling(rate).mean()


ticker = 'AAPL'
start_day_train = "2022-10-01"
end_day_train = "2023-03-15"
start_day_test = "2023-03-15"
end_day_test = "2023-04-10"
stock = yf.download(ticker, start_day_train, end_day_test)

closing_prices = stock['Close']  # Use only closing prices

sma = get_sma(closing_prices, 20)  # Get 20 day SMA

# Calcul du EMA (Exponantial Moving Average)
stock['EWMA30'] = stock['Close'].ewm(span=30).mean()

# Calcul du WMA (Weighted Moving Average)
weights = np.arange(1, 11)
wma10 = stock['Close'].rolling(10).apply(
    lambda prices: np.dot(prices, weights)/weights.sum(), raw=True)
sma10 = stock['Close'].rolling(10).mean()

# Plot the data
plt.title(ticker + 'SMA, EMA, WMA')
plt.xlabel('Days')
plt.ylabel('Closing Prices')
plt.plot(closing_prices, label='Closing Prices')
plt.plot(sma, label='20-Day SMA')
plt.plot(stock['EWMA30'], label='EMA')
plt.plot(wma10, label="10-Day WMA")
plt.legend()
plt.show()
