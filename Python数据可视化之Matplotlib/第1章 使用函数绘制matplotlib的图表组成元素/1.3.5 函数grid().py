import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.05,10,1000)
y = np.sin(x)

plt.plot(x,y,ls="-.",lw=2,c="c",label="plot rigure")

plt.legend()

'''
函数功能: 绘制刻度线的网格线
调用签名: plt.grid(linestyle=":",color="r")
linestyle: 网格线的线条风格
color: 网格线的线条颜色
'''
plt.grid(linestyle=":",color="r")

plt.show()
