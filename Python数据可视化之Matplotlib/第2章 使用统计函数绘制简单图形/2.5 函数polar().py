import matplotlib.pyplot as plt
import numpy as np

barSlices = 12

theta = np.linspace(0.0,2*np.pi,barSlices,endpoint=False)
r = 30*np.random.rand(barSlices)

'''
函数功能: 在极坐标轴上绘制折线图,用于绘制极线图
调用签名: plt.polar(theta,r)
theta: 每个标记所在射线与极径的夹角
r: 每个标记到原点的距离
'''
plt.polar(theta,r,color="chartreuse",linewidth=2,marker='*',mfc="b",ms=10)

plt.show()