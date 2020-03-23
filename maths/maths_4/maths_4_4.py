%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
np.seterr(divide='ignore', invalid='ignore')

def f1(x):
    return (np.sin(x))

k = 1
a_arr =  np.linspace(0.01, 0.02, 100)
y_arr = []
# x1 = []
for k in range(-5,5):
    x1 = []
    a1 = []
    for a in a_arr:
        x_ = np.pi * k / a
        if(x_ > 100 and x_ < 500):
            x1.append(x_)
            a1.append(a)
    plt.plot(x1, a1)
