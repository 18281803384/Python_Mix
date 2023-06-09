import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.rcParams["font.sans-serif"] = ["FangSong"]
mpl.rcParams["axes.unicode_minus"] = False

x = np.linspace(-2 * np.pi,2 * np.pi,200)
y = np.sin(x)
y1 = np.cos(x)

plt.plot(x,y,label=r"$\sin(x)$")
plt.plot(x,y1,label=r"$\cos(x)$")

plt.legend(loc="lower left")

plt.title("正弦函数和余弦函数的折线图")

plt.show()