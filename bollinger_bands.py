import numpy as np
import pandas as pd
import pandas_datareader as pdr
import matplotlib.pyplot as plt
import yfinance as yf


def get_sma(prices, rate):
    return prices.rolling(rate).mean()


def get_bollinger_bands(prices, rate=20):
    sma = get_sma(prices, rate)
    std = prices.rolling(rate).std()
    bollinger_up = sma + std * 2  # Calculate top band
    bollinger_down = sma - std * 2  # Calculate bottom band
    return bollinger_up, bollinger_down


ticker = 'AAPL'
start_day_train = "2022-10-01"
end_day_train = "2023-03-15"
start_day_test = "2023-03-15"
end_day_test = "2023-04-10"
stock = yf.download(ticker, start_day_train, end_day_test)

closing_prices = stock['Close']  # Use only closing prices

bollinger_up, bollinger_down = get_bollinger_bands(closing_prices)

plt.title(ticker + ' Bollinger Bands')
plt.xlabel('Days')
plt.ylabel('Closing Prices')
plt.plot(closing_prices, label='Closing Prices')
plt.plot(bollinger_up, label='Bollinger Up', c='g')
plt.plot(bollinger_down, label='Bollinger Down', c='r')
plt.legend()
plt.show()

# ------------------------------------------------------------------------------------------------------------
