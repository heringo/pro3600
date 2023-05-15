from typing import Iterable, Tuple

import math
import yfinance as yf


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
        

if __name__ == '__main__' :
    compute_stat_interface()