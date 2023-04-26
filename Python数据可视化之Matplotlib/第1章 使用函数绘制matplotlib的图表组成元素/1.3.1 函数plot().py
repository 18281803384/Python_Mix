import matplotlib.pyplot as plt
import numpy as np

# 表示在0.5至10之间均匀地取100个数
x = np.linspace(0.5,10,100)
y = np.cos(x)

'''
函数功能: 展现变量的趋势变化
调用签名: plt.plot(x,y,ls="-",lw=2,c="c",label="plot rigure")
x: x轴上的数值
y: y轴上的数值
ls: 折线图的线条风格
lw: 折线图的线条宽度
c: 折线图的线条颜色
label: 标记图形内容的标签文本
'''
plt.plot(x,y,ls="-",lw=2,c="c",label="cos(x)")

plt.legend()
plt.show()
