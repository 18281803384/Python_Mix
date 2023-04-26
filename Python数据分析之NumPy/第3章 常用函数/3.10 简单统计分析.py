import numpy as np

c = np.loadtxt("file/data.csv", delimiter=",", usecols=(6,), unpack=True)

# median函数找到中位数
print("中位数 = ", np.median(c))

# msort对数据进行一个升序排列
sorted_close = np.msort(c)
print("升序排列 = ", sorted_close)

# 方差
print( "方差 = ", np.var(c) )