import numpy as np

b = np.arange(24).reshape(2,12)
print(b)

# 数组的维度
print( b.ndim )

# 数组的总个数
print( b.size )

# 数组中的元素在内存中所占的字节数
print( b.itemsize )

# 查看数组所占的存储空间
print( b.nbytes )
print( b.size * b.itemsize )

b.resize(6,4)
print(b)
# 对数组进行转置
print( b.T )

# 负数构成的数组
b = np.array([1.j + 1, 2.j + 3])
print(b)

# 给出复数数组的实部
print( b.real )

# 给出复数数组的虚部
print( b.imag )

# 查看数据类型
print( b.dtype )
print( b.dtype.str )

b = np.arange(4).reshape(2,2)
print(b)
f = b.flat
print(f)
# flat遍历多维数组的元素,然后可以直接获取数组元素
print( b.flat[2] )

# 获取多个元素
print( b.flat[[1,3]] )

# flat属性是一个可赋值的属性
b.flat = 7
print(b)

b.flat[[1,3]] = 1
print(b)