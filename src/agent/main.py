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

class ThreadPool:
    def __init__(self):
        self.threads = []
        self.is_busy = []
        self.queue = Queue()
        self.condition = threading.Condition()

        # Get the natural number of threads.
        nr_threads = threading.cpu_count()

        # Assign "not busy" to all threads
        self.is_busy = [False] * nr_threads

        # Start the main loop for each thread
        for i in range(nr_threads):
            thread = threading.Thread(target=self.main_loop, args=(i,))
            thread.start()
            self.threads.append(thread)

    def __del__(self):
        while True:
            idle_count = self.is_busy.count(False)

            if idle_count == len(self.is_busy):
                for thread in self.threads:
                    thread.join()
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
        with self.condition:
            self.condition.notify()
            
'''Ce code Python définit une classe ThreadPool qui permet d'exécuter plusieurs tâches en parallèle en utilisant des threads. 
Les constantes définies au début du code sont également présentes.

Notez que les bibliothèques standard Python threading et queue sont utilisées pour gérer la synchronisation et la communication entre les threads. 
La destruction du ThreadPool a été implémentée en utilisant __del__() au lieu du destructeur C++ ~ThreadPool().'''

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


#This funcition returns the agent number at (i,j) location within the L x L lattice.
#The agents are stored by columns
def to_n(L, i, j):
    return i + j * L

#The function returns the east neighbor agent number
def east(L, n):
    if n >= L * L:
        return 0
    j = n // L
    i = n - j * L
    m = i + (j + 1) * L
    return m - L * L if m >= L * L else m

#This function return the south neighbor agent number
def south(L, n):
    if n >= L * L:
        return 0
    j = n // L
    i = n - j * L
    return j * L if i + 1 == L else (i + 1) + j * L

#The function returns the west neighbor agent number
def west(L, n):
    if n >= L * L:
        return 0
    j = n // L
    i = n - j * L
    return i + (L - 1) * L if j == 0 else i + (j - 1) * L

#The function returns the north neightboor agent number
def north(L, n):
    if n >= L * L:
        return 0
    j = n // L
    i = n - j * L
    return L - 1 + j * L if i == 0 else i - 1 + j * L


# This function returns a bootstrapped vector.
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

import numpy as np
import random
from scipy.optimize import least_squares


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
        super().__init__(nr_prms, nr_stats)
        self.print_ = print_
        self.stats_ = stats

    def __call__(self, beta, fvec):
        beta_m = beta[0]
        beta_n = beta[1]
        beta_i = beta[2]
        lambda_ = beta[3]
        assert nr_prms == 4
        expr_threshold = 1

        rng = np.random.default_rng()
        stats_cumul = np.zeros(nr_stats)

        for r in range(sim_R):
            dp_tm1 = 0
            trading_volume = 0

            for t in range(begin_discard + T):
                shock = rng.standard_normal(N)
                expectations = np.power(1 + np.abs(dp_tm1), beta_m) * beta_i * shock

                for exchange in range(nr_exchanges):
                    for i in range(N):
                        u = rng.uniform()
                        j = random_neighbor(L, i, u)
                        expectations[i] = np.power(1 + np.abs(dp_tm1), beta_m) * (beta_n * expectations[j] + beta_i * shock[i])

                excess_demand = 0
                local_trading_volume = 0

                for i in range(N):
                    if expectations[i] < -threshold:
                        excess_demand -= 1
                    elif expectations[i] > threshold:
                        excess_demand += 1
                        local_trading_volume += 1

                dp_tm1 = excess_demand / lambda_

                if t >= begin_discard:
                    dp[t - begin_discard] = dp_tm1
                    trading_volume += local_trading_volume

            if np.sum(dp) == 0:
                print("None transactions...")
                return 1

            centered_dp = centered(dp)
            stats_cumul[0] += compute_sigma(centered_dp)
            stats_cumul[1] += compute_kurtosis(centered_dp)
            stats_cumul[2] += compute_autocorrelation(centered_dp, 1)
            stats_cumul[3] += compute_autocorrelation(centered_dp, 10)
            stats_cumul[4] += compute_autocorrelation_squares(dp, 1)
            stats_cumul[5] += compute_autocorrelation_squares(dp, 10)
            stats_cumul[6] += trading_volume / N / T
            assert nr_stats == 7

        for j in range(nr_stats):
            fvec[j] = stats_cumul[j] / sim_R - self.stats_[j]

        if self.print_:
            print("_m\t_n\t_i\t\t\t\t_0\t_10\t_0\t_10\ttv\tfit")
            for j in range(nr_prms):
                print(beta[j], end='\t')
            for j in range(nr_stats):
                print(stats_cumul[j] / sim_R, end='\t')
            print(np.sum((stats_cumul / sim_R - self.stats_) ** 2))

        return 0

import numpy as np
from scipy.optimize import least_squares
import threading
import os

class Estimation:
    def __init__(self, r, M, beta0):
        self.r = r
        self.stats = M[r, :].T
        self.beta = beta0.copy()
        print(f"{r} constructed...")

    def estimation_task(self):
        print(f"Task {self.r} starts...")
        
        def functor(beta):
            # Define the function to compute the difference between the estimated and target statistics.
            # You'll need to replace this with the actual function based on your problem.
            return np.zeros_like(self.stats)

        result = least_squares(functor, self.beta)
        print(f"Task {self.r} completes...")
        
        # The results are put at the end of a file, one file per thread.
        # The name of the file is built with the id of the thread.
        file_name = f"{threading.get_ident()}.txt"
        with open(file_name, "a") as out:
            out.write(f"{self.r}\t{result.status}\t")
            for j in range(len(self.stats)):
                out.write(f"{self.stats[j]}\t")
            for j in range(len(self.beta)):
                out.write(f"{self.beta[j]}\t")
            out.write("\n")

import numpy as np
import os
import threading
from concurrent.futures import ThreadPoolExecutor
from functools import partial

def main():
    # Replace the following functions with the appropriate implementations
    def get_returns(file_name):
        pass

    def one_draw_from_moving_block_bootstrap(rng, returns, block_size):
        pass

    def centered(x):
        pass

    def compute_sigma(centered_x):
        pass

    def compute_kurtosis(centered_x):
        pass

    def compute_autocorrelation(centered_x, lag):
        pass

    def compute_autocorrelation_squares(x, lag):
        pass

    rng = np.random.default_rng()
    returns = get_returns("CAC40-cours-journalier-ôclture.txt")
    R = 100  # Replace with the correct value for R
    nr_stats = 7
    M = np.zeros((R, nr_stats))

    for r in range(R):
        x = returns if r == 0 else one_draw_from_moving_block_bootstrap(rng, returns, block_size)
        centered_x = centered(x)
        M[r, 0] = compute_sigma(centered_x)
        M[r, 1] = compute_kurtosis(centered_x)
        M[r, 2] = compute_autocorrelation(centered_x, 1)
        M[r, 3] = compute_autocorrelation(centered_x, 10)
        M[r, 4] = compute_autocorrelation_squares(x, 1)
        M[r, 5] = compute_autocorrelation_squares(x, 10)
        M[r, 6] = 0.01

    nr_prms = 4
    beta = np.array([1.73058, 1.04878, 0.0651077, 1603.94])
    stats = M[0, :]
    # Replace the following line with the actual optimization step
    # based on your problem
    ret, beta = 0, beta

    estimations = [Estimation(r, M, beta) for r in range(R)]

    with ThreadPoolExecutor() as executor:
        for r in range(1, R):
            executor.submit(estimations[r].estimation_task)

    for j in range(nr_prms):
        tmp = np.array([estimations[r].beta[j] for r in range(R)])
        tmp.sort()
        print(j, tmp.mean(), tmp[int(0.05 * R)], tmp[int(0.5 * R)], tmp[int(0.95 * R)])

if __name__ == "__main__":
    main()


