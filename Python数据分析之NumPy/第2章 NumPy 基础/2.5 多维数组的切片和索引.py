import numpy as np

# reshape函数修改数组的维度
b = np.arange(24).reshape(2,3,4)
print(b.shape)
print(b)

# 第1层 第1行 第1列
print( b[0,0,0] )

# 所有层 第1行 第1列
print( b[:,0,0] )

# 第1层 所有行列
print( b[0] )

# 第1层 所有行列
print( b[0,:,:] )

# 第1层 所有行列
print( b[0,...] )

# 第1层 第2行所有
print( b[0,1] )

# 第1层 第2行所有 中隔地选定元素步长为2
print( b[0,1,::2] )

# 所有层 第2列所有
print( b[...,1] )

# 所有层 第2行所有
print( b[:,1] )

# 第1层 所有行 第2列
print( b[0,:,1] )

# 第1层 最后1列
print( b[0,:,-1] )

# 第1层 最后一列的所有
print( b[0,::-1,-1] )

# 在数组中隔地选定元素
print( b[0,::2,-1] )

# 将第一层和第二层交换
print( b[::-1] )