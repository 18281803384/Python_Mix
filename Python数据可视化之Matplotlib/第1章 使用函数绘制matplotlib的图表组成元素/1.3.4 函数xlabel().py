import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.05,10,1000)
y = np.sin(x)

plt.plot(x,y,ls="-.",lw=2,c="c",label="plot figure")

plt.legend()

'''
函数功能: 设置x轴的标签文本
调用签名: plt.xlabel(string)
string：标签文本内容
平移性: 上面的函数功能，调用签名和参数说明同样可以平移到函数ylabel()上
'''
plt.xlabel("x-axis")
plt.ylabel("y-axis")

plt.show()