import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.rcParams["font.sans-serif"] = ["FangSong"]
mpl.rcParams["axes.unicode_minus"] = False

scoresT = np.random.randint(0,100,100)

x = scoresT

bins = range(0,101,10)

'''
调用函数: hist(x,y,bins=bins,color="b",histtype="bar",label="score",rwidth=10)
x: 连续型数据输入值
bins: 用于确定柱体的个数或是柱体边缘范围
color: 柱体的颜色
histtype: 柱体类型
label: 图例内容
rwidth: 柱体宽度
'''
plt.hist(x,bins=bins,color="#377eb8",histtype="bar",rwidth=10)

plt.xlabel("测试成绩")
plt.ylabel("学生人数")

plt.show()