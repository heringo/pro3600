import numpy as np
from itertools import accumulate
from random import randint
from functools import reduce

def debug(arg):
    print(f"{arg} \t {arg}")

def one_draw_from_moving_block_bootstrap(rng, x, block_size):
    '''
    'rng' : a random number generator
    'x' : a time series data (a list or array)
    'block_size' : the siwze of the block to be used in the moving block bootstrap method
    
    '''

    assert len(x) > block_size                              #check if the length of time data is greater than block_size
    index = lambda: randint(0, len(x) - block_size)         #generate random number between 0 and x - block_size to select random starting points for blocks
    blocks_nr = int(len(x) / block_size + 0.5)              #calculate the number of block
    tmp = []                                                #to store concatenated blocks

    for i in range(blocks_nr):                              
        start = index()
        tmp.extend(x[start:start+block_size])

    return tmp

def main():
    rng = np.random.default_rng()
    random_normal = rng.normal()
    T = 1000
    rho = 0.5
    mu = 1

    # Estimation de la variance de l'estimateur de _1 pour un AR1 par simulation.
    R = 100000
    rho_1 = np.zeros(R)

    for r in range(R):
        x = np.zeros(T)
        x_m1 = mu / (1. - rho)

        for t in range(T):
            xx = rho * x_m1 + mu + random_normal
            x[t] = xx
            x_m1 = xx

        xb = np.mean(x)
        x -= xb
        rho_1[r] = np.inner(x[1:], x[:-1]) / np.inner(x, x)

    m = np.mean(rho_1)
    s2 = np.inner(rho_1, rho_1) / R
    print(m)
    print(s2 - m*m)
    print(1. / T)

    # Estimation de la variance de l'estimateur de _1 pour un AR1 par bootstrap.
    x = np.zeros(T)
    x_m1 = mu / (1. - rho)

    for t in range(T):
        xx = rho * x_m1 + mu + random_normal
        x[t] = xx
        x_m1 = xx

    R = 100000
    debug(rho)
    debug(1. / T)

    for number in range(2, 11):
        rho_1 = np.zeros(R)

        for r in range(R):
            xx = one_draw_from_moving_block_bootstrap(rng, x, T // number)
            xxb = np.mean(xx)
            xx -= xxb
            rho_1[r] = np.inner(xx[1:], xx[:-1]) / np.inner(xx, xx)

        m = np.mean(rho_1)
        s2 = np.inner(rho_1, rho_1) / R
        print(f"{number} \t {T // number} \t {m} \t {s2 - m*m}")

if __name__ == "__main__":
    main()
