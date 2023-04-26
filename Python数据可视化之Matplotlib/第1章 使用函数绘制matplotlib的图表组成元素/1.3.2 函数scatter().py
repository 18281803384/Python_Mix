import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.5,10,1000)
# rand函数可以返回一个或一组服从“0~1”均匀分布的随机样本值。随机样本取值范围是[0,1)，不包括1
y = np.random.rand(1000)

'''
函数功能: 寻找变量之间的关系
调用签名: plt.scatter(x,y,c="b",label="sactter figure")
x: x轴上的数值
y: y轴上的数值
c: 散点图中的标记的颜色
label: 标记图形内容的标签文本
'''
plt.scatter(x,y,label="sactter figure")


plt.legend()
plt.show()