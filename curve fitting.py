import numpy as np
from scipy.optimize import curve_fit

def exponential_function(x, a, b):
  return a * np.exp(b * x)
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 8, 16, 32]) 

popt, pcov = curve_fit(exponential_function, x, y)
print("Fitted parameters:", popt) 

fitted_curve = exponential_function(x, *popt)  
