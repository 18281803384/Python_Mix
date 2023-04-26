import numpy as np

a = np.arange(9)

print(a)
print( a[3:7] )

# 下标0~7,以2为步长选取元素
print( a[:7:2] )

# 利用负数下标翻转数组
print( a[::-1] )