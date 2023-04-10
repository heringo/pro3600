import requests
import pandas as pd
import numpy as np
from math import floor
from termcolor import colored as cl
import matplotlib.pyplot as plt
import yfinance as yf

plt.rcParams['figure.figsize'] = (20, 10)
plt.style.use('fivethirtyeight')
start_day_train = "2022-10-01"
end_day_train = "2023-03-15"
start_day_test = "2023-03-15"
end_day_test = "2023-04-10"


def get_historical_data(symbol, start_date=None):
    api_key = "F7I1YMRWX50RG48U"
    api_url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={api_key}&outputsize=full'
    raw_df = requests.get(api_url).json()
    df = yf.download(symbol, start_day_train, end_day_test)
    for i in df.columns:
        df[i] = df[i].astype(float)
    df.index = pd.to_datetime(df.index)
    if start_date:
        df = df[df.index >= start_date]
    return df


googl = get_historical_data('AAPL', start_day_train)


def get_macd(price, slow, fast, smooth):
    exp1 = price.ewm(span=fast, adjust=False).mean()
    exp2 = price.ewm(span=slow, adjust=False).mean()
    macd = pd.DataFrame(exp1 - exp2).rename(columns={'Close': 'macd'})
    signal = pd.DataFrame(macd.ewm(span=smooth, adjust=False).mean()).rename(
        columns={'macd': 'signal'})
    hist = pd.DataFrame(macd['macd'] - signal['signal']
                        ).rename(columns={0: 'hist'})
    frames = [macd, signal, hist]
    df = pd.concat(frames, join='inner', axis=1)
    return df


googl_macd = get_macd(googl['Close'], 26, 12, 9)
googl_macd.tail()


def plot_macd(prices, macd, signal, hist):
    ax1 = plt.subplot2grid((8, 1), (0, 0), rowspan=5, colspan=1)
    ax2 = plt.subplot2grid((8, 1), (5, 0), rowspan=3, colspan=1)

    ax1.plot(prices)
    ax2.plot(macd, color='grey', linewidth=1.5, label='MACD')
    ax2.plot(signal, color='skyblue', linewidth=1.5, label='SIGNAL')

    for i in range(len(prices)):
        if str(hist[i])[0] == '-':
            ax2.bar(prices.index[i], hist[i], color='#ef5350')
        else:
            ax2.bar(prices.index[i], hist[i], color='#26a69a')

    plt.legend(loc='lower right')


plot_macd(googl['Close'], googl_macd['macd'],
          googl_macd['signal'], googl_macd['hist'])

plt.show()
