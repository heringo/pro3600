import yfinance as yf
from flask import Flask, request, render_template
import subprocess
#import plotly.offline as pyo
#import plotly.graph_objs as go
from plotly.offline import plot, iplot
import plotly
import plotly_resampler as FigureResampler
import pandas as pd
#import matplotlib.pyplot as plt
import yfinance as yf
import math
#import scipy
from scipy.stats import norm
import numpy as np
import pandas_market_calendars as mcal
from datetime import timedelta, datetime
import requests
import datetime
from neuralprophet import NeuralProphet
import numpy as np
import pandas as pd 
import yfinance as yf
import matplotlib.pyplot as plt 
import plotly
from pandas_datareader import data as pdr
import plotly_resampler
from dateutil.relativedelta import relativedelta
import importlib
from yahoo_fin import stock_info as si
# ---------------------------------------------------------------

auj = datetime.date.today()


app = Flask(__name__)


@app.route('/')
def home():
    php_output = subprocess.check_output(
        ['php', './templates/interface_tim.php'])
    return php_output


@app.route('/result', methods=['POST'])
def result():
    # On vérifie que le ticker existe bien
    ticker = request.form['inputValue']
    check = yf.Ticker(ticker)
    if check.history().empty:
        error_message = "Le ticker '{}' n'existe pas.".format(ticker)
        return render_template('erreur.html', ticker=ticker)
    # On fixe les dates d'import des données et de prédiction
    start_day_train = '2015-01-01'
    start_day_brownian = auj - datetime.timedelta(days=365)
    end_day_train = auj
    end_day_pred = auj + datetime.timedelta(days=2*30)


    #Modèle brownien
    brownian_function = importlib.import_module('brownian_function')
    S_plot,stock,dates_pred = brownian_function.brownian(ticker, start_day_train,end_day_train,start_day_brownian,end_day_pred)
    
    #Modèle NeuralProphet
    neural_function = importlib.import_module('neural_function')
    neural, neural_dates = neural_function.neural(ticker)

    #Modèle Agent
    agent_function = importlib.import_module('agent_function')
    agent_function.main(ticker)
    
    #Formatation des données et écriture dans des fichiers txt

    values = stock.iloc[:, 4]
    op = stock.iloc[:, 0]
    hi = stock.iloc[:, 1]
    lo = stock.iloc[:, 2]
    cl = stock.iloc[:, 3]
    # SMA
    stock['ewma'] = stock['Close'].ewm(span=30).mean()
    # Bollinger Bands
    stock['bollinger_up'] = cl.rolling(20).mean() + cl.rolling(20).std() * 2
    stock['bollinger_down'] = cl.rolling(20).mean() - cl.rolling(20).std() * 2
    # RSI
    change = cl.diff()
    change.dropna(inplace=True)
    change_up = change.copy()
    change_down = change.copy()
    change_up[change_up < 0] = 0
    change_down[change_down > 0] = 0
    stock['rsi'] = 100 * change_up.rolling(14).mean() / (
        change_up.rolling(14).mean() + change_down.rolling(14).mean().abs())
    # MACD
    exp1 = cl.ewm(span=12, adjust=False).mean()
    exp2 = cl.ewm(span=26, adjust=False).mean()
    stock["macd"] = exp1 - exp2
    stock['signal'] = stock['macd'].ewm(span=9, adjust=False).mean()
    stock["hist"] = stock['macd'] - stock['signal']
    # SO
    stock["highroll"] = hi.rolling(14).max()
    stock["lowroll"] = lo.rolling(14).min()
    stock["%K"] = ((cl - stock['lowroll']) /
                   (stock['highroll']-stock['lowroll'])) * 100
    stock["%D"] = stock["%K"].rolling(3).mean()

    # Dates
    date = stock.index[0:len(values)]

    ordo = open("./templates/ordo.txt", "w")
    absi = open("./templates/absi.txt", "w")
    absi_pred = open("./templates/absi_pred.txt", "w")
    absi_neural = open("./templates/absi_neural.txt", "w")
    ope = open("./templates/open.txt", "w")
    close = open("./templates/close.txt", "w")
    low = open("./templates/low.txt", "w")
    high = open("./templates/high.txt", "w")
    ewma = open("./templates/ewma.txt", "w")
    bolup = open("./templates/bolup.txt", "w")
    boldown = open("./templates/boldown.txt", "w")
    rsi = open("./templates/rsi.txt", "w")
    macd = open("./templates/macd.txt", "w")
    signal = open("./templates/signal.txt", "w")
    hist = open("./templates/hist.txt", "w")
    fastso = open("./templates/fastso.txt", "w")
    slowso = open("./templates/slowso.txt", "w")
    brownian = open("./templates/brownian.txt", "w")
    neuralprophet = open("./templates/neuralprophet.txt", "w")
    for i in range(len(neural_dates)):
        absi_neural.write(neural_dates[i]+'\n')
    for i in range(len(dates_pred)):
        absi_pred.write(dates_pred[i]+'\n')
    for i in range(len(values)):
        newo = str(values[i])
        newop = str(op[i])
        newhi = str(hi[i])
        newlo = str(lo[i])
        newcl = str(cl[i])
        newewma = str(stock["ewma"][i])
        newbolup = str(stock['bollinger_up'][i])
        newboldown = str(stock['bollinger_down'][i])
        newrsi = str(stock['rsi'][i])
        newmacd = str(stock['macd'][i])
        newsignal = str(stock['signal'][i])
        newhist = str(stock['hist'][i])
        newfastso = str(stock['%K'][i])
        newslowso = str(stock['%D'][i])
        if i < S_plot.size:
            newbrownian = str(S_plot[i])
            brownian.write(newbrownian+'\n')
        if i < neural.size:
            newneural = str(neural[i])
            neuralprophet.write(newneural+'\n')
        newa = str(date[i]).split()[0]
        ordo.write(newo+'\n')
        ope.write(newop+'\n')
        close.write(newcl+'\n')
        low.write(newlo+'\n')
        high.write(newhi+'\n')
        absi.write(newa+'\n')
        ewma.write(newewma+'\n')
        bolup.write(newbolup+'\n')
        boldown.write(newboldown+'\n')
        rsi.write(newrsi+'\n')
        macd.write(newmacd+'\n')
        signal.write(newsignal+'\n')
        hist.write(newhist+'\n')
        fastso.write(newfastso+'\n')
        slowso.write(newslowso+'\n')
    ordo.close()
    ope.close()
    high.close()
    low.close()
    close.close()
    absi.close()
    absi_pred.close()
    ewma.close()
    bolup.close()
    boldown.close()
    rsi.close()
    macd.close()
    signal.close()
    hist.close()
    fastso.close()
    slowso.close()
    brownian.close()
    neuralprophet.close()
    absi_neural.close()

    absi = open("./templates/rabsi.txt", "w")
    ope = open("./templates/ropen.txt", "w")
    close = open("./templates/rclose.txt", "w")
    low = open("./templates/rlow.txt", "w")
    high = open("./templates/rhigh.txt", "w")
    '''for i in range(5) :
        deb=fin - datetime.timedelta(days=4)
        stock_data = si.get_data(ticker, start_date=deb, end_date=fin, interval='1m')
        L.append(stock_data)
        fin=deb - datetime.timedelta(days=1)'''
    stock_data = si.get_data(ticker, start_date=auj - datetime.timedelta(days=3), end_date=auj, interval='1m')
    L=[]
    L.append(stock_data)
    IL = L[::-1]
    stock_total = pd.concat(IL)
    op = stock_total.iloc[:,0]
    hi = stock_total.iloc[:,1]
    lo = stock_total.iloc[:,2]
    cl = stock_total.iloc[:,3]
    op=op.interpolate()
    hi=hi.interpolate()
    lo=lo.interpolate()
    cl=cl.interpolate()
    date = stock_total.index[0:len(op)]

    for i in range(len(op)) :
        newop=str(op[i])
        newhi=str(hi[i])
        newlo=str(lo[i])
        newcl=str(cl[i])
        newa=str(date[i]).split()[0]+'T'+str(date[i]).split()[1]
        ope.write(newop+'\n')
        close.write(newcl+'\n')
        low.write(newlo+'\n')
        high.write(newhi+'\n')
        absi.write(newa+'\n')
    ope.close()
    high.close()
    low.close()
    close.close()
    absi.close()

    php_output = subprocess.check_output(
        ['php', './templates/interface_tim.php'])
    return php_output


if __name__ == '__main__':
    app.run(debug=True)
