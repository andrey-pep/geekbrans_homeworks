import numpy as np
from pylab import *
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def Q(x, y, z):
    return (x**2 + y**2 + z**2)

fig = figure()
ax = Axes3D(fig)

x = np.linspace(-20,20,201)
y = np.linspace(-20,20,201)
X, Y = np.meshgrid(x, y)
Z1 = Q(X, Y, (x + 2 * y - 1))
Z2 = Q(X, Y, (-4 * x + 2.5 * y + 6))

surf = ax.plot_surface(X, Y, Z1, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
surf2 = ax.plot_surface(X, Y, Z2, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
plt.grid(True)
plt.show()

A = np.array([[1,2,-1], [8,-5,2]])
B = np.array([1,12])
np.linalg.lstsq(A,B, rcond=None)
