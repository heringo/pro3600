from typing import Iterable, Tuple
import sys

import numpy as np
import datetime

from network_agent import *
from compute_stat import *

AUJ = datetime.date.today()

# Constants
NR_STATS = 7
NR_PARAMS = 4
R = 2               #TODO R = 100
BLOCK_SIZE = 250
L = 64
N = L * L
NR_EXCHANGES = 5
BEGIN_DISCARD = 50
T = 250
SIM_R = 1           #TODO SIM_R = 100  #number of simulation
TEXTE = 1


class BaseFunctor:
    """ An abstract base class used for creating custom functor objects.
    
    Attributes
    ----------
    inputs: any
        inputs 
    values: any
        values
        
    Methods
    -------
    inputs():
        return inputs_    
    values():
        return values
    """
    def __init__(self, inputs=None, values=None) -> None:
        self.inputs_ = inputs
        self.values_ = values

    def inputs(self):
        return self.inputs_

    def values(self):
        return self.values_


class Functor(BaseFunctor):
    """Functor which simulates the trading market in one day with agent

    Args:
        BaseFunctor (BaseFuntor): class BaseFuntor 
        
    Attributes
    ----------
    txt: int
        condition to stop the simulation and to print on a txt file
    print_: boolean

    stats_: Iterable[float]
        statistics of sample 
    Price: Iterable[float]
        Variation of prices during the journey
        
        
    Methods
    -------
    __call__(beta):
        Operator which is called when Functor is used
    """
    
    
    def __init__(self, 
                 stats: Iterable[float],
                 lastprice : float, 
                 print_=False) -> None:
        """Super init with NR_PARAMS, NR_STATS which are integers

        Args:
            stats (Iterable[float]): statistics of sample 
            lastprice (float): last price from yfinance of ticker
            print_ (bool, optional): Defaults to False.
        """
        super().__init__(NR_PARAMS, NR_STATS)
        self.txt = True
        self.print_ = print_
        self.stats_ = stats
        self.Price = np.zeros(T)
        self.lastprice = lastprice
        
        '''
        beta : vecteur de paramètres (tableau à 4 valeurs)
        fvec : vecteur de valeurs de fonction 'fvec' (tableau de 7 valeurs initialisées à zéro)
        '''

    def __call__(self, beta: Tuple[float, float, float]) -> int:
        """Operator which is called when Functor is used

        Args:
            beta (Tuple[float, float, float]): beta = [beta_macroeconomic, beta_neighborhood, beta_idiosyncratic]

        Returns:
            int: 1 or 0 if the function was completed
        """
        
        fvec = np.zeros(NR_STATS)                   #vector for stats
        beta_m = beta[0]
        beta_n = beta[1]
        beta_i = beta[2]
        lambda_ = beta[3]
        assert NR_PARAMS == 4
        threshold = 1
        self.log = True

        rng = np.random.default_rng()               #random number between 1 and 2 
        rand_uniform = rng.uniform

        expectations = np.array([rand_uniform() for i in range(N)])

        stats_cumul = np.zeros(NR_STATS)
        dp = np.zeros(T)

        for r in range(SIM_R):                      
            print()
            dp_tm1 = 0
            trading_volume = 0
            price = self.lastprice
            Price = np.zeros(T)
            for t in range(BEGIN_DISCARD + T):
                shock = rng.standard_normal(N)                                          #Genererate a shock
                expectations = np.power(1 + np.abs(dp_tm1), beta_m) * beta_i * shock    #Initialize expectations of agents without knowledge of their neighboors
                
                for exchange in range(NR_EXCHANGES):
                    for i in range(N):
                        u = rng.uniform()
                        
                        #Random neighboor chosen 
                        j = west(L, i) if u < 0.25 else (south(L, i) if u < 0.5 else (east(L, i) if u < 0.75 else north(L, i)))
                        #Update expectation with knowing their neigboors
                        expectations[i] = np.power(1 + np.abs(dp_tm1), beta_m) * (beta_n * expectations[j] + beta_i * shock[i])

                excess_demand = 0
                local_trading_volume = 0

                #Compute excess demande for each trade with expectations
                for i in range(N):
                    if expectations[i] < -threshold:
                        excess_demand -= 1
                    elif expectations[i] > threshold:
                        excess_demand += 1
                        local_trading_volume += 1

                #compute new exchange rates
                dp_tm1 = excess_demand / (lambda_*10)
                #print(dp_tm1)

                if t >= BEGIN_DISCARD:
                    dp[t - BEGIN_DISCARD] = dp_tm1              #exchange rate is stocked on dp
                    trading_volume += local_trading_volume      #local transaction volume is added to global transaction
                    price = price*(1-dp_tm1)
                    self.Price[t - BEGIN_DISCARD] = price
                    
                    if self.log == True :
                        print(f'nouveau prix = {price} et trading_volume = {trading_volume}')
            
            
            if np.sum(dp) == 0:
                print("None transactions...")
                return 0
            
            #print(dp)
            
            #stats computed from the exchange rate
            centered_dp = centered(dp)
            stats_cumul[0] += compute_sigma(centered_dp)
            stats_cumul[1] += compute_kurtosis(centered_dp)
            stats_cumul[2] += compute_autocorrelation(centered_dp, 1)
            stats_cumul[3] += compute_autocorrelation(centered_dp, 10)
            stats_cumul[4] += compute_autocorrelation_squares(dp, 1)
            stats_cumul[5] += compute_autocorrelation_squares(dp, 10)
            stats_cumul[6] += trading_volume / N / T
            assert NR_STATS == 7
        
        if self.log == True :
            print(self.Price)
        
        if self.txt :
            
            filename = "./templates/PredictionAgent.txt"
            with open(filename, "w") as f:
                for i in range(len(self.Price)):
                    f.write(f'{self.Price[i]}\n')
            
            sys.exit()
            
        
        return 1