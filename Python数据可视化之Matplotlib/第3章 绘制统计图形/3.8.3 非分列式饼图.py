import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.rcParams["font.sans-serif"] = ["FangSong"]
mpl.rcParams["axes.unicode_minus"] = False

labels = "A难度水平","B难度水平","C难度水平","D难度水平"

students = [0.35,0.15,0.20,0.30]

colors = ["#377eb8","#4daf4a","#984ea3","#ff7f00"]

plt.pie(students,labels=labels,autopct="%3.1f%%",startangle=45,pctdistance=0.7,labeldistance=1.2,colors=colors)

plt.title("选择不同难度测试试卷的学生百分比")

plt.show()
