import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime

# Load the data into a dataframe
ticker = ['AAPL']
#stock = ticker.history(interval="1d", period="max")
start_day_train = "2022-10-01"
end_day_train = "2023-03-15"
start_day_test = "2023-03-15"
end_day_test = "2023-04-10"

# -----------------------------------------------------------
# Calcul du RSI

# Filter the data by date
stock = yf.download(ticker, start_day_train, end_day_test)

change = stock["Close"].diff()
change.dropna(inplace=True)

# Create two copies of the Closing price Series
change_up = change.copy()
change_down = change.copy()
change_up[change_up < 0] = 0
change_down[change_down > 0] = 0

# Verify that we did not make any mistakes
change.equals(change_up+change_down)

# Calculate the rolling average of average up and average down
avg_up = change_up.rolling(14).mean()
avg_down = change_down.rolling(14).mean().abs()

rsi = 100 * avg_up / (avg_up + avg_down)

# Set the theme of our chart
plt.style.use('fivethirtyeight')

# Make our resulting figure much bigger
#plt.rcParams['figure.figsize'] = (20, 20)

# Create two charts on the same figure.
ax1 = plt.subplot2grid((10, 1), (0, 0), rowspan=4, colspan=1)
ax2 = plt.subplot2grid((10, 1), (5, 0), rowspan=4, colspan=1)

# First chart:
# Plot the closing price on the first chart
ax1.plot(stock['Close'], linewidth=1)
ax1.set_title('Close Price')

# Second chart :
# Plot the RSI
ax2.set_title('Relative Strength Index')
ax2.plot(rsi, color='orange', linewidth=1)
# Add two horizontal lines, signalling the buy and sell ranges.
# Oversold
ax2.axhline(30, linestyle='--', linewidth=1.5, color='green')
# Overbought
ax2.axhline(70, linestyle='--', linewidth=1.5, color='red')
plt.show()
