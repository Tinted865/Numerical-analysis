import numpy as np

def trapezoidal_rule(f, a, b, n):
  h = (b - a) / n
  integral = 0.5 * f(a) + 0.5 * f(b)
  for i in range(1, n):
    integral += f(a + i * h)
  return integral * h

# Example usage
def f(x):
  return np.sin(x)

a = 0.0
b = np.pi  # Integrate from 0 to pi
n = 100  # Increase n for better accuracy

integral_approx = trapezoidal_rule(f, a, b, n)
print("Approximate definite integral of sin(x) from 0 to pi:", integral_approx)
