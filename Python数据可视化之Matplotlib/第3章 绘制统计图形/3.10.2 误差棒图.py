import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.1,0.6,10)
y = np.exp(x)

error = 0.05 + 0.15 * x

lower_error = error
upper_error = 0.3 * error
error_limit = [lower_error,upper_error]

'''
函数签名: plt.errorbar()
x,y: 数据点的位置
yerr: 单一数值的非对称形式误差范围
fmt: 数据点的标记样式和数据点标记的连接线样式
ecolor: 误差棒的线条颜色
elinewidth: 误差棒的线条粗细
ms: 数据点的大小
mfc: 数据点的标记颜色
mec: 数据点的标记边缘颜色
capthick: 误差棒边界横杠的厚度
capsize: 误差棒边界横杠的大小
'''
plt.errorbar(x,y,yerr=error_limit,fmt=":o",ecolor="y",elinewidth=4,ms=5,mfc="c",mec="r",capthick=1,capsize=2)

plt.xlim(0,0.7)

plt.show()