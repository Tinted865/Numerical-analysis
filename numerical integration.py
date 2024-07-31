import numpy as np
from scipy.integrate import quad

def f(x):
    return x**2

result, error = quad(f, 0, 1)
print(result)  # Output: 0.3333333333333333