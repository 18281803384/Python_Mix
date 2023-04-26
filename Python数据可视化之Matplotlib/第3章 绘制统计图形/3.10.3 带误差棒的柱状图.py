import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.rcParams["font.sans-serif"] = ["FangSong"]
mpl.rcParams["axes.unicode_minus"] = False

x = np.arange(5)
y = [100,68,79,91,82]
std_err = [7,2,6,10,5]

error_attri = dict(elinewidth=2,ecolor="black",capsize=3)

plt.bar(x,y,
        color="c",
        width=0.6,
        align="center",
        yerr=std_err,
        error_kw=error_attri,
        tick_label=["园区1","园区2","园区3","园区4","园区5"])

plt.xlabel("芒果种植区")
plt.ylabel("收割量")

plt.title("不同芒果种植区的单词收割量")

plt.grid(True,axis="y",ls=":",color="gray",alpha=0.2)

plt.show()