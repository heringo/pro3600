from typing import List
import math
from statistics import median

def main():
    with open('CAC40-cours-journalier-ôclture.txt') as file:
        cac = []
        for line in file:
            date, value = line.strip().split()
            cac.append(float(value))
    
    r = [] 
    for t in range(1, len(cac)):
        r.append(math.log(cac[t] / cac[t-1]))
    
    T = len(r)
    rb = sum(r) / T
    minimum = min(r)
    maximum = max(r)
    median_r = median(r)
    
    r_m_rb = []
    for r_t in r:
        r_m_rb.append(r_t - rb)
    
    sigma2 = sum([x**2 for x in r_m_rb]) / (T-1)
    sigma = math.sqrt(sigma2)
    
    tmp4 = sum([x**4 for x in r_m_rb])
    kurtosis = tmp4 / sigma2**2 * T * (T+1) / (T-1) / (T-2) / (T-3) - 3. * (T-1)**2 / (T-2) / (T-3)
    
    tmp2 = sum([x**2 for x in r_m_rb])
    tmp3 = sum([x**3 for x in r_m_rb])
    skewness = tmp3 / sigma2 / sigma * T / (T-1) / (T-2)
    
    standardized_range = (maximum - minimum) / sigma
    
    ds0 = [1, 2, 3]
    ds = [0.125, 0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 3]
    # ls = [1, 2, 3, 4, 5, 10, 20, 40, 70, 100]
    ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, ...]
    
    print("Tableau sur la série brute.\n", end="")
        
    for d in ds0: 
        print('moment ordre d')
        data_brut = []
        
        #rendement à la puissance d
        rd = []
        for rdaily in r:
            rd.append(pow(rdaily,d))
            
        #rendement à la puissance d centrée en zéro
        rd_avg = sum(rd)/len(r)
        rd_central = list(rd)
        for i in range(len(rd_central)):
            rd_central -= rd_avg
        
        #variance de rd_central
        rd_central_var = sum(map(lambda x,y : x * y, rd_central, rd_central))
        
        #autocorrélation avec les lags ls
        for lag in ls :
            rd_central_autocor = sum(map(lambda x, y : x * y, rd_central, rd_central[lag:]))/rd_central_var
            data_brut.append(rd_central_autocor)
            
    print("Tableau sur la série en valeur absolue pour d dans ds0.\n", end="")
        
    for d in ds0: 
        print('moment ordre d')
        data_abs_ds0 = []
        
        #rendement à la puissance d
        rd = []
        for rdaily in r:
            rd.append(pow(abs(rdaily),d))
            
        #rendement à la puissance d centrée en zéro
        rd_avg = sum(rd)/len(r)
        rd_central = list(rd)
        for i in range(len(rd_central)):
            rd_central -= rd_avg
        
        #variance de rd_central
        rd_central_var = sum(map(lambda x,y : x * y, rd_central, rd_central))
        
        #autocorrélation avec les lags ls
        for lag in ls :
            rd_central_autocor = sum(map(lambda x, y : x * y, rd_central, rd_central[lag:]))/rd_central_var
            data_abs_ds0.append(rd_central_autocor)
    
    print("Tableau sur la série en valeur absolue pour d dans ds.\n", end="")
    
    for d in ds: 
        print('moment ordre d')
        data_abs_ds = []
        
        #rendement à la puissance d
        rd = []
        for rdaily in r:
            rd.append(pow(abs(rdaily),d))
            
        #rendement à la puissance d centrée en zéro
        rd_avg = sum(rd)/len(r)
        rd_central = list(rd)
        for i in range(len(rd_central)):
            rd_central -= rd_avg
        
        #variance de rd_central
        rd_central_var = sum(map(lambda x,y : x * y, rd_central, rd_central))
        
        #autocorrélation avec les lags ls et rechercher de tau_star
        tau_star = 0
        for i in len(rd_central) :
            if sum(map(lambda x, y : x * y, rd_central, rd_central[lag:]))/rd_central_var <= 0 :
                tau_star = lag
                break
        print('tau_star = ' + tau_star)
    
    
if __name__ == "__main__":
    main()