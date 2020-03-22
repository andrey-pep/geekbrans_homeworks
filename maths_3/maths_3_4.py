%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
np.seterr(divide='ignore', invalid='ignore')
 
### 1 часть
def eq(p):
    x, y = p
    return ( x**2 - 1, np.exp(x) + x*(1 - y) - 1)

x = np.linspace(-3 * np.pi, 3 * np.pi, 201)
plt.plot(x, f1(x))
plt.plot(x, f2(x))
x1, y1 = fsolve(eq, (1,1))
print(x1, y1)

### 2 часть
def eq2(p):
    x, y = p
    return ( x**2 - 1, np.exp(x) + x*(1 - y) + 0.1  )   #нечестный костыль, todo: нормальное решение

x = np.linspace(-3 * np.pi, 3 * np.pi, 201)
x1, y1 = fsolve(eq2, (1,1))
print(x1, y1)
