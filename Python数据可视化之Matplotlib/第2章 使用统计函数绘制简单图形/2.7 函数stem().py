import  matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.5,2*np.pi,20)
y = np.random.randn(20)

'''
函数功能: 绘制离散有序数据，用于绘制棉棒图
调用签名: plt.stem(x,y)
x: 指定棉棒的x轴基线上的位置
y: 绘制棉棒的长度
linefmt: 棉棒的样式
markefmt: 棉棒末端的样式
basefmt: 指定基线的样式
'''
plt.stem(x,y,linefmt="-.",markerfmt="o",basefmt="-")

plt.show()