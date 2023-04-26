import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.rcParams["font.sans-serif"] = ["FangSong"]
mpl.rcParams["axes.unicode_minus"] = False

time = np.arange(1,11,0.5)
machinPower = np.power(time,2) + 0.7

plt.plot(time,machinPower,linestyle="-",linewidth=2,color="r")

plt.xlim(10,1)

plt.xlabel("使用年限")
plt.ylabel("机器功率")

plt.title("机器损耗曲线")

plt.grid(ls=":",lw=1,color="gray",alpha=0.5)

plt.show()