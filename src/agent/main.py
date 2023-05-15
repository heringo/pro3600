import datetime
import numpy as np
from concurrent.futures import ThreadPoolExecutor

from compute_stat import *
from Estimation import *

import datetime
AUJ = datetime.date.today()

# Constants
NR_STATS = 7
NR_PARAMS = 4
R = 2                       #TODO R = 100 Too long
BLOCK_SIZE = 250
L = 64
N = L * L
NR_EXCHANGES = 5
BEGIN_DISCARD = 50
T = 250
SIM_R = 1                   #TODO SIM_R = 100 Too long
TEXTE =1


def main(ticker='^FCHI') -> None:
    """ Simulation of the market 'ticker'

    Args:
        ticker (str, optional): ticker from yfinance (market to simulate). Defaults to '^FCHI'.
    """
    
    rng = np.random.default_rng()
    returns = get_returns(ticker)
    lastprice = returns[-1]
    M = np.zeros((R, NR_STATS))         #matrix R lines and 7 columns (sigma, kurtosis ...)

    #computes R simulation with bootstrap sample and computes stats of the sample
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

    
    #already optimized: macroeconomic source, a source related neighborhood, an idiosyncratic source
    beta = np.array([1.73058, 1.04878, 0.0651077, 1603.94])    
    
    #Estimation of different bootstrap sample
    estimations = [Estimation(r, M, beta, lastprice) for r in range(R)]

    #Creation pool of threads
    with ThreadPoolExecutor() as executor:
        for r in range(1, R):
            executor.submit(estimations[r].estimation_task())
            
    #All tasks done
    

    # #show new values of beta (average, 5%, median, 95% ...)
    # for j in range(NR_PARAMS):
    #     tmp = np.array([estimations[r].beta[j] for r in range(R)])
    #     tmp.sort()
    #     print(f"{j}, moyenne = {stat.mean(tmp)}, 5% = {tmp[int(0.05 * R)]},  médiane = {tmp[int(0.5 * R)]}, 95% = {tmp[int(0.95 * R)]}")
        

if __name__ == "__main__":
    main()


