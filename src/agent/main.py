import numpy as np
import threading
from queue import Queue
import time
import math

# Constants
NR_STATS = 7
NR_PARAMS = 4
R = 100
BLOCK_SIZE = 250
L = 64
N = L * L
NR_EXCHANGES = 5
BEGIN_DISCARD = 50
T = 250
SIM_R = 100

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
    return x - x.mean()

# The vector x is a centered vector!
def compute_sigma(x):
    T = x.shape[0]
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
    centered_squares = squares - squares.mean()
    length = x.shape[0] - lag
    s2 = np.square(centered_squares).sum()
    return np.dot(centered_squares[:length], centered_squares[lag:]) / s2

# This function returns the returns from the prices read into the file.
def get_returns(filename):
    with open(filename, "r") as f:
        data = f.readlines()
    price = [float(line.strip().split()[1]) for line in data]
    assert len(price) > 1
    T = len(price) - 1
    returns = np.zeros(T)
    for t in range(T):
        returns[t] = math.log(price[t + 1] / price[t])
    return returns


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
    T = x.shape[0]
    assert T > block_size
    index = np.random.randint(0, T - block_size + 1)
    nr_draws = int(T / block_size)
    tmp = np.zeros(T)
    for i in range(nr_draws):
        start = index(rng)
        for j in range(block_size):
            tmp[i * block_size:i * block_size + block_size] = x[start:start + block_size]
    remain = T - (nr_draws * block_size)
    start = index(rng)
    tmp[nr_draws * block_size:nr_draws * block_size + remain] = x[start:start + remain]
    return tmp

#-----------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------ Base de Functor -------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------


import numpy as np
import random
from scipy.optimize import least_squares

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
    def __init__(self, stats, print_=False):
        super().__init__(NR_PARAMS, NR_STATS)
        self.print_ = print_
        self.stats_ = stats

    #La méthode call() est l'opérateur de la fonction appelable qui est appelé lorsque lorsque l'objet est utilisé comme une fonction
    def __call__(self, beta, fvec):
        '''
        beta : vecteur de paramètres (tableau à 4 valeurs)
        fvec : vecteur de valeurs de fonction 'fvec' (tableau de 7 valeurs initialisées à zéro)
        '''
        
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
            dp_tm1 = 0
            trading_volume = 0

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
                dp_tm1 = excess_demand / lambda_

                if t >= BEGIN_DISCARD:
                    dp[t - BEGIN_DISCARD] = dp_tm1              #le taux de change est stocké dans le tableau 'dp'
                    trading_volume += local_trading_volume      #le volume de transaction local est ajouté au volume de transaction globale

            if np.sum(dp) == 0:
                print("None transactions...")
                return 0

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
            fvec[j] = stats_cumul[j] / SIM_R - self.stats_[j]

        return 1

import numpy as np
from scipy.optimize import least_squares
import scipy.optimize
import threading
import os

#Cette classe centralise toutes les informations que l'on a besoin pour lancer l'estimation
class Estimation:
    def __init__(self, r, M, beta0):
        self.r = r                                      #Le nombre de tâche
        self.stats = np.transpose(M[:r, :])             #Des statistiques à reproduire, chaque estimation essaye de reproduire des paramètres statistiques
        self.beta = beta0                               #le point de départ qui deviendra la solution
        print(f"{r} constructed...")

    def estimation_task(self):
        print(f"Task {self.r} starts...")
        functor = lambda x: (self.stats @ x).reshape((-1, 1))                   #functor est une fonction qui calcule le produit scalaire entre self.stats et x renvoie grâce au reshape(-1,-1) autant de colonne que d'entrée et automatique le nb de ligne
        numDiff = lambda x: np.gradient(functor(x), axis=0) / 0.0001            #fonction qui calcule le gradient de la fonction functor avec un pas de 0.0001, axis=0 derivée par rapport à la première dérivée de la matrice
        
        #Pour minimiser une fonction de plusieurs variables en trouvant des variables qui minimisent la fonction
        #functor est la fonction a minimiser, 
        #self.beta sont les valeurs initiales des variables
        lm = scipy.optimize.least_squares(functor, self.beta, jac=numDiff)
        print(f"Task {self.r} completes...")                              
        
        
        # Write results to file
        filename = f"{threading.get_ident()}.txt"
        with open(filename, "a") as f:
            f.write(f"{self.r}\t{lm.status}\t")
            f.write("\t".join(map(str, self.stats.flatten())) + "\t")
            f.write("\t".join(map(str, lm.x.flatten())) + "\n")

import numpy as np
import os
import threading
from concurrent.futures import ThreadPoolExecutor
from functools import partial

def main():

    rng = np.random.default_rng()
    returns = get_returns("CAC40-cours-journalier-ôclture.txt")
    R = 100  # Replace with the correct value for R
    M = np.zeros((R, NR_STATS))

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

    beta = np.array([1.73058, 1.04878, 0.0651077, 1603.94])
    stats = M[0, :]

    # TODO initialisation de ret avec estimation_task ?
    
    
    #vecteur de taille R pour chaque simulation
    estimations = [Estimation(r, M, beta) for r in range(R)]

    #Creation une pool of threads
    with ThreadPoolExecutor() as executor:
        for r in range(1, R):
            executor.submit(estimations[r].estimation_task)
    #Toutes les tâches ont été exécuté

    #Pour chaque paramètre, il calcule la moyenne, le 5%, la médiane, le 95% et le pourcentage
    for j in range(NR_PARAMS):
        tmp = np.array([estimations[r].beta[j] for r in range(R)])
        tmp.sort()
        print(j, tmp.mean(), tmp[int(0.05 * R)], tmp[int(0.5 * R)], tmp[int(0.95 * R)])

if __name__ == "__main__":
    main()


