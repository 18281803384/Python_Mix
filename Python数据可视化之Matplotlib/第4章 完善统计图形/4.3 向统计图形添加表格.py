import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.rcParams["font.sans-serif"] = ["FangSong"]
mpl.rcParams["axes.unicode_minus"] = False

labels = ["A难度水平","B难度水平","C难度水平","D难度水平"]

students = [0.35,0.15,0.20,0.30]

explode = (0.1,0.1,0.1,0.1)

colors = ["#377eb8","#4daf4a","#984ea3","#ff7f00"]

plt.pie(students,explode=explode,labels=labels,autopct="%1.1f%%",startangle=45,shadow=True,colors=colors)

plt.title("选择不同难度测试试卷的学生百分比")

colLabels = ["A难度水平","B难度水平","C难度水平","D难度水平"]
rowLabels = ["学生选择试卷人数"]
studentValues = [[350,150,200,300]]
colColors = ["#377eb8","#4daf4a","#984ea3","#ff7f00"]

'''
函数签名: plt.tabel()
cellText: 表格的数值,将源数据按照行进行分组,每组数据放在列表里存储,所有组数据再放在列表里存储。
colWidths: 表格每列的宽度。
colLabels: 表格每列的列名称。
colColors: 表格每列的列名称所在单元格的颜色。
rowLabels: 表格每行的行名称。
rowLoc: 表格每行的行名称对齐位置,可以左对齐、居中和右对齐。
loc: 表格再画布中的位置。
'''
plt.table(cellText=studentValues,
        cellLoc="center",
        colWidths=[0.1] * 4,
        colColours=colColors,
        rowLabels=rowLabels,
        rowLoc="center",
        loc="bottom")

plt.show()
