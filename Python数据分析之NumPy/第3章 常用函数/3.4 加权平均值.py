import numpy as np

# 计算成交量 average 加权平均值函数
c, v = np.loadtxt("file/data.csv", delimiter=',', usecols=(6, 7), unpack=True)
print(c, v)
vwap = np.average(c, weights=v)
print("VWAP = ", vwap)

# mean 算术平均值函数
print( "mean = ", np.mean(c) )

# 时间加权平均值
t = np.arange(len(c))
print("twap = ", np.average(c, weights=v))

