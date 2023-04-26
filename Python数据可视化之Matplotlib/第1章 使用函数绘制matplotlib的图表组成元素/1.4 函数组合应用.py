import matplotlib.pyplot as plt
import numpy as np

# 定义数据
x = np.linspace(0.05,100,1000)
print(x)
y = np.sin(x)
y1 = np.random.rand(1000)

# scatter figure
plt.scatter(x,y1,c="0.25",label="scatter figure")

# plot figure
plt.plot(x,y,ls="--",lw=2,label="plot figure")

for spine in plt.gca().spines.keys():
    plt.gca().spines[spine].set_color("none")
plt.gca().xaxis.set_ticks_position("bottom")
plt.gca().yaxis.set_ticks_position("left")

# 设置x,y轴的数值显示范围
plt.xlim(0.0,4.0)
plt.ylim(-3.0,3.0)

# 设置x,y轴标签文本
plt.ylabel("y_axis")
plt.xlabel("x_axis")

# 绘制刻度线的网格线
plt.grid(True,ls=":",color="r")

# 设置x,y轴的水平参考线
plt.axhline(y=0.0,c="r",ls="--",lw=2)
plt.axvline(x=2.0,c="r",ls="--",lw=2)

# 绘制x,y轴的参考区域
plt.axhspan(ymin=-1.0,ymax=1.0,facecolor="y",alpha=.3)
plt.axvspan(xmin=1.5,xmax=2.5,facecolor="y",alpha=.3)

# 添加图形内容细节的无指向型注释文本
plt.text(3.5,-2.7,"'|' is tickline",weight="bold",color="b")
plt.text(3.5,-2.95,"3.5 is ticklabel",weight="bold",color="b")

# 添加图像内容细节的指向型注释文本
plt.annotate("maximum",xy=(np.pi/2,1.0),xytext=((np.pi/2)-0.2,1.5),weight="bold",color="r",arrowprops=dict(arrowstyle="->",connectionstyle="arc3",color="r"))

# 为图像内容添加标签
plt.title("atructure of matplotlib")

# 定义文本标签图例
plt.legend(loc="lower left")

# 显示图像
plt.show()

