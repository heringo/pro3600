from typing import Iterable

import numpy as np
import statistics as stat
import yfinance as yf
import math

import datetime

AUJ = datetime.date.today()

def centered(x: Iterable[float]) -> Iterable[float]:
    """ This function returns the vector x appropriately centered.

    Args:
        x (Iterable[float]): list of daily closde price

    Returns:
        Iterable[float]: list of daily closed price centered
    """
    return x - np.mean(x)


def compute_sigma(x: Iterable[float]) -> float:
    """ This function computes the sigma which is standard deviation (écart-type)

    Args:
        x (Iterable[float]): list of daily closed price centered

    Returns:
        float: Standard deviation (écart-type)
    """
    T = len(x)
    s2 = np.square(x).sum()
    return math.sqrt(s2 / (T - 1))


def compute_kurtosis(x: Iterable[float]) -> float :
    """ This function compute the kurtosis (coefficient d'applatissement). 
    Kurtosis, also known as the kurtosis coefficient, is a statistical measure that evaluates the shape of the distribution of a dataset. 
    It indicates how much the distribution deviates from a normal distribution (bell-shaped).

    Args:
        x (Iterable[float]): list of daily closed price centered

    Returns:
        float: kurtosis
    """
    T = x.shape[0]
    s2 = np.square(x).sum()
    s4 = np.square(x**2).sum()
    sigma2 = s2 / (T - 1)
    return s4 / sigma2**2 * T*(T+1) / (T-1) / (T-2) / (T-3) - 3. * (T-1)**2 / (T-2) / (T-3)


def compute_autocorrelation(x: Iterable[float], lag: int) -> float:
    """ This function compute the autocorrelation with a lag.
    The autocorrelation coefficient, also known as autocorrelation, measures the correlation between a dataset and itself shifted over time. 
    It is used to detect periodic patterns or dependencies in a time series.

    Args:
        x (Iterable[float]): list of daily closed price centered
        lag (int): the lag indicates the number of periods or time intervals by which the series is shifted

    Returns:
        float: autocorrelation coefficient
    """
    length = x.shape[0] - lag
    s2 = np.square(x).sum()
    return np.dot(x[:length], x[lag:]) / s2


def compute_autocorrelation_squares(x: Iterable[float], lag: int) -> float :
    """ This function compute autocorrelation squares.
    It's the same thing as autocorrelation but we considered the sqaure of x

    Args:
        x (Iterable[float]): list of daily closed price centered
        lag (int): the lag indicates the number of periods or time intervals by which the series is shifted

    Returns:
        float: autocorrelation square
    """
    squares = x**2
    centered_squares = squares - stat.mean(squares)
    length = x.shape[0] - lag
    s2 = np.square(centered_squares).sum()
    return np.dot(centered_squares[:length], centered_squares[lag:]) / s2


def get_returns(ticker: str) -> Iterable[float]:
    """ This function extract the list of daily closed price of 'ticker' from yfinance

    Args:
        ticker (str): ticker from yfinance

    Returns:
        Iterable[float]: list of daily closed price
    """
    # Define the ticker list
    tickers_list = ticker

    # Extract the necessary data
    start_day = "2022-01-01"
    end_day = f"{AUJ}"

    tickerData = yf.Ticker(tickers_list)
    tickerDf = tickerData.history(period='1d', start=start_day, end=end_day)
    dailyClose = tickerDf['Close'].tolist()
    return np.array(dailyClose)
    