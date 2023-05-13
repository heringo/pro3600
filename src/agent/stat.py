#Script to calculate CAC40 statistics
#la moyenne, l'écart-type, la médiane, le minimum, le maximum, le kurtosis, la skewness, le Studentized Range et deux corrélations de rang (à une journée et dix jours).
import math
import yfinance as yf

def get_cac40_closing_prices():
    # Créer un objet Ticker pour le CAC40
    cac40 = yf.Ticker('^FCHI')
    
    # Récupérer l'historique des prix de clôture sur une période d'un an
    history = cac40.history(period='1y')
    
    # Extraire les prix de clôture et les dates
    closing_prices = history['Close'].tolist()
    dates = history.index.tolist()
    
    # Créer une liste des prix de clôture avec leurs dates correspondantes
    prices_with_dates = list(zip(dates, closing_prices))
    
    return prices_with_dates

# Appel de la fonction pour récupérer les prix de clôture du CAC40 sur un an
c_a_c = get_cac40_closing_prices()

#print(c_a_c)
print(c_a_c[1][1])
# Affichage des prix de clôture
#for date, price in cac40_prices:
#    print(f"Date: {date}, Prix de clôture: {price}")
#
#
#Extract data from the file
#with open("CAC40-cours-journalier-ôclture.txt") as f:
#    c_a_c = []
#    for line in f:
#        date, value = line.split()
#        c_a_c.append(float(value))

#Operation for daily yield and average daily yield 
r = []
for i in range(1, len(c_a_c)):
    r.append(math.log(c_a_c[i][1] / c_a_c[i - 1][1]))

T = len(r)
rb = sum(r) / T 
print("T", T)
print("rb", rb)

#Operation for average absolute yield
absr_m_rb = [abs(x) for x in r]
average_absr_m_rb = sum(absr_m_rb) / T
print("average_absr_m_rb", average_absr_m_rb)

#Operation for min and max daily yield
min_r = min(r)
max_r = max(r)
print("min", min_r)
print("max", max_r)

#Operation for median 
median_r = sorted(r)[T // 2]
print("median", median_r)

#Operation for Variance and Standard deviation
r_m_rb = [r_t - rb for r_t in r]

sigma2 = sum([x * x for x in r_m_rb]) / (T - 1)
sigma = math.sqrt(sigma2)
print("sigma2", sigma2)
print("sigma", sigma)

#Operation for Kurtosis
tmp4 = sum([x * x * x * x for x in r_m_rb])
kurtosis = tmp4 / (sigma2 ** 2) * T * (T + 1) / ((T - 1) * (T - 2) * (T - 3)) - 3 * (T - 1) ** 2 / ((T - 2) * (T - 3))
print("kurtosis", kurtosis)

#Operation for skewness
tmp2 = sum([x * x for x in r_m_rb])
tmp3 = sum([x ** 3 for x in r_m_rb])
skewness = tmp3 / (sigma2 ** 1.5) * T / ((T - 1) * (T - 2))
print("skewness", skewness)

#Operation for studentized Range
studentized_range = (max_r - min_r) / sigma
print("studentized_range", studentized_range)

#Operation for rank correlations 
s2 = sum([x * y for x, y in zip(r_m_rb, r_m_rb)])
rho_1 = sum([x * y for x, y in zip(r_m_rb[1:], r_m_rb)]) / s2
rho_10 = sum([x * y for x, y in zip(r_m_rb[10:], r_m_rb)]) / s2
print("rho_1", rho_1)
print("rho_10", rho_10)