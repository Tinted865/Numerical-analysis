import numpy as np
import matplotlib.pyplot as plt

def trapezoidal_rule(f, a, b, n):
    x = np.linspace(a, b, n+1)
    y = f(x)
    h = (b - a) / n
    integral = (h / 2) * (y[0] + 2 * np.sum(y[1:-1]) + y[-1])
    return integral
def f(x):
    return np.sin(x)
a = 0
b = np.pi
n = 10
result = trapezoidal_rule(f, a, b, n)
print(f"Approximate value of the integral using the trapezoidal rule: {result}")
x = np.linspace(a, b, 1000)
y = f(x)
plt.plot(x, y, label='f(x)')

x_trap = np.linspace(a, b, n+1)
y_trap = f(x_trap)
for i in range(n):
    plt.fill([x_trap[i], x_trap[i], x_trap[i+1], x_trap[i+1]], [0, y_trap[i], y_trap[i+1], 0], 'b', edgecolor='r', alpha=0.2)

plt.title('Trapezoidal Rule Approximation')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.show()
