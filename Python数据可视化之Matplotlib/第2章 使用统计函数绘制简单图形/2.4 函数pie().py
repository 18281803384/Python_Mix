import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams["font.sans-serif"] = ["FangSong"]
mpl.rcParams["axes.unicode_minus"] = False

kinds = "简易箱","保温箱","行李箱","密封箱"

colors = ["#e41a1c","#377eb8","#4daf4a","#984ea3"]

soldNums = [0.5,0.45,0.15,0.35]

'''
函数功能: 绘制定性数据的不同类型的百分比
调用签名: plt.pie(x)
x: 定性数据的不同类别的百分比
'''
plt.pie(soldNums,labels=kinds,autopct="%3.1f%%",startangle=60,colors=colors)

plt.title("不同类型箱子的销售数量占比")

plt.show()