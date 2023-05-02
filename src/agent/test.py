import numpy as np
from scipy.optimize import least_squares

# Define the Rosenbrock function
def rosenbrock(x):
    return np.array([10 * (x[1] - x[0]**2), (1 - x[0])])

# Starting point
x0 = np.array([2, 2])

# Use the LM algorithm to minimize the Rosenbrock function
res = least_squares(rosenbrock, x0, method='lm')

print(res.x)  # prints the solution
