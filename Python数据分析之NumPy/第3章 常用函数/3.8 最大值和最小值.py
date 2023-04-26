import numpy as np

# 计算成交量 average 加权平均值函数
h, l = np.loadtxt("file/data.csv", delimiter=',', usecols=(4, 5), unpack=True)

print("最大值 = ", np.max(h))
print("最小值 = ", np.min(l))


# ptp函数返回数组元素最大值和最小值之间的差值
print(np.ptp(h))
print(np.ptp(l))