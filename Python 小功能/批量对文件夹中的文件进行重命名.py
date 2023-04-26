# 作者: ZengCheng
# 时间: 2022/9/26
import os

path = "D:/test"  # 文件夹路径
file_list = os.listdir(path)  # 获取path下所有的文件或文件夹的名字的列表。
file_name = '文件' # 替换后的文件名
old_file_list = []
new_file_list = []
for i in range(len(file_list)):  # 循环遍历file_list的数量
    old_name = os.path.join(path, file_list[i])  # 获取旧的文件路径名
    old_file_list.append(file_list[i])
    new_file_name = file_name + '_' + str(i + 1) + '.txt'  # 创建新的文件夹名
    new_file_list.append(new_file_name)
    new_name = os.path.join(path, new_file_name)  # 创建新的文件路径名
    os.rename(old_name, new_name)  # 进行文件更名

print('旧：', old_file_list)
print('新：', new_file_list)
print('文件更名成功！')
