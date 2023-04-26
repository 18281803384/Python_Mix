import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

a = np.random.randn(100)
b = np.random.randn(100)

'''
函数功能: 二维数据借助气泡大小展示三维数据,用于绘制气泡图
调用签名: plt.scatter(x,y)
x: x轴上的数值
y: y轴上的数值
s: 散点标记的大小
c: 散点标记的颜色
cmap: 将浮点数映射成颜色的颜色映射表
'''
plt.scatter(a,b,s=np.power(10*a+20*b,2),c=np.random.rand(100),cmap=mpl.cm.RdYlBu,marker="o")

plt.show()