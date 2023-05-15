## What is it?

In finance, **neuralnetworks modeling (NNM)** is an approach that allows modeling and simulating financial markets using CNN (**ConvolutionalNeuralNetwork)**. CNNs use a mathematical operation called [convolution](https://en.wikipedia.org/wiki/Convolution) in place of general matrix multiplication in at least one of their layers. When adding an LSTM(LongShortTermMemory) layer, the neural network becomes more apt at forecasting time series data like the stock market which are non-linear. 

In our case we used NeuralProphet from Facebook to evaluate the stock market prices by finding the solution of a ‘fitting the curve problem’ with this equation representing yhat (the forecast)of y (the stock market prices) :

<img width="967" alt="image" src="https://github.com/heringo/pro3600/assets/121232962/e2f56741-ebc1-4518-a4b4-ca70259477c4">

<img width="1008" alt="image" src="https://github.com/heringo/pro3600/assets/121232962/fa9e61dd-6310-4b7e-b08c-b35986017ae6">


For further explanation on the Neural prophet model please visit the NeuralProphet paper : [NeuralPaper](https://arxiv.org/pdf/2111.15397.pdf). 

In the specific context of modeling stock prices, NeuralProphet can be used to estimate the price dynamics of financial assets such as stocks. The additive components Trend, Seasonality, Events, AutoRegression correlated with a neural network (that tries to learn the patterns of the stock)make an estimation of the prices and try to forecast them in the future.

Furthermore, the NeuralProphet model allows for exploring many features to modify the models according to your needs. The main complexity is finding the hyperparameters that will fit the best the stock. Accuracy can vary from a stock to another, we would need to study more deeply the volatility to provide for better and more accurate models as prices aren’t the only features in financial markets.

It is important to note that the NeuralProphet model  is a simplified version of reality and rely on specific assumptions and parameters(does not take into account the events unless told and relies on the constant feeding of information). The results obtained from these models can provide useful insights and perspectives on variations in stock prices, but they do not represent a precise prediction of the actual market.

## Where to get it ?

The source code is currently hosted on GitHub at: [https://github.com/heringo/pro3600](https://github.com/heringo/pro3600)

## Required installations

Import the following libraries :

```
pip install pandas
pip install yfinance
pip install neuralProphet
pip install pandas_datareader
pip install numpy
pip install matplotlib
pip install plotly
pip install plotly_resampler
pip install datetime

```

## How to use it ?

Choose your ticker, your forecast_period, and the number of years you want the model to be trained on,  on [main.py](http://main.py/) and run [main.py](http://main.py/)

'''python
python3 [main.py](http://main.py/)
'''

## Dependencies

- [NumPy - Adds support for large, multi-dimensional arrays, matrices and high-level mathematical functions to operate on these arrays](https://www.numpy.org/)
- [python-datetime - Provides powerful extensions to the standard datetime module](https://dateutil.readthedocs.io/en/stable/index.html)
- [PyTorch-Provides powerful two high-level features: Tensor computation (like NumPy) with strong GPU acceleration and deep neural networks built on a tape-based autograd system.](https://pytorch.org/)
- [NeuralProphet - Provides framework for interpretable time series forecasting(built on top of FB’ Prophet Model).](https://pypi.org/project/neuralprophet/)
- [Pandas- Provides fast, flexible, and expressive data structures designed to make working with "relational" or "labeled" data both easy and intuitive.](https://pandas.pydata.org/)
- [YahooFinance-Provides stock data from Yahoo! Finance’s API.](https://pypi.org/project/yfinance/)
- [Plotly-Provides an interactive, open-source, and browser-based graphing library.](https://pypi.org/project/plotly/)
- [Matplotlib-Provides a comprehensive library for creating static, animated, and interactive visualizations in Python.](https://pypi.org/project/matplotlib/)

## License

No license for now.

## Getting Help

For usage questions, the best place to go to is [StackOverflow](https://stackoverflow.com/questions). Further, general questions and discussions can also be written to our email adress [FiNanCe@gmail.com](mailto:FiNanCe@gmail.com).

## Development

Most development discussions take place on GitHub in this repo. Furthermore, I’m available through my personal mail :  [theo.niemann@telecom-sudparis.eu](mailto:theo.niemann@telecom-sudparis.eu) feel free to email me for any development discussions.
