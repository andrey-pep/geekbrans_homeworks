import numpy as np
import itertools
import math

#3.1
k, n = 0, 100
a = np.random.randint(0, 2, n)
b = np.random.randint(0, 2, n)
c = np.random.randint(0, 2, n)
d = np.random.randint(0, 2, n)
x = a + b + c + d
for i in range(0, n):
    if x[i] == 2:
        k = k + 1
#print(a, b, c, d)
#print(x)
print(k, n, k/n)
n = 4
C = math.factorial(n) / pow(math.factorial(n/2), 2)   #после преобразований сократилось, т.к. k = n / 2
p = C / math.pow(2,n)
print(p)
