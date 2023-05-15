## What is it?

In finance, **agent-based modeling (ABM)** is an approach that allows modeling and simulating financial markets using a representation in the form of a population of individual agents. Each agent in the agent-based model has its own behavior, investment strategy, and can be influenced by the actions and opinions of other agents.

In the specific context of modeling stock prices, ABM can be used to simulate the price dynamics of financial assets such as stocks. In an agent-based model of stock prices, each agent represents an investor who makes buying or selling decisions based on their own rules and strategies.

One of the key features of ABM is the propagation of opinion or influence between agents. This means that the actions and decisions of one agent can influence other agents, creating a network effect or spread of opinions. For example, if a group of agents starts buying a particular stock, it can influence other agents to follow suit and buy as well, leading to an increase in the stock price.

Agent-based models allow for exploring the complex dynamics and emergent phenomena that can occur in financial markets, such as the formation of investor clusters or the propagation of opinions within the population of agents.

It is important to note that agent-based models are simplifications of reality and rely on specific assumptions and parameters. The results obtained from these models can provide useful insights and perspectives on collective behaviors and variations in stock prices, but they do not represent a precise prediction of the actual market.

## Where to get it ?

The source code is currently hosted on GitHub at: [https://github.com/heringo/pro3600](https://github.com/heringo/pro3600)

## Required installations

Import the following libraries :

```python
pip install typing
pip install numpy
pip install statistics
pip install yfinance
pip install math 
pip install datetime
pip install scipy
pip install concurrent
pip install queue
pip install threading
```

## How to use it ? 

Choose your ticker on main.py and run main.py

'''python
python3 main.py
'''

## Dependencies

- [NumPy - Adds support for large, multi-dimensional arrays, matrices and high-level mathematical functions to operate on these arrays](https://www.numpy.org/)
- [python-datetime - Provides powerful extensions to the standard datetime module](https://dateutil.readthedocs.io/en/stable/index.html)
- [YahooFinance-Provides stock data from Yahoo! Finance’s API.](https://pypi.org/project/yfinance/)
- [Scipy-Provides modules for statistics, optimization, integration, linear algebra, Fourier transforms, signal and image processing, ODE solvers, and more.](https://pypi.org/project/scipy/)


## License

No license for now.

## Getting Help

For usage questions, the best place to go to is [StackOverflow](https://stackoverflow.com/questions). Further, general questions and discussions can also be written to our email adress FiNanCe@gmail.com.

## Development

Most development discussions take place on GitHub in this repo. Furthermore, we are available through our personal mails : henri.ngo@telecom-sudparis.eu feel free to email us for any development discussions.
