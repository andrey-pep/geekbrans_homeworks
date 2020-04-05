import numpy as np
import matplotlib.pyplot as plt
import scipy 
import scipy.linalg  
​
A = np.array([[1,2,3], [2,16,21], [4,28,73]])
P, L, U = scipy.linalg.lu(A)
print(P)
print(L)
print(U)
print("solving")
B = np.array([[1,2,3], [3,2,5], [7,1,5]])
for b in B:
    Y = np.linalg.solve(L, b)
    print(np.linalg.solve(U, Y))
    
#[[0. 1. 0.]
# [0. 0. 1.]
# [1. 0. 0.]]
#[[ 1.    0.    0.  ]
# [ 0.25  1.    0.  ]
# [ 0.5  -0.4   1.  ]]
#[[  4.    28.    73.  ]
# [  0.    -5.   -15.25]
# [  0.     0.   -21.6 ]]
#solving
#[ 2.24074074  0.10185185 -0.14814815]
#[ 1.92592593  0.31481481 -0.18518519]
#[ 0.52777778  0.31944444 -0.05555556]
