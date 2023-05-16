import sys, os

# sys.path.insert(1,os.path.join(os.path.dirname(__file__), '../NeuralProphet', 'NeuralProphet'))
# sys.path.insert(1,os.path.join(os.path.dirname(__file__), '..', 'agent'))

# import NeuralProphet.main
# import agent.main


import yfinance as yf
from flask import Flask, request, render_template
import subprocess

import pandas as pd

import yfinance as yf
# import math
# import numpy as np
# import pandas_market_calendars as mcal
from datetime import timedelta, datetime
import yahoo_fin.stock_info as si
import importlib

# ---------------------------------------------------------------
import datetime
auj = datetime.date.today()



app = Flask(__name__)


@app.route('/')
def home():
    php_output = subprocess.check_output(
        ['php', 'pro.php'])
    return php_output


@app.route('/result', methods=['POST'])
def result():
    L=[]
    # On vérifie que le ticker existe bien
    ticker = request.form['inputValue']
    # On fixe les dates d'import des données et de prédiction
    start_day_train = '2015-01-01'
    start_day_brownian = auj - datetime.timedelta(days=365)
    end_day_train = auj
    end_day_pred = auj + datetime.timedelta(days=2*30)

    if ticker == "":
        php_output = subprocess.check_output(
        ['php', 'pro.php'])
        return php_output

    # Période pour laquelle on telecharge tourtes les données jusqu'à aujourdhui
    stock = yf.download(ticker, start_day_train, end_day_train)
    if stock.empty:
        error_message = "Le ticker '{}' n'existe pas.".format(ticker)
        return render_template('erreur.html', ticker=ticker)
    
    #Modèle brownien
    brownian_function = importlib.import_module('brownian')
    S_plot,dates_pred = brownian_function.brownian(ticker, start_day_train,end_day_train,start_day_brownian,end_day_pred,stock)
    
    #Modèle NeuralProphet
    neural_function = importlib.import_module('main')
    neural, neural_dates = neural_function.main(ticker)
    
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
    stock['ewma'] = cl.ewm(span=30).mean()
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
    ewma = open("./templates/rewma.txt", "w")
    bolup = open("./templates/rbolup.txt", "w")
    boldown = open("./templates/rboldown.txt", "w")
    rsi = open("./templates/rrsi.txt", "w")
    macd = open("./templates/rmacd.txt", "w")
    signal = open("./templates/rsignal.txt", "w")
    hist = open("./templates/rhist.txt", "w")
    fastso = open("./templates/rfastso.txt", "w")
    slowso = open("./templates/rslowso.txt", "w")
    fin=auj
    for i in range(5) :
        deb=fin - datetime.timedelta(days=4)
        stock_data = si.get_data(ticker, start_date=deb, end_date=fin, interval='1m')
        L.append(stock_data)
        fin=deb - datetime.timedelta(days=1)
    stock_data = si.get_data(ticker, start_date=auj - datetime.timedelta(days=29), end_date=fin, interval='1m')
    L.append(stock_data)
    IL = L[::-1]
    stock_total = pd.concat(IL)
    stock_total = stock_total.loc[:, ~stock_total.columns.duplicated()]
    op = stock_total.iloc[:,0]
    hi = stock_total.iloc[:,1]
    lo = stock_total.iloc[:,2]
    cl = stock_total.iloc[:,3]
    op=op.interpolate()
    hi=hi.interpolate()
    lo=lo.interpolate()
    cl=cl.interpolate()

    # SMA
    stock_total['ewma'] = cl.ewm(span=30).mean()
    # Bollinger Bands
    stock_total['bollinger_up'] = cl.rolling(20).mean() + cl.rolling(20).std() * 2
    stock_total['bollinger_down'] = cl.rolling(20).mean() - cl.rolling(20).std() * 2

    # RSI
    change = cl.diff()
    change.dropna(inplace=True)
    change_up = change.copy()
    change_down = change.copy()
    change_up[change_up < 0] = 0
    change_down[change_down > 0] = 0

    T = ["nan"]
    for i in range(len(op)-1) :
        newT = 100 * change_up.rolling(14).mean()[i] / (
            change_up.rolling(14).mean()[i] + change_down.rolling(14).mean().abs()[i])
        T.append(newT)
    # MACD
    exp1 = cl.ewm(span=12, adjust=False).mean()
    exp2 = cl.ewm(span=26, adjust=False).mean()
    stock_total["macd"] = exp1 - exp2
    stock_total['signal'] = stock_total['macd'].ewm(span=9, adjust=False).mean()
    stock_total["hist"] = stock_total['macd'] - stock_total['signal']
    # SO
    stock_total["highroll"] = hi.rolling(14).max()
    stock_total["lowroll"] = lo.rolling(14).min()
    stock_total["%K"] = ((cl - stock_total['lowroll']) /
                   (stock_total['highroll']-stock_total['lowroll'])) * 100
    stock_total["%D"] = stock_total["%K"].rolling(3).mean()

    date = stock_total.index[0:len(op)]

    for i in range(len(op)) :
        newop=str(op[i])
        newhi=str(hi[i])
        newlo=str(lo[i])
        newcl=str(cl[i])
        newewma = str(stock_total["ewma"][i])
        newbolup = str(stock_total['bollinger_up'][i])
        newboldown = str(stock_total['bollinger_down'][i])
        newrsi = str(T[i])
        newmacd = str(stock_total['macd'][i])
        newsignal = str(stock_total['signal'][i])
        newhist = str(stock_total['hist'][i])
        newfastso = str(stock_total['%K'][i])
        newslowso = str(stock_total['%D'][i])
        newa=str(date[i]).split()[0]+'T'+str(date[i]).split()[1]
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
    ope.close()
    high.close()
    low.close()
    close.close()
    absi.close()
    ewma.close()
    bolup.close()
    boldown.close()
    rsi.close()
    macd.close()
    signal.close()
    hist.close()
    fastso.close()
    slowso.close()
    php_output = subprocess.check_output(
        ['php', 'pro.php'])
    return php_output


if __name__ == '__main__':
    app.run(debug=True)
