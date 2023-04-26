import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.rcParams["font.sans-serif"] = ["FangSong"]
mpl.rcParams["axes.unicode_minus"] = False

labels = "A难度水平","B难度水平","C难度水平","D难度水平"

students = [0.35,0.15,0.20,0.30]

colors = ["#377eb8","#4daf4a","#984ea3","#ff7f00"]

explode = (0.1,0.1,0.1,0.1)

'''
函数签名: plt.pie()
students: 饼片代表的百分比
explode: 饼片边缘偏离半径的百分比
labels: 标记每份饼片的文本标签内容
autopct: 饼片文本标签内容对应的数值百分比样式
startangle: 从x轴作为起始位置,第一个饼片逆时针旋转的角度
colors: 饼片的颜色
'''
plt.pie(students,explode=explode,labels=labels,autopct="%3.1f%%",startangle=45,shadow=True,colors=colors)

plt.title("选择不同难度测试试卷的学生百分比")

plt.show()
