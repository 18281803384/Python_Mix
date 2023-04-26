import numpy as np

A = np.eye(2)
print(A)

B = 2 * A
print(B)

# bmat函数从两个小矩阵创建一个分块复合矩阵
print( np.bmat("A B; A B") )