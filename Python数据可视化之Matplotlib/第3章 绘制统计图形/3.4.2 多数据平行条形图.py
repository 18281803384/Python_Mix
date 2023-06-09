import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.rcParams["font.sans-serif"] = ["FangSong"]
mpl.rcParams["axes.unicode_minus"] = False

x = np.arange(5)
y = [6,10,4,5,1]
y1 = [2,6,3,8,5]

bar_width = 0.35
tick_label = ["A","B","C","D","E"]

plt.barh(x,y,bar_width,color="c",align="center",label="班级A",alpha=0.5)
plt.barh(x+bar_width,y1,bar_width,color="b",align="center",label="班级B",alpha=0.5)

plt.xlabel("测试难度")
plt.ylabel("试卷份数")

plt.yticks(x+bar_width/2,tick_label)

plt.legend()

plt.show()