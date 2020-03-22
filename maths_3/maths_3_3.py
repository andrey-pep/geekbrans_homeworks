%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
import math

def transform(r, a):        #перевод координат
    x = r * math.sin(a)
    y = r * math.cos(a)
    return x,y
    
R = 10                      #рисуем окужность по полярным координатам (если правильно понял задание :))
alpha = np.pi / 2
x = []
y = []
t = np.linspace(-np.pi, np.pi, 201)
for p in t:
    x_, y_ = transform(R, p)
    x.append(x_)
    y.append(y_)
plt.plot(x, y)
plt.show()

r1 = 7                    рисуем график отрезка
alpha1 = np.pi/5
r2 = 16
alpha2 = np.pi/9
x_1, y_1 = transform(r1, alpha1)
x_2, y_2 = transform(r2, alpha2)
x = [x_1, x_2]
y = [y_1, y_2]
plt.plot(x, y)
plt.show()
