import yfinance as yf
from flask import Flask, request, render_template
import subprocess

# ---------------------------------------------------------------
import datetime
auj = datetime.date.today()

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
        php_output = subprocess.check_output(['php', 'C:\\inetpub\\wwwroot\\pro3600.php'])
        return php_output

if __name__ == '__main__':
    app.run(debug=True)