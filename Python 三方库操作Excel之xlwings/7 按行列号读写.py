import xlwings as xw

# 创建新的工作薄
wb = xw.Book()
# 获取当前活动的工作薄
sht = wb.sheets.active

for i in range(1,6):
    for j in range(1,6):
        sht.range(i, j).value = '({}, {})'.format(i, j)

# 批量读取
print(sht.range((1, 1), (5, 5)).expand().value)
# 按行读
print(sht.range(1, 1).expand('right').value)
# 按列读
print(sht.range(1, 1).expand('down').value)

input('Enter to quit')
wb.close()