from typing import Iterable, Tuple

import numpy as np
from scipy.optimize import least_squares
from Functor import *

def one_draw_from_moving_block_bootstrap(rng : float, x: Iterable[float], block_size: int)-> Iterable[float]:
    """ Moving block bootstrap is a resampling method used to estimate the statistical properties of a time series.
        The main idea of the moving block bootstrap is to generate bootstrap samples 
        by using consecutive blocks of data rather than individual observations.

    Args:
        rng (float): random number between 0 and 1
        x (Iterable[float]): list of daily closed prices (time series data)
        block_size (int): size of a block

    Returns:
        Iterable[float]: new list of daily closed prices resampled
    """

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


class Estimation:
    """ A class which launchs a task to estimate beta which represents 3 values describing envrionnement
        by minimizing the functor function : 
        beta = [beta_macroeconomic, beta_neighborhood, beta_idiosyncratic]
        
    Attributes
    ----------
    r: int
        Agent, which executes movement orders of path finding.
    stats: ASensor
        Sensor used to scan and rescan the map.
    beta: ASensor
        Sensor used to scan and rescan the map
    Price: ASensor
        Sensor used to scan and rescan the map
        
    
        
    Methods
    -------

    estimation_task():
        it estimates beta which represents 3 values describing envrionnement
        by minimizing the functor function : 
        beta = [beta_macroeconomic, beta_neighborhood, beta_idiosyncratic]
        

    """
    
    def __init__(self, 
                 r: int, 
                 M: Iterable[Iterable[float]], 
                 beta0: Tuple[float,float,float],
                 lastprice: float) -> None:
        """Uses transpose to have a column of rth stats

        Args:
            r (int): number of line r (line of stats)
            M (Iterable[Iterable[float]]): Array of stats
            beta0 (Tuple[float,float,float]): beta value to start minimizing
            lastprice (float): last price with yfinance of ticker
            
        """
        self.r = r
        self.stats = np.transpose(M[r])
        self.beta = beta0
        self.lastprice = lastprice 
        print(self.r, "constructed...")
        #print(self.stats)

    def estimation_task(self) -> None:
        """ It estimates beta which represents 3 values describing envrionnement
            by minimizing the functor function : 
            beta = [beta_macroeconomic, beta_neighborhood, beta_idiosyncratic]
        """
        print("Task", self.r, "starts...")
        lm = least_squares(Functor(self.stats, self.lastprice), self.beta, method='trf')
        ret = lm.status
        print("Task", self.r, "completes...")
        
        #filename = f"{threading.get_ident()}.txt"
        #with open(filename, "a") as f:
        #    f.write(f"{self.r}\t{ret}\t")
        #    f.write("\t".join(map(str, self.stats.flatten())) + "\t")
        #    f.write("\t".join(map(str, lm.x.flatten())) + "\n")