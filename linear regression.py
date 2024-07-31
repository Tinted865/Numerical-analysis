import numpy as np
import matplotlib.pyplot as plt
np.random.seed(0)
x = np.linspace(0, 10, 100)
y = 2.5 * x + np.random.normal(0, 1, 100)
A = np.vstack([x, np.ones(len(x))]).T
m, c = np.linalg.lstsq(A, y, rcond=None)[0]
plt.scatter(x, y, label='Data')
plt.plot(x, m*x + c, label='Fitted line', color='red')
plt.legend()
plt.show()
