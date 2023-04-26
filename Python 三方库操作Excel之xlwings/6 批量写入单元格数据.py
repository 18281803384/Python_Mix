import xlwings as xw

# 创建新的工作薄
wb = xw.Book()
# 连接工作表
sht = wb.sheets['Sheet1']
# 批量写入数据
sht.range('A1').value = [['Foo 1', 'Foo 2', 'Foo 3'], [10.0, 20.0, 30.0]]
# 批量读取数据
print(sht.range('A1').expand().value)
# 保存数据
wb.save('file/test_6.xlsx')
# 关闭
wb.close()