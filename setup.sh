#!/bin/bash
wget https://www.python.org/ftp/python/3.9.6/Python-3.9.6.tgz
wget https://www.php.net/distributions/php-8.0.8.tar.gz
tar -xf Python-3.9.5.tgz
tar -xf php-8.0.8.tar.gz
cd Python-3.9.5
./configure
make
sudo make install
cd ..
cd php-8.0.8
./configure
make
sudo make install
cd..
wget https://bootstrap.pypa.io/get-pip.py
sudo python3 get-pip.py

pip install numpy
/usr/bin/python3 -m pip install neuralprophet 
pip install matplotlib
pip install pandas
pip install tables
pip install scipy
pip install flask
pip install yfinance
pip install pandas_datareader
pip install plotly 
pip install plotly_resampler
pip install datetime
pip install pandas_market_calendars
pip install typing
