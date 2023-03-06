import yfinance as yf 

# Récupérer les données pour le CAC 40
cac40 = yf.Ticker("TSLA")

# Récupérer l'historique des prix sur une période donnée
hist = cac40.history(period="max")

print(hist[:5])