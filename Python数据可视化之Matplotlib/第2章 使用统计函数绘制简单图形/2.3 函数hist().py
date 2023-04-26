import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.rcParams["font.sans-serif"]=["FangSong"]
mpl.rcParams["axes.unicode_minus"]=False

boxWeight = np.random.randint(0,10,100)
x = boxWeight

bins = range(0,11,1)

'''
函数功能: 在x轴上绘制定性数据的分布特征,用于绘制直方图
调用函数: plt.hist(x,y)
x: 在x轴上绘制箱体的定量数据输入值
'''
plt.hist(x,bins=bins,color='g',histtype='bar',rwidth=1,alpha=0.6)

plt.xlabel("箱子重量(kg)")
plt.ylabel("箱子数量(个)")

plt.show()