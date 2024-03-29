import numpy as np
import threading
from queue import Queue
import time
import math
import yfinance as yf
import statistics as stat
import sys

import numpy as np
from scipy.optimize import least_squares
import scipy.optimize
import threading
import os

import numpy as np
import random
from scipy.optimize import least_squares

import numpy as np
import os
import threading
from concurrent.futures import ThreadPoolExecutor
from functools import partial
import datetime
from yahoo_fin import stock_info as si
import pandas_market_calendars as mcal
from typing import Iterable, Tuple


AUJ = datetime.date.today()

# Constants
NR_STATS = 7
NR_PARAMS = 4
R = 2 #TODO R = 100
BLOCK_SIZE = 250
L = 64
N = L * L
NR_EXCHANGES = 5
BEGIN_DISCARD = 50
T = 250
SIM_R = 1 #TODO SIM_R = 100
TEXTE =1

#-----------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------ Gestion des tâches : Threading ---------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------

#Les thresads sont des processus légers qui permettent d'exécuter des tâches en parallèle.
class ThreadPool:
    #Constructeur
    def __init__(self):
        self.threads = []                           #Stockage des threads
        self.is_busy = []                           #Indique si un thread est occupé ou non
        self.queue = Queue()                        #Stocker les tâches à faire
        self.condition = threading.Condition()      #Notifier les threads lorsqu'une nouvelle tâche est ajoutée à la file d'attente

        nr_threads = threading.cpu_count()          #Détermine le nombre de thread à créér en fonction de la machine

        self.is_busy = [False] * nr_threads         #Initialise à 'non occupé'

        #Création et lancement des thread
        for i in range(nr_threads):
            thread = threading.Thread(target=self.main_loop, args=(i,))
            thread.start()
            self.threads.append(thread)

    #Destructeur (appelé lorsque l'objet est détruit)
    def __del__(self):
        while True:
            idle_count = self.is_busy.count(False)      #Compte le nombre de threads 'False'

            if idle_count == len(self.is_busy):         #Si tous les threads sont inactifs
                for thread in self.threads:
                    thread.join()                       #La méthode join() bloque le programme jusqu'à ce le thread soit terminé
                return

            time.sleep(1)

    def main_loop(self, i):
        while True:
            task = self.queue.get()

            if task is None:
                break

            self.is_busy[i] = True
            task()
            self.is_busy[i] = False

    def add_task(self, task_to_add):
        self.queue.put(task_to_add)
        with self.condition:                            #verouillage de l'objet condition associé au thread
            self.condition.notify()                     #La méthode notify() signale à tous les threads en attente l'ajout et de reprendre la vérification de la file d'attente
   
   
   
#-----------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------ Outils d'analyse statistique -----------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------
        
# This function returns the vector x appropriately centered.
def centered(x):
    return x - np.mean(x)

# The vector x is a centered vector!
def compute_sigma(x):
    T = len(x)
    s2 = np.square(x).sum()
    return math.sqrt(s2 / (T - 1))

# The vector x is a centered vector!
def compute_kurtosis(x):
    T = x.shape[0]
    s2 = np.square(x).sum()
    s4 = np.square(x**2).sum()
    sigma2 = s2 / (T - 1)
    return s4 / sigma2**2 * T*(T+1) / (T-1) / (T-2) / (T-3) - 3. * (T-1)**2 / (T-2) / (T-3)

# The vector x is a centered vector!
def compute_autocorrelation(x, lag):
    length = x.shape[0] - lag
    s2 = np.square(x).sum()
    return np.dot(x[:length], x[lag:]) / s2

def compute_autocorrelation_squares(x, lag):
    squares = x**2
    centered_squares = squares - stat.mean(squares)
    length = x.shape[0] - lag
    s2 = np.square(centered_squares).sum()
    return np.dot(centered_squares[:length], centered_squares[lag:]) / s2

# This function returns the returns from the prices read into the file.
def get_returns(ticker):
    # Define the ticker list
    tickers_list = ticker

    # Extract the necessary data
    start_day = "2022-01-01"
    end_day = f"{AUJ}"

    tickerData = yf.Ticker(tickers_list)
    tickerDf = tickerData.history(period='1d', start=start_day, end=end_day)
    dailyClose = tickerDf['Close'].tolist()
    return np.array(dailyClose)

def get_closing_prices(ticker = '^FCHI') -> Iterable[Tuple[str,float]]:
    """ this function gets closing prices with dates

    Args:
        ticker (str, optional): ticker from yfinance. Defaults to '^FCHI'.

    Returns:
        Iterable[Tuple[str,float]]: list of date and closing prices
    """

    cac40 = yf.Ticker(ticker)
    
    #gets closing prices from a 1y period
    history = cac40.history(period='1y')
    
    #extract date and closing prices
    closing_prices = history['Close'].tolist()
    dates = history.index.tolist()
    
    #create the list
    prices_with_dates = list(zip(dates, closing_prices))
    
    return prices_with_dates

def compute_stat_interface(ticker = '^FCHI') -> None :
    """ This function creates a stats.txt of ticker for interface:
    Averiage Yield, Averiage Absolute Yield, Median, Standard Deviation, Kurtosis, Skewness, Studentized Range, Rank Correlation, Long Term Memory

    Args:
        ticker (str, optional): ticker from yfinance. Defaults to '^FCHI'.
    """
    
    c_a_c = get_closing_prices(ticker)

    #print(c_a_c[1][1])
    
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
    
    filename = "./plot/stats.txt"
    with open(filename, "w") as f:
        f.write(f'{rb}\n')
        f.write(f'{average_absr_m_rb}\n')
        f.write(f'{sigma}\n')
        f.write(f'{kurtosis}\n')
        f.write(f'{skewness}\n')
        f.write(f'{studentized_range}\n')
        f.write(f'{rho_1}\n')
        f.write(f'{rho_10}\n')
    


#-----------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------ Réseau d'Agents ------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------

#Retourne le numéro associé à l'agent (i,j)
def to_n(L, i, j):
    return i + j * L

#Retourne le num voisin à l'Est de l'agent n
def east(L, n):
    if n >= L * L:
        return 0
    j = n // L
    i = n - j * L
    m = i + (j + 1) * L
    return m - L * L if m >= L * L else m

#Retourne le num voisin au Sud de l'agent n
def south(L, n):
    if n >= L * L:
        return 0
    j = n // L
    i = n - j * L
    return j * L if i + 1 == L else (i + 1) + j * L

#Retourne le num voisin à l'Ouest de l'agent n
def west(L, n):
    if n >= L * L:
        return 0
    j = n // L
    i = n - j * L
    return i + (L - 1) * L if j == 0 else i + (j - 1) * L

#Retourne le num voisin au Nord de l'agent n
def north(L, n):
    if n >= L * L:
        return 0
    j = n // L
    i = n - j * L
    return L - 1 + j * L if i == 0 else i - 1 + j * L

#-----------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------ Estimation bootstrap -------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------


def one_draw_from_moving_block_bootstrap(rng, x, block_size):
    '''
    'rng' : a random number generator
    'x' : a time series data (a list or array)
    'block_size' : the size of the block to be used in the moving block bootstrap method
    '''
    T = x.shape[0]
    assert T > block_size
    index = np.random.randint(0, T - block_size + 1)
    nr_draws = int(T / block_size)
    tmp = np.zeros(T)
    for i in range(nr_draws):
        start = index
        for j in range(block_size):
            tmp[i * block_size:i * block_size + block_size] = x[start:start + block_size]
    remain = T - (nr_draws * block_size)
    start = index
    tmp[nr_draws * block_size:nr_draws * block_size + remain] = x[start:start + remain]
    return tmp

#-----------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------ Base de Functor -------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------

#Une classe qui implémente l'opérateur de la fonction appelable "()"
class BaseFunctor:
    def __init__(self, inputs=None, values=None):
        self.inputs_ = inputs
        self.values_ = values

    def inputs(self):
        return self.inputs_

    def values(self):
        return self.values_


class Functor(BaseFunctor):
    def __init__(self, stats, last_price, print_=False):
        super().__init__(NR_PARAMS, NR_STATS)
        self.txt = TEXTE
        self.print_ = print_
        self.stats_ = stats
        self.Price = np.zeros(T)
        self.lastprice = last_price

    #La méthode call() est l'opérateur de la fonction appelable qui est appelé lorsque lorsque l'objet est utilisé comme une fonction
    def __call__(self, beta):
        '''
        beta : vecteur de paramètres (tableau à 4 valeurs)
        fvec : vecteur de valeurs de fonction 'fvec' (tableau de 7 valeurs initialisées à zéro)
        '''
        fvec = np.zeros(NR_STATS)
        beta_m = beta[0]
        beta_n = beta[1]
        beta_i = beta[2]
        lambda_ = beta[3]
        assert NR_PARAMS == 4
        threshold = 1

        rng = np.random.default_rng()               #générateur de nombres
        rand_normal = rng.normal
        rand_uniform = rng.uniform
        #shock = np.array([rand_normal() for i in range(N)]) pas besoin car initialiser plus tard
        expectations = np.array([rand_uniform() for i in range(N)])

        stats_cumul = np.zeros(NR_STATS)
        dp = np.zeros(T)

        for r in range(SIM_R):                      #le nombre de simulation
            print()
            dp_tm1 = 0
            trading_volume = 0
            price = self.lastprice
            Price = np.zeros(T)
            for t in range(BEGIN_DISCARD + T):
                shock = rng.standard_normal(N)                                          #Un choc aléatoire est généré
                expectations = np.power(1 + np.abs(dp_tm1), beta_m) * beta_i * shock    #Initialise des attentes sans connaître celle des voisins
                
                for exchange in range(NR_EXCHANGES):
                    for i in range(N):
                        u = rng.uniform()
                        
                        #Choix d'un voisin aléatoire
                        j = west(L, i) if u < 0.25 else (south(L, i) if u < 0.5 else (east(L, i) if u < 0.75 else north(L, i)))
                        #Actualise mes attentes en fonction des attentes des voisins
                        expectations[i] = np.power(1 + np.abs(dp_tm1), beta_m) * (beta_n * expectations[j] + beta_i * shock[i])

                excess_demand = 0
                local_trading_volume = 0

                #Calcul de l'excès de demande sur chaque échange grâce aux attentes des traders
                for i in range(N):
                    if expectations[i] < -threshold:
                        excess_demand -= 1
                    elif expectations[i] > threshold:
                        excess_demand += 1
                        local_trading_volume += 1

                #Calcul du nouveau taux de change
                dp_tm1 = excess_demand / (lambda_*10)
                #print(dp_tm1)

                if t >= BEGIN_DISCARD:
                    dp[t - BEGIN_DISCARD] = dp_tm1              #le taux de change est stocké dans le tableau 'dp'
                    trading_volume += local_trading_volume      #le volume de transaction local est ajouté au volume de transaction globale
                    price = price*(1-dp_tm1)
                    #self.Price[t - BEGIN_DISCARD] += price/5
                    self.Price[t - BEGIN_DISCARD] = price
                    print(f'nouveau prix = {price} et trading_volume = {trading_volume}')
            
            
            if np.sum(dp) == 0:
                print("None transactions...")
                return 0
            
            #print(dp)
            
            #différentes statistiques sont calculées à partir des taux de change stockés dans dp
            centered_dp = centered(dp)
            stats_cumul[0] += compute_sigma(centered_dp)
            stats_cumul[1] += compute_kurtosis(centered_dp)
            stats_cumul[2] += compute_autocorrelation(centered_dp, 1)
            stats_cumul[3] += compute_autocorrelation(centered_dp, 10)
            stats_cumul[4] += compute_autocorrelation_squares(dp, 1)
            stats_cumul[5] += compute_autocorrelation_squares(dp, 10)
            stats_cumul[6] += trading_volume / N / T
            assert NR_STATS == 7

        
        # TODO à modifier
        for j in range(NR_STATS):
            #print(fvec)
            #print(stats_cumul)
            #print(self.stats_)
            fvec[j] = stats_cumul[j] / SIM_R - self.stats_[j]
        
        print(self.Price)
        
        
        
        if self.txt :
            
            # Création d'une liste pour stocker les heures
            heures = []

            # Définition de l'heure de départ
            heure = 13
            minute = 30

            # Boucle pour générer les heures jusqu'à 20h
            while heure < 20:
                # Ajout de l'heure actuelle à la liste
                heures.append(f"{heure:02d}:{minute:02d}:00")
    
                # Incrément des minutes de 5
                minute += 5
    
                # Vérification et ajustement des heures et minutes si nécessaire
                if minute >= 60:
                    minute = 0
                    heure += 1

            # Écriture des heures dans un fichier texte
            with open("heures.txt", "w") as fichier:
                for heure in heures:
                    fichier.write(heure + "\n")

            
            #filename = "PredictionAgent.txt"
            with open("./templates/PredictionAgent.txt", "w") as f:
                for i in range(len(self.Price)):
                    f.write(f'{self.Price[i]}\n')
            self.txt = 0

            #filename = "PredictionHeure"
            '''with open("./templates/PredictionHeure.txt", "w") as f:
                for i in range(250):
                    f.write(f'{AUJ}TT13:54:00')'''
            
            start_time = datetime.datetime.strptime("13:30:00", "%H:%M:%S")
            end_time = datetime.datetime.strptime("20:00:00", "%H:%M:%S")
            total_lines = 250

            time_difference = (end_time - start_time) / (total_lines - 1)

            # Créer le calendrier NYSE
            nyse = mcal.get_calendar('NYSE')

            # Obtenir le dernier jour d'ouverture du marché
            last_trading_day = nyse.valid_days(start_date=AUJ- datetime.timedelta(days=5), end_date=AUJ)[-1]


            with open("./templates/PredictionHeure.txt", "w") as file:
                current_time = start_time
                for _ in range(total_lines):
                    datetime_string = last_trading_day.strftime("%Y-%m-%d") + "T" + current_time.strftime("%H:%M:%S")
                    file.write(datetime_string + "\n")
                    current_time += time_difference
            
            # filename = "PredictionAgentAbscisse.txt"
            # with open(filename, "a") as f:
            #     for i in range(len(self.Price)):
            #         f.write(f'{}')
            
        
        # for i in range(len(self.Price)):
        #     print(self.Price[i])
        
        return 1


class Estimation:
    def __init__(self, r, M, beta0, lastprice):
        self.r = r
        self.stats = np.transpose(M[r])
        self.beta = beta0
        self.Price = 0 
        self.lastprice = lastprice
        print(self.r, "constructed...")
        #print(self.stats)

    def estimation_task(self):
        print("Task", self.r, "starts...")

        functor=Functor(self.stats, self.lastprice)
        functor.__call__(self.beta)
        #lm = least_squares(Functor(self.stats, self.lastprice), self.beta, method='trf')
        #ret = lm.status
        print("Task", self.r, "completes...")
        #filename = f"{threading.get_ident()}.txt"
        #with open(filename, "a") as f:
        #    f.write(f"{self.r}\t{ret}\t")
        #    f.write("\t".join(map(str, self.stats.flatten())) + "\t")
        #    f.write("\t".join(map(str, lm.x.flatten())) + "\n")


def main(ticker):

    rng = np.random.default_rng()
    returns = get_returns(ticker)
    lastprice = returns[-1]
    M = np.zeros((R, NR_STATS))         #matrice de R lignes et 7 colonnes de statistiques (sigma, kurtosis ...)

    #effectue R simulations échantillons bootstrap dont on calcules les paramètres statistiques
    for r in range(R):
        x = returns if r == 0 else one_draw_from_moving_block_bootstrap(rng, returns, BLOCK_SIZE)
        centered_x = centered(x)
        M[r, 0] = compute_sigma(centered_x)
        M[r, 1] = compute_kurtosis(centered_x)
        M[r, 2] = compute_autocorrelation(centered_x, 1)
        M[r, 3] = compute_autocorrelation(centered_x, 10)
        M[r, 4] = compute_autocorrelation_squares(x, 1)
        M[r, 5] = compute_autocorrelation_squares(x, 10)
        M[r, 6] = 0.01

    
    beta = np.array([1.73058, 1.04878, 0.0651077, 1603.94])     #optimisation : source macro-économique, une source liée à son voisinage, une source idiosyncratique
    #beta0 = np.array([1, 1, 0, 1000])     #stat du l'échantillon d'origine
    stats = M[0, :]                                            
    
    
    #print(M)
    # TODO initialisation de ret avec estimation_task ?
    
    
    #vecteur de taille R pour chaque simulation
    estimations = [Estimation(r, M, beta, lastprice) for r in range(R)]

    #Creation une pool of threads
    with ThreadPoolExecutor() as executor:
        for r in range(1, R):
            executor.submit(estimations[r].estimation_task())
    #Toutes les tâches ont été exécuté

    #Pour chaque paramètre, il calcule la moyenne, le 5%, la médiane, le 95% et le pourcentage
    #for j in range(NR_PARAMS):
    #    tmp = np.array([estimations[r].beta[j] for r in range(R)])
    #    tmp.sort()
    #    print(f"{j}, moyenne = {stat.mean(tmp)}, 5% = {tmp[int(0.05 * R)]},  médiane = {tmp[int(0.5 * R)]}, 95% = {tmp[int(0.95 * R)]}")

    compute_stat_interface(ticker)

if __name__ == "__main__":
    main()

