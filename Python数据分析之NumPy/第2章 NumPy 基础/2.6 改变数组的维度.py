import numpy as np

b = np.arange(24).reshape(2,3,4)
print(b)

# ravel函数完成数据的展平,只是返回数组的一个视图(view)
print( b.ravel() )

# flatten函数完成数据的展平,会请求分配内存来保存结果
print( b.flatten() )

# shape函数用正整数元组来设置数组的维度
b.shape = (6,4)
print(b)

# transpose函数转置数组
print( b.transpose() )

# resize函数改变维度,直接修改所操作的数组
b.resize((2,12))
print(b)