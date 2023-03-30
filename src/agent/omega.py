import numpy as np
import random
from typing import List
import math
import pandas as pd

def one_draw_from_moving_block_bootstrap(rng, x, block_size):
    T = x.size
    assert T > block_size
    index = random.randint(0, T - block_size)
    nr_draws = int(T / block_size)
    tmp = np.zeros(T)

    for i in range(nr_draws):
        start = index(rng)
        tmp[i * block_size: (i + 1) * block_size] = x[start: start + block_size]

    remain = T - (nr_draws * block_size)
    start = index(rng)
    tmp[nr_draws * block_size: nr_draws * block_size + remain] = x[start: start + remain]

    return tmp

def get_returns(filename: str) -> np.ndarray:
    data = pd.read_csv(filename, sep="\t", header=None, names=["date", "value"])
    price = data["value"].values

    assert price.size > 1
    returns = np.log(price[1:] / price[:-1])

    return returns

def centered(x: np.ndarray) -> np.ndarray:
    return x - x.mean()

def compute_sigma(x: np.ndarray) -> float:
    T = x.size
    s2 = x.dot(x)
    return math.sqrt(s2 / (T - 1))

def compute_kurtosis(x: np.ndarray) -> float:
    T = x.size
    s2 = x.dot(x)
    s4 = (x * x).dot(x * x)
    sigma2 = s2 / (T - 1)

    return s4 / sigma2 / sigma2 * T * (T + 1) / (T - 1) / (T - 2) / (T - 3) - 3. * (T - 1) * (T - 1) / (T - 2) / (T - 3)

def compute_autocorrelation(x: np.ndarray, lag: int) -> float:
    length = x.size - lag
    s2 = x.dot(x)
    return x[:length].dot(x[lag:]) / s2

def compute_autocorrelation_squares(x: np.ndarray, lag: int) -> float:
    squares = x * x
    centered_squares = squares - squares.mean()
    length = x.size - lag
    s2 = centered_squares.dot(centered_squares)

    return centered_squares[:length].dot(centered_squares[lag:]) / s2

def main():
    rng = random.Random()
    returns = get_returns("CAC40-cours-journalier-cloture.txt")
    R = 100000
    K = 6
    X = np.zeros((R, K))

    for r in range(R):
        x = returns if r == 0 else one_draw_from_moving_block_bootstrap(rng, returns, 250)
        centered_x = centered(x)
        X[r, 0] = compute_sigma(centered_x)
        X[r, 1] = compute_kurtosis(centered_x)
        X[r, 2] = compute_autocorrelation(centered_x, 1)
        X[r, 3] = compute_autocorrelation(centered_x, 10)
        X[r, 4] = compute_autocorrelation_squares(x, 1)
        X[r, 5] = compute_autocorrelation_squares(x, 10)

    average = X.mean(axis=0)
    X_tilde = X - average
    Omega = X_tilde.T.dot(X_tilde) / (R - 1)

    print("size\tkurtosis\t_1\t_10\t_1\t_10")
    print(returns.size, R, K)
    print("average:\n", average)
    print("Omega:\n", Omega)

    Omega_inv = np.linalg.inv(Omega)
    print("Omega_inv:\n", Omega_inv)

if __name__ == "__main__":
    main()

