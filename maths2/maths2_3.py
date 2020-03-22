#### часть 1 и 2, для окружности задаются одинаковые a и b
%matplotlib inline
import numpy as np
import math
import matplotlib.pyplot as plt
x = []
y1 = []
y2 = []
a = 5
b = 10
x0 = 3
y0 = 0
accuracy = 0.1
for x_ in np.arange(x0 - a, x0 + a + 1, accuracy):
    last = 0
    if(x_ > x0 + a):
        x_ = x0 + a
        last = 1
    x.append(x_)
    y1.append(math.sqrt(math.pow(b,2)*(1 - math.pow((x_ - x0),2) / math.pow(a,2))) - y0)
    y2.append(-math.sqrt(math.pow(b,2)*(1 - math.pow((x_ - x0),2) / math.pow(a,2))) - y0)
    if(last):
        break
plt.plot(x,y1)
plt.plot(x,y2)

#### часть 3
x1 = []
x2 =[]
y = []
a = 5
b = 5
x0 =0
y0 = 5
accuracy = 0.1
for y_ in np.arange(y0 - b, y0 + b, accuracy):
    y.append(y_)
    x1.append(math.sqrt(math.pow(a,2)*(1 + math.pow((y_ - y0),2) / math.pow(b,2))) - x0)
    x2.append(-math.sqrt(math.pow(a,2)*(1 + math.pow((y_ - y0),2) / math.pow(b,2))) - x0)
plt.plot(x1,y)
plt.plot(x2,y)
