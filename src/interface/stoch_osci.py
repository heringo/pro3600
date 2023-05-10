
import datetime
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf

ticker = ['AAPL']
start_day_train = "2022-10-01"
end_day_train = "2023-03-15"
start_day_test = "2023-03-15"
end_day_test = "2023-04-10"
stock = yf.download(ticker, start_day_train, end_day_test)


def add_stochastic_oscillator(df, periods=14):
    copy = df.copy()

    high_roll = copy["High"].rolling(periods).max()
    low_roll = copy["Low"].rolling(periods).min()

    # Fast stochastic indicator
    num = copy["Close"] - low_roll
    denom = high_roll - low_roll
    copy["%K"] = (num / denom) * 100

    # Slow stochastic indicator
    copy["%D"] = copy["%K"].rolling(3).mean()

    return copy


stock_copy = add_stochastic_oscillator(stock)


today = datetime.datetime.now()

date_pattern = "%Y-%m-%d"
today_str = today.strftime(date_pattern)
date_ranges = {
    "1M": (today - datetime.timedelta(days=30)).strftime(date_pattern),
    "3M": (today - datetime.timedelta(days=90)).strftime(date_pattern),
    "6M": (today - datetime.timedelta(days=180)).strftime(date_pattern),
    "1Y": (today - datetime.timedelta(days=365)).strftime(date_pattern),
    "2Y": (today - datetime.timedelta(days=2*365)).strftime(date_pattern),
}


def plot_stochastic_oscillator(df, symbol, rng, periods=14):
    start = date_ranges[rng]
    end = today_str
    temp_df = df[start:end]

    fig, ax = plt.subplots(nrows=2, ncols=1, sharex=True,
                           tight_layout=True, figsize=(6, 6))

    ax[0].set_title(f"{symbol} price, {rng}")
    ax[0].plot(temp_df["Close"], color="tab:blue")

    ax[1].set_title(
        f"{symbol} Stochastic Oscillator ({periods}-day period), {rng}")
    ax[1].set_ylim(-10, 110)
    ax[1].plot(temp_df["%K"], color="tab:blue")  # fast
    ax[1].plot(temp_df["%D"], color="tab:orange")  # slow

    ax[1].axhline(80, color="tab:red", ls="--")
    ax[1].axhline(20, color="tab:green", ls="--")

    custom_lines = [
        Line2D([0], [0], color="tab:blue", lw=4),
        Line2D([0], [0], color="tab:orange", lw=4),
        Line2D([0], [0], color="tab:red", lw=4),
        Line2D([0], [0], color="tab:green", lw=4),
    ]
    ax[1].legend(custom_lines, ["%K", "%D",
                 "Overbought", "Oversold"], loc="best")


stock_copy = add_stochastic_oscillator(stock)
plot_stochastic_oscillator(stock_copy, "AAPL", "6M")
plt.show()
