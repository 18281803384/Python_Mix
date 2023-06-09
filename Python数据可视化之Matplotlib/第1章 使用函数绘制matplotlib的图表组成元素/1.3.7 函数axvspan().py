import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.05,10,1000)
y = np.sin(x)

plt.plot(x,y,ls="-.",lw=2,c="c",label="plot rigure")

plt.legend()

'''
函数功能: 绘制垂直于x轴的参考区域
调用签名: plt.axvspan(xmin=1.0,xmax=2.0,facecolor="y",alpha=0.3)
xmin: 参考区域的起始位置
xmax: 参考区域的终止位置
facecolor: 参考区域的填充颜色
alpha: 参考区域的填充颜色的透明度
平移性: 上面的函数功能，调用签名和参数说明同样可以平移到函数axhspan()上
'''
plt.axvspan(xmin=4.0,xmax=6.0,facecolor="y",alpha=0.3)
plt.axhspan(ymin=0.0,ymax=0.5,facecolor="y",alpha=0.3)

plt.show()