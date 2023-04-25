import yfinance as yf
from flask import Flask, request, render_template
import subprocess

# ---------------------------------------------------------------


app = Flask(__name__)

@app.route('/')
def home():
    php_output = subprocess.check_output(['php', 'C:\\inetpub\\wwwroot\\pro3600.php'])
    return php_output

@app.route('/result', methods=['POST'])
def result():
        ticker = request.form['inputValue']
        # Extract the necessary data
        start_day_train = "2023-01-02"
        end_day_train = "2023-04-05"

        stock = yf.download(ticker, start_day_train, end_day_train)
        values = stock.iloc[:,4]
        date = stock.index[0:len(values)]

        ordo = open("C:\\inetpub\\wwwroot\\ordo.txt", "w")
        absi = open("C:\\inetpub\\wwwroot\\absi.txt", "w")
        for i in range(len(values)) :
           newo=str(values[i])
           newa=str(date[i]).split()[0]
           ordo.write(newo+'\n')
           absi.write(newa+'\n')
        ordo.close()
        absi.close()
        php_output = subprocess.check_output(['php', 'C:\\inetpub\\wwwroot\\pro3600.php'])
        return php_output

if __name__ == '__main__':
    app.run(debug=True)