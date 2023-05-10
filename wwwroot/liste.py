import yfinance as yf
from flask import Flask, request, render_template
import subprocess
import yahoo_fin.stock_info as si
import pandas as pd

# ---------------------------------------------------------------
import datetime
auj = datetime.date.today()
L=[]

app = Flask(__name__)

@app.route('/')
def home():
    php_output = subprocess.check_output(['php', 'C:\\inetpub\\wwwroot\\pro3600.php'])
    return php_output

@app.route('/result', methods=['POST'])
def result():
         ticker = request.form['inputValue']
         # Extract the necessary data
         start_day_train = '1900-01-01'
         end_day_train = auj

         stock = yf.download(ticker, start_day_train, end_day_train)
         values = stock.iloc[:,4]
         op = stock.iloc[:,0]
         hi = stock.iloc[:,1]
         lo = stock.iloc[:,2]
         cl = stock.iloc[:,3]
         date = stock.index[0:len(values)]

         ordo = open("C:\\inetpub\\wwwroot\\ressources\\ordo.txt", "w")
         absi = open("C:\\inetpub\\wwwroot\\ressources\\absi.txt", "w")
         ope = open("C:\\inetpub\\wwwroot\\ressources\\open.txt", "w")
         close = open("C:\\inetpub\\wwwroot\\ressources\\close.txt", "w")
         low = open("C:\\inetpub\\wwwroot\\ressources\\low.txt", "w")
         high = open("C:\\inetpub\\wwwroot\\ressources\\high.txt", "w")
         for i in range(len(values)) :
            newo=str(values[i])
            newop=str(op[i])
            newhi=str(hi[i])
            newlo=str(lo[i])
            newcl=str(cl[i])
            newa=str(date[i]).split()[0]
            ordo.write(newo+'\n')
            ope.write(newop+'\n')
            close.write(newcl+'\n')
            low.write(newlo+'\n')
            high.write(newhi+'\n')
            absi.write(newa+'\n')
         ordo.close()
         ope.close()
         high.close()
         low.close()
         close.close()
         absi.close()

         absi = open("C:\\inetpub\\wwwroot\\ressources\\rabsi.txt", "w")
         ope = open("C:\\inetpub\\wwwroot\\ressources\\ropen.txt", "w")
         close = open("C:\\inetpub\\wwwroot\\ressources\\rclose.txt", "w")
         low = open("C:\\inetpub\\wwwroot\\ressources\\rlow.txt", "w")
         high = open("C:\\inetpub\\wwwroot\\ressources\\rhigh.txt", "w")
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
         php_output = subprocess.check_output(['php', 'C:\\inetpub\\wwwroot\\pro3600.php'])
         return php_output

if __name__ == '__main__':
    app.run(debug=True)