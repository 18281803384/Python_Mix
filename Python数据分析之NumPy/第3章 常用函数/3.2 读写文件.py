import csv
import random

import numpy as np

# 创建一个单位矩阵
i2 = np.eye(2)
print(i2)

# 使用savetxt函数将数据存储到文件中
np.savetxt("file/eye.txt", i2)


for i in range(100):
    random_number = random.randint(100, 900)
    persons = [('AAPL', '28-01-2011', '', random_number, random_number, random_number, random_number, random_number)]
    with open('file/data.csv', 'a', encoding='utf-8', newline='') as f:
        write = csv.writer(f)  # 创建writer对象
        for data in persons:
            write.writerow(data)