import  matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.1,0.6,6)
y = np.exp(x)

'''
函数功能: 绘制y轴方向或是x轴方向的误差范围，会用绘制误差棒图
调用签名: plt.errorbar(x,y,yerr=a,xerr=b)
x: 数据点的水平位置
y: 数据点的垂直位置
yerr: y轴方向的数据点的误差计算方法
xerr: x轴方向的数据点的误差计算方法
'''
plt.errorbar(x,y,fmt="bo:",yerr=0.2,xerr=0.02)

plt.xlim(0,0.7)

plt.show()