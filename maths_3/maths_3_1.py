%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
import math
x = np.linspace(-np.pi, np.pi, 201)
a = np.random.randint(np.pi, size=(1, 3))
b = np.random.randint(10, size=(1, 3))
k = np.random.randint(10, size=(1, 3))
for i in range(0,3):
    plt.plot(x, k[0][i] * np.cos(x - a[0][i]) + b[0][i])
plt.show
