%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-np.pi, np.pi, 201)
plt.plot(x, np.cos(1*x))
plt.plot(x, np.cos(5*x))
plt.show
