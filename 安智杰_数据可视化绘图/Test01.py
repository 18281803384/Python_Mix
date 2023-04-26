import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# -----读取数据
Test_Data = open('Test_Data.dat', 'rb') # 以只读二进制模式打开文件
Data = np.frombuffer(Test_Data.read(), np.uint8)    # 二进制文件数据重组为一维数组(列),数据类型为无符号整数uint8（0 ~ 255）
Test_Data.close()   # 关闭已打开的文件

# -----重组数据,【python索引是从0开始】
data = Data.reshape(1046, -1, order="F")    # 将Data一维数组重新划分为(1046,最大列)矩阵,按照列的顺序来填充
data_start = np.where(data[14] == 0)[0].T # 查询出data矩阵15行向量中元素等于0的索引,转置为一维数组(行)
data_end = np.where(data[14] == 31)[0].T
data = data[:, data_start[0]:data_end[-1]+1]  # 查询出data矩阵(所有行,指定列)的矩阵数据

data_start = np.where(data[15] == 0)[0].T # 查询出data矩阵16行向量中元素等于0的索引,转置为一维数组(行)
data_end = np.where(data[15] == 31)[0].T
data = data[:, data_start[0]:data_end[-1]+1]

# -----短距和长距的数据模式处理
Short_distance = np.where(data[12] == 0)[0].T   # 查询出data矩阵13行向量中元素等于0的索引,转置为一维数组(行)
data0 = data[:, Short_distance]  # 查询出data矩阵(所有行,指定列)的矩阵数据
data0 = data0[16:1040, :]   # 查询出data矩阵(17:1040,所有列)的矩阵数据
odd_number = data0[0:data0.shape[0]:2, :]  # 查询data0矩阵中(奇数行,所有列)的矩阵数据
even_number = data0[1:data0.shape[0]:2, :]  # 查询data0矩阵中(偶数行,所有列)的矩阵数据
data0 = odd_number + even_number * 256  # odd_number矩阵数据加上even_number矩阵元素*256的矩阵数据
data0 = np.array(data0, dtype=np.int32) # 更改data0矩阵数据类型,数据类型为整数int32(-2147483648 ~ 2147483647）)
data0 = data0.T # 对data0数组进行转置
# 知识点: 因matlab查询是从'列顺序'查找的,而Python是默认从'行顺序'查找,为了方便理解元素查找,所以这里把数组进行转置,当Python去从'行顺序'时查找时就是按照原数组'列顺序'查找的
data0[data0 > 2 ** 15] = data0[data0 > 2 ** 15] - 2 ** 16   # 查询出data0数组元素大于2^15的元素值替换为data0数组元素大于2^15再减去2^16的元素值
data0 = data0.T # 对data0数组再转置回来
data0 = data0.reshape(512 * 128 * 4, -1, order="F") # 将data0二维数组重新划分为(512 * 128 * 4,最大列)矩阵,按照列的顺序来填充

long_distance = np.where(data[12] == 1)[0].T
data1 = data[:, long_distance]
data1 = data1[16:1040, :]
odd_number = data1[0:data1.shape[0]:2, :]
even_number = data1[1:data1.shape[0]:2, :]
data1 = odd_number + even_number * 256
data1 = np.array(data1, dtype=np.int32)
data1 = data1.T
data1[data1 > 2 ** 15] = data1[data1 > 2 ** 15] - 2 ** 16
data1 = data1.T
data1 = data1.reshape(512 * 128 * 4, -1, order="F")

# -----循环处理短距和长距的数组数据
for i in range(data0.shape[1]): # 循环获取data0数组的列向量 28列,下标0~27
    data0_column = data0[:, i] # 获取data0数组某一列向量

    # 将data0_column数组一分二,TX1为前半列向量,TX2为后半列向量
    TX1 = data0_column[0:int(data0_column.shape[0] / 2)]
    TX2 = data0_column[int(data0_column.shape[0] / 2):data0_column.shape[0]]
    TX1_mode = TX1.reshape(512, -1, order="F")  # 将TX1一维数组重新划分为(512,最大列)矩阵,按照列的顺序来填充
    TX2_mode = TX2.reshape(512, -1, order="F")

    # TX1_mode0_Rx1 数组可绘制二维线图
    TX1_mode0_Rx1 = TX1_mode[:, 0:TX1_mode.shape[1]:4]
    TX1_mode0_Rx2 = TX1_mode[:, 1:TX1_mode.shape[1]:4]
    TX1_mode0_Rx3 = TX1_mode[:, 2:TX1_mode.shape[1]:4]
    TX1_mode0_Rx4 = TX1_mode[:, 3:TX1_mode.shape[1]:4]

    TX2_mode0_Rx1 = TX2_mode[:, 0:TX2_mode.shape[1]:4]
    TX2_mode0_Rx2 = TX2_mode[:, 1:TX2_mode.shape[1]:4]
    TX2_mode0_Rx3 = TX2_mode[:, 2:TX2_mode.shape[1]:4]
    TX2_mode0_Rx4 = TX2_mode[:, 3:TX2_mode.shape[1]:4]

    # TX1_mode_RX11 数组可绘制三维曲面图
    TX1_mode_RX11 = np.fft.fft(TX1_mode0_Rx1, n=512, axis=0)    # 对TX1_mode0_Rx1 数组已列的形式进行傅里叶变换,并指定变换后为(512,最大列)
    TX1_mode_RX11 = TX1_mode_RX11.T # 对TX1_mode_RX11数组进行转置
    TX1_mode_RX11 = np.fft.fft(TX1_mode_RX11, n=128, axis=0)    # 对TX1_mode_RX11 数组已列的形式再进行傅里叶变换,并指定变换后为(128,最大列)
    TX1_mode_RX11 = abs(TX1_mode_RX11)  # 对TX1_mode_RX11 求绝对值
    TX1_mode_RX11 = TX1_mode_RX11[1:125, 0:256] # 对TX1_mode_RX11 数组进行行列切片

    TX1_mode_RX22 = np.fft.fft(TX1_mode0_Rx2, n=512, axis=0)
    TX1_mode_RX22 = TX1_mode_RX22.T
    TX1_mode_RX22 = np.fft.fft(TX1_mode_RX22, n=128, axis=0)
    TX1_mode_RX22 = abs(TX1_mode_RX22)
    TX1_mode_RX22 = TX1_mode_RX22[1:125, 0:256]

    TX1_mode_RX33 = np.fft.fft(TX1_mode0_Rx3, n=512, axis=0)
    TX1_mode_RX33 = TX1_mode_RX33.T
    TX1_mode_RX33 = np.fft.fft(TX1_mode_RX33, n=128, axis=0)
    TX1_mode_RX33 = abs(TX1_mode_RX33)
    TX1_mode_RX33 = TX1_mode_RX33[1:125, 0:256]

    TX1_mode_RX44 = np.fft.fft(TX1_mode0_Rx4, n=512, axis=0)
    TX1_mode_RX44 = TX1_mode_RX44.T
    TX1_mode_RX44 = np.fft.fft(TX1_mode_RX44, n=128, axis=0)
    TX1_mode_RX44 = abs(TX1_mode_RX44)
    TX1_mode_RX44 = TX1_mode_RX44[1:125, 0:256]

# -----绘制二维线图
fig1 = plt.figure(num='二维线图', figsize=(12, 6))  # 创建一个名为"二维线图"图形,指定图形大小
plt.subplots_adjust(wspace=0.5, hspace=0.5) # 调整图形的布局,左右上下间距
mpl.rcParams["font.sans-serif"] = ["FangSong"]
mpl.rcParams["axes.unicode_minus"] = False

fig1_ax1 = fig1.add_subplot(221)    # 将fig1 图形分割成2行2列,子图的归属位置
fig1_ax2 = fig1.add_subplot(222)
fig1_ax3 = fig1.add_subplot(223)
fig1_ax4 = fig1.add_subplot(224)

fig1_ax1.plot(TX1_mode0_Rx1, ls="-", lw=0.2, c="c")   # 在fig1_ax1子图上绘制二维线图,设置线的风格、宽度、颜色,并设置标题
fig1_ax1.set_title("TX1_mode0_Rx1")
fig1_ax1.set_xlabel("x轴")
fig1_ax1.set_ylabel("y轴")
fig1_ax2.plot(TX1_mode0_Rx2, ls="-", lw=0.2, c="lime")
fig1_ax2.set_title("TX1_mode0_Rx2")
fig1_ax2.set_xlabel("x轴")
fig1_ax2.set_ylabel("y轴")
fig1_ax3.plot(TX1_mode0_Rx3, ls="-", lw=0.2, c="deepskyblue")
fig1_ax3.set_title("TX1_mode0_Rx3")
fig1_ax3.set_xlabel("x轴")
fig1_ax3.set_ylabel("y轴")
fig1_ax4.plot(TX1_mode0_Rx4, ls="-", lw=0.2, c="deeppink")
fig1_ax4.set_title("TX1_mode0_Rx4")
fig1_ax4.set_xlabel("x轴")
fig1_ax4.set_ylabel("y轴")

# -----绘制三维曲面图
fig2 = plt.figure(num='三维曲面', figsize=(12, 6))  # 创建一个名为"三维曲面"图形,指定图形大小
plt.subplots_adjust(wspace=0.5, hspace=0.5) # 调整图形的布局,左右上下间距
X = np.arange(1, int(TX1_mode_RX11.shape[1]) + 1, 1)    # 创建一个X散点数据数组,1起步,最大值为TX1_mode_RX11 数组的列长,步长为1
Y = np.arange(1, int(TX1_mode_RX11.shape[0]) + 1, 1)    # 创建一个Y散点数据数组,1起步,最大值为TX1_mode_RX11 数组的行长,步长为1
x, y = np.meshgrid(X, Y)    # 将X,Y散点数据处理成x,y网格数据

fig2_ax1 = fig2.add_subplot(221, projection='3d')   # 将fig2 图形分割成2行2列,子图的归属位置,设置三维度构建
fig2_ax2 = fig2.add_subplot(222, projection='3d')
fig2_ax3 = fig2.add_subplot(223, projection='3d')
fig2_ax4 = fig2.add_subplot(224, projection='3d')

fig2_ax1.plot_surface(x, y, TX1_mode_RX11, cmap='rainbow')  # 在fig2_ax1子图上绘制三维曲面图,设置线的颜色,并设置标题
fig2_ax1.set_title("TX1_mode_RX11")
fig2_ax1.set_xlabel('x轴')
fig2_ax1.set_ylabel('y轴')
fig2_ax1.set_zlabel('z轴')
fig2_ax2.plot_surface(x, y, TX1_mode_RX22, cmap='rainbow')
fig2_ax2.set_title("TX1_mode_RX22")
fig2_ax2.set_xlabel('x轴')
fig2_ax2.set_ylabel('y轴')
fig2_ax2.set_zlabel('z轴')
fig2_ax3.plot_surface(x, y, TX1_mode_RX33, cmap='rainbow')
fig2_ax3.set_title("TX1_mode_RX33")
fig2_ax3.set_xlabel('x轴')
fig2_ax3.set_ylabel('y轴')
fig2_ax3.set_zlabel('z轴')
fig2_ax4.plot_surface(x, y, TX1_mode_RX44, cmap='rainbow')
fig2_ax4.set_title("TX1_mode_RX44")
fig2_ax4.set_xlabel('x轴')
fig2_ax4.set_ylabel('y轴')
fig2_ax4.set_zlabel('z轴')

plt.show()

