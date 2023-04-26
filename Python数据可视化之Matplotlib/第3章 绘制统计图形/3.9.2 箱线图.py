import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.rcParams["font.sans-serif"] = ["FangSong"]
mpl.rcParams["axes.unicode_minus"] = False

testA = np.random.randn(5000)
testB = np.random.randn(5000)

testList = [testA,testA]
labels = ["随机数生成器AlphaRM","随机数生成器BetaRM"]
colors = ["#1b9e77","#d95f02"]

whis = 1.6
width = 0.35

'''
函数签名: plt.boxplot()
testList: 绘制箱线图的输入数据
whis: 四分位间距的倍数,用来确定箱须包含数据的范围的大小
widths: 设置箱体的宽度
sym: 离群值的标记样式
labels: 绘制每一个数据集的刻度标签
patch_artist: 是否给箱体添加颜色
'''
bplot = plt.boxplot(testList,whis=whis,widths=width,sym="o",labels=labels,patch_artist=True)

for pathch,color in zip(bplot["boxes"],colors):
    pathch.set_facecolor(color)

plt.ylabel("随机数值")
plt.title("生成器抗干扰能力的稳定性比较")

plt.grid(axis="y",ls=":",lw=1,color="gray",alpha=0.4)

plt.show()