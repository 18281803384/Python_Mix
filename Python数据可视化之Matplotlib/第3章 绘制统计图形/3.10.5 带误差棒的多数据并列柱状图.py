import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.rcParams["font.sans-serif"] = ["FangSong"]
mpl.rcParams["axes.unicode_minus"] = False

x = np.arange(5)
y1 = [100,68,79,91,82]
y2 = [120,75,70,78,85]
std_err1 = [7,2,6,10,5]
std_err2 = [1,1,4,8,9]

error_attri = dict(elinewidth=2,ecolor="black",capsize=3)

bar_width = 0.4
tick_label = ["园区1","园区2","园区3","园区4","园区5"]

plt.bar(x,y1,
        bar_width,
        color="#87CEEB",
        align="center",
        yerr=std_err1,
        error_kw=error_attri,
        label="2010")

plt.bar(x+bar_width,y2,
        bar_width,
        color="#CD5C5C",
        align="center",
        yerr=std_err2,
        error_kw=error_attri,
        label="2013")

plt.xlabel("芒果种植区")
plt.ylabel("收割量")

plt.xticks(x+bar_width/2,tick_label)

plt.title("不同芒果种植区的单词收割量")

plt.grid(True,axis="y",ls=":",color="gray",alpha=0.2)

plt.show()