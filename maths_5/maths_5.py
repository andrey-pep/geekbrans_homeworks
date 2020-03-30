%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
import math

n = 100
r = 0.7
x = np.random.rand(n)
y = r*x + (1 - r)*np.random.rand(n)
plt.plot(x, y, 'o')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)

a = (np.sum(x)*np.sum(y) - n*np.sum(x*y))/(np.sum(x)*np.sum(x) - n*np.sum(x*x))
b = (np.sum(y) - a*np.sum(x))/n

A = np.vstack([x, np.ones(len(x))]).T
a1, b1 = np.linalg.lstsq(A, y)[0]
print(a, b)
print(a1, b1)
Xm = np.sum(x) / len(x)
Ym = np.sum(y) / len(y)
R = np.sum((x - Xm) * (y - Ym)) / np.sqrt(np.sum((x - Xm) * (x - Xm)) * np.sum((y - Ym) * (y - Ym)))
print(R)
plt.plot([0, 1], [b, a + b])
plt.show()
