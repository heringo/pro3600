## What is it?

**pro3600** is an interactive graphic user interface that provides fast, flexible, and expressive financial features and models forecasting on closing prices of the stock market. It aims to help the consumer get an idea on the market by evaluating its state with three different approach robust models : a Geometric Brownian Motion Model, a NeuralNetwork model provided by NeuralProphet and an Agent Based Model. It also offers practical technical analysis tools and dynamic visualization through plotly.

## Main Features

Here are just a few of the things that we provide :

- Easy search and plot of yfinance stock provided by the API
- Three Robust Models aimed to forecast the stock market.
- Various technical analysis tools like MACD or RSI.
- Display of daily Volume Trades using calculations from the Agent Based Model
- Easy to use GUI with buttons
- Other interesting statistic tools

## Where to get it ?

The source code is currently hosted on GitHub at: [https://github.com/heringo/pro3600](https://github.com/heringo/pro3600)

## Required installations

Import the following libraries :

```python
pip install pandas
pip install yfinance
pip install flask
pip install neuralProphet
pip install scipy 
pip install pandas_datareader
pip install numpy
pip install matplotlib
pip install plotly
pip install plotly_resampler
pip install datetime
pip install pandas_market_calendars
pip install subprocess
pip install typing
pip install itertools
```

## Dependencies

- [NumPy - Adds support for large, multi-dimensional arrays, matrices and high-level mathematical functions to operate on these arrays](https://www.numpy.org/)
- [python-datetime - Provides powerful extensions to the standard datetime module](https://dateutil.readthedocs.io/en/stable/index.html)
- [PyTorch-Provides powerful two high-level features: Tensor computation (like NumPy) with strong GPU acceleration and deep neural networks built on a tape-based autograd system.](https://pytorch.org/)
- [NeuralProphet - Provides framework for interpretable time series forecasting(built on top of FB’ Prophet Model).](https://pypi.org/project/neuralprophet/)
- [Pandas- Provides fast, flexible, and expressive data structures designed to make working with "relational" or "labeled" data both easy and intuitive.](https://pandas.pydata.org/)
- [YahooFinance-Provides stock data from Yahoo! Finance’s API.](https://pypi.org/project/yfinance/)
- [Flask-Provides a lightweight WSGI web application framework.](https://pypi.org/project/Flask/)
- [Scipy-Provides modules for statistics, optimization, integration, linear algebra, Fourier transforms, signal and image processing, ODE solvers, and more.](https://pypi.org/project/scipy/)
- [Plotly-Provides an interactive, open-source, and browser-based graphing library.](https://pypi.org/project/plotly/)
- [Matplotlib-Provides a comprehensive library for creating static, animated, and interactive visualizations in Python.](https://pypi.org/project/matplotlib/)

License

No license for now.

## Background

Work that started on tktinterin 2022 but that has been extended to Javascript, html and php to provide an extensive GUI for financial forecasts to give the user forecasts in minutes hours but also days and weeks

## Getting Help

For usage questions, the best place to go to is [StackOverflow](https://stackoverflow.com/questions/tagged/pandas). Further, general questions and discussions can also be written to our email adress FiNanCe@gmail.com.

## Development

Most development discussions take place on GitHub in this repo. Furthermore, we are available through our personal mails : henri.ngo@telecom-sudparis.eu / timothee.badiche@telecom-sudparis.eu / valentin.six@telecom-sudparis.eu / theo.niemann@telecom-sudparis.eu feel free to email us for any development discussions.
