import xlwings as xw

# 创建新的工作薄
wb = xw.Book()
# 连接工作表
sht = wb.sheets['Sheet1']
# 写入数据
sht.range('A1').value = 'Foo 1'
# 读取数据
print(sht.range('A1').value)

input('Enter to quit')
wb.close()