### две параллельных плоскости

%matplotlib inline
import numpy as np
from pylab import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = figure()
ax = Axes3D(fig)
X1 = np.arange(-5, 5, 0.5)
Y1 = np.arange(-5,5,0.5)
X1,Y1 = np.meshgrid(X1, Y1)
Z1 = 2 * X1 + 5 * Y1
Z2 = 2 * X1 + 5 * Y1 + 60
ax.plot_wireframe(X1, Y1, Z1)
ax.plot_wireframe(X1, Y1, Z2)
show()

### две поверхности второго порядка
%matplotlib inline
import numpy as np
from pylab import *
import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d import Axes3D
fig = figure()
ax = Axes3D(fig)
fig2 = figure()
ax2 = Axes3D(fig2)
X1 = np.arange(-5, 5, 0.5)
Y1 = np.arange(-5,5,0.5)
X1,Y1 = np.meshgrid(X1, Y1)
Z1 = 2 * X1 * X1 + 5 * Y1 * Y1
Z2 = np.sqrt(X1**2 + Y1**2)
ax.plot_surface(X1, Y1, Z2)
ax2.plot_surface(X1, Y1, Z1)
show()
