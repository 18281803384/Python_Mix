import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams["font.sans-serif"] = ["FangSong"]
mpl.rcParams["axes.unicode_minus"] = False

x = [1,2,3,4,5]
y = [6,10,4,5,1]
y1 = [2,6,3,8,5]

plt.barh(x,y,align="center",color="#66c2a5",tick_label=["A","B","C","D","E"],label="班级A")
plt.barh(x,y1,align="center",left=y,color="#8da0cb",label="班级B")

plt.ylabel("测试难度")
plt.xlabel("试卷份数")

plt.legend()

plt.show()
