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
    rng = np.random.default_rng() #générateur de nombre aléatoire
    random_normal = rng.normal()
    
    #paramètre du modèle AR1
    T = 1000     #longueur de la série temporelle simulée
    rho = 0.5    #coefficient de corrélation autorégressive
    mu = 1       #mu est la moyenne de la série temporelle 

    #Estimmation de la variance de l'estimateur de l'autocorrélation d'un processus autorégressif d'ordre 1 (AR1)
    R = 100000   #nombre de simulation
    rho_1 = np.zeros(R) 

    for r in range(R):
        x = np.zeros(T)
        x_m1 = mu / (1. - rho) #valeur initiale de la série temporelle

        #Exécution de la simulation de la série temporelle AR1
        for t in range(T):
            xx = rho * x_m1 + mu + random_normal
            x[t] = xx
            x_m1 = xx

        #Calcul l'estimateur de l'autocorrélation de la série temporelle de x
        xb = np.mean(x)
        x -= xb      #pour centrer la série temporelle
        rho_1[r] = np.inner(x[1:], x[:-1]) / np.inner(x, x)

    m = np.mean(rho_1)
    s2 = np.inner(rho_1, rho_1) / R
    print(m)            #Moyenne de l'estimateur
    print(s2 - m*m)     #Variance de l'estimateur
    print(1. / T)

    # Estimation de la variance de l'estimateur d'autocrrélation à partir d'un processus AR1 grâce à la méthode bootstrap
    x = np.zeros(T)
    x_m1 = mu / (1. - rho)

    for t in range(T):
        xx = rho * x_m1 + mu + random_normal
        x[t] = xx
        x_m1 = xx

    R = 100000         #Nombre de répétitions de la méthode bootstrap
    print(rho)         
    print(1. / T)

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
        #Affichage de la moyenne et la variance de la distribution des estimateurs d'autocorrélation
        

if __name__ == "__main__":
    main()
