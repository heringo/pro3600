## What is it?

Geometric Brownian Motion (GMB) is a stochastic process that describes the random evolution of a variable over time. It is often used to model or predict stock prices due to its ability to capture key characteristics such as continuous price changes and volatility. GBM assumes that the logarithmic returns of an asset follow a normal distribution.

The GBM model is based on the following stochastic differential equation:

dS = μ * S * dt + σ * S * dW

- **`dS`** is the change in the asset price **`S`**
- **`μ`** is the average expected return (also called drift)
- **`dt`** is the infinitesimal time step
- **`σ`** is the standard deviation of the returns (also called volatility)
- **`dW`** is a Wiener process (random variable)

By discretizing the time steps and using numerical methods, it is possible to simulate the future price trajectory of the asset based on the GBM model. 

The GBM model finds wide application in various areas of finance, including:

**Stock Price Forecasting**

By simulating stock price paths using GBM, analysts can estimate the potential future range of stock prices. These simulations assist in risk assessment, option pricing, and portfolio optimization. GBM's ability to capture volatility and mimic real-world price movements makes it a valuable tool for understanding stock market dynamics.

**Option Pricing**

GBM plays a crucial role in option pricing models, such as the Black-Scholes-Merton model. It assumes that the underlying asset follows GBM, allowing the calculation of the fair value of options based on factors like strike price, time to expiration, and volatility. GBM-based simulations enable investors to assess the potential profitability and risk of various option strategies.

It is important to note that the Geometric Brownian Motion model is a simplified version of reality and rely on specific assumptions and parameters(does not take into account the events unless told and relies on the constant feeding of information). The results obtained from these models can provide useful insights and perspectives on variations in stock prices, but they do not represent a precise prediction of the actual market.

If you want additional details on GMB and its uses for stock modelling or stock prediction, we recommand the following pages :

## Where to get it ?

The source code is currently hosted on GitHub at: [https://github.com/heringo/pro3600](https://github.com/heringo/pro3600)

## Required installations

Import the following libraries :

```
pip install pandas
pip install yfinance
pip install numpy
pip install pandas_market_calendars
```

## How to use it ?

Choose your ticker on [brownian.py](http://main.py/) and run [brownian.py](http://main.py/)

'''python
python3 [main.py](http://main.py/)
'''

## Dependencies

- [Pandas Market Calendars - Allows us to get the calendar of the stock market for the futur days](https://pypi.org/project/pandas-market-calendars/)
- [Pandas- Provides fast, flexible, and expressive data structures designed to make working with "relational" or "labeled" data both easy and intuitive.](https://pandas.pydata.org/)
- [YahooFinance-Provides stock data from Yahoo! Finance’s API.](https://pypi.org/project/yfinance/)
- [Numpy - Contains all the basics scientific tools when computing on Python](https://numpy.org)

## License

No license for now.

## Getting Help

For usage questions, the best place to go to is [StackOverflow](https://stackoverflow.com/questions). Further, general questions and discussions can also be written to our email adress [FiNanCe@gmail.com](mailto:FiNanCe@gmail.com).

## Development

Most development discussions take place on GitHub in this repo. Furthermore, I’m available through my personal mail :  [valentin.six@telecom-sudparis.eu](mailto:valentin.six@telecom-sudparis.eu) feel free to email me for any development discussions.
