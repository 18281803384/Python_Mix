import csv
import pandas as pd


print('-' * 30 + "写入csv")

with open('file/data.csv', 'w') as f:
    writer = csv.writer(f, delimiter=' ')
    writer.writerow(['id', 'name', 'age'])
    writer.writerow(['10001', 'Mike', 20])
    writer.writerow(['10002', 'Bob', 22])
    writer.writerow(['10003', 'Jordan', 21])


with open('file/data.csv', 'w', encoding='utf-8', newline='') as f:
    filenames = ['id', 'name', 'age']
    writer = csv.DictWriter(f, fieldnames=filenames)
    writer.writeheader()
    writer.writerow({'id': '1001','name': 'Mike','age': 20})
    writer.writerow({'id': '1002', 'name': 'Bob', 'age': 22})
    writer.writerow({'id': '1003', 'name': 'Jordan', 'age': 21})
    writer.writerow({'id': '1004', 'name': '王伟', 'age': 22})


print('CSV文件存储完毕')

print('-' * 30 + "读取csv")

with open('file/data.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

print('-' * 30 + 'pandas 读取csv文件数据')
df = pd.read_csv('file/data.csv')
print(df)