import numpy as np

b = np.array([1.j + 1, 2.j + 3])
print(b)
print(b.shape)

# tolist函数把NumPy数组换成Python列表
print( b.tolist() )

# astype函数可以在转换数组时指定数据类型
b.astype("complex")
print(b)