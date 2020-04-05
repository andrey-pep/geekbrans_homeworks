import numpy as np
import matplotlib.pyplot as plt

A = np.array([[1,2,3], [4,5,6], [7,8,9]])
B = np.array([[12, 2, 1]])
C = np.concatenate((A, B.T), axis=1)
np.linalg.matrix_rank(A, 0.0001), np.linalg.matrix_rank(C, 0.0001)

#(2,3) - ранк матрицы меньше ранка расширенной матрицы, решений 0, меняем матрицу и решаем

import numpy as np
import matplotlib.pyplot as plt

A = np.array([[1,2,3], [4,5,6], [7,8,9]])
B = np.array([[1, 2, 3]])
C = np.concatenate((A, B.T), axis=1)
np.linalg.matrix_rank(A, 0.0001), np.linalg.matrix_rank(C, 0.0001)

#(2,2)
import numpy as np
import matplotlib.pyplot as plt
A = np.array([[1,2,3], [4,5,6], [7,8,9]])
B = np.array([1, 2, 3])
np.linalg.solve(A, B)
#array([-0.23333333,  0.46666667,  0.1       ])
