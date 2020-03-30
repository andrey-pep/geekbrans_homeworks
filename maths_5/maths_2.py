%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

#2.1
black_nums = [2, 4, 6, 8, 10, 11, 13 ,15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
red_nums = [1, 3 ,5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]

red_s = 0
black_s = 0
zero_s = 0
s = 0

for i in range(0,100):
    x = np.random.randint(0, 37)
#     print(x)
    if (x in black_nums):
        black_s += 1
    elif (x in red_nums):
        red_s += 1
    elif (x == 0):
        zero_s +=1
    else:
        print(x)
    s += 1

p_black = black_s / s
p_red = red_s / s
p_zero = zero_s / s

print ("P(black) = " + str(p_black))
print ("P(red) = " + str(p_red))
print ("P(zero) = " + str(p_zero))
print ("P(balck + red + zero)=" + str(p_black + p_red + p_zero))
if (p_black + p_red + p_zero == 1):
    print("ЧТД")
else:
    print("Ouuuups")
    
#2.2
s_x = []
for i in range(0, 10):
    x = np.random.rand(10)
    s_x.append(sum(x))
n, bins, patches = plt.hist(s_x, 10)
plt.show()
