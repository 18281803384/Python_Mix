import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams["font.sans-serif"]=["FangSong"]
mpl.rcParams["axes.unicode_minus"]=False

x = [1,2,3,4,5,6,7,8]
y = [3,1,4,5,8,9,7,2]

'''
函数功能: 在y轴上绘制定性数据的分布特征,用于绘制条形图
调用函数: plt.bar(x,y)
x: 标示在y轴上的定性数据的类别
y: 每种定性数据的类别的数量
'''
plt.barh(x,y,align="center",color="c",tick_label=["q","a","c","e","r","j","b","p"],hatch="/")

plt.xlabel("箱子编号")
plt.ylabel("箱子重量(kg)")

plt.show()