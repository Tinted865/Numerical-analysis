import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline

# Generate some data
x = np.linspace(0, 10, 10)
y = np.sin(x)

# Perform spline interpolation
spl = UnivariateSpline(x, y)
x2 = np.linspace(0, 10, 400)
y2 = spl(x2)

# Plot the data and the spline
plt.scatter(x, y, label='Data')
plt.plot(x2, y2, label='Spline interpolation', color='red')
plt.legend()
plt.show()
