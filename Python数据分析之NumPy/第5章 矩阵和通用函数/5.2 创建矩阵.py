import numpy as np

# 字符串创建矩阵
A = np.mat('1 2 3; 4 5 6; 7 8 9')
print(A)

# 转置矩阵
print( A.T )

# NumPy数组创建矩阵
B = np.mat(np.arange(9).reshape(3,3))
print(B)