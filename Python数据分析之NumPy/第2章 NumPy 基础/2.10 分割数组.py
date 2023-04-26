import numpy as np

a = np.arange(9).reshape(3,3)
print(a)

# 水平分割,沿水平方向分别分割为3个相同大小的子数组
print( np.hsplit(a,3) )

print( np.split(a,3,axis=1) )

# 垂直分割,沿垂直方向分别分割为3个相同大小的子数组
print( np.vsplit(a,3) )

print( np.split(a,3,axis=0) )

# 深度分割
c = np.arange(27).reshape(3,3,3)
print(c)

print( np.dsplit(c,3) )