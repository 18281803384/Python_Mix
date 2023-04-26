import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.05,10,1000)
y = np.sin(x)

plt.plot(x,y,ls="-.",lw=2,c="c",label="plot rigure")

plt.legend()

'''
函数功能: 添加图形内容细节的无指向型注释文本
调用签名: plt.text(x,y,string,weight="hold",color="b")
x: 注释文本内容所在位置的横坐标
y: 注释文本内容所在位置的纵坐标
string: 注释文本的内容
weight: 注释文本内容粗细风格
color: 注释文本内容的字体颜色
'''
plt.text(3.10,0.09,"y=sin(x)",weight="bold",color="b")

plt.show()