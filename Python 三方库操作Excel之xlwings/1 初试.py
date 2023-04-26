import xlwings as xw

# 创建新的工作薄
wb = xw.Book()
# 实例化工作表
sht = wb.sheets['Sheet1']
# 写入
sht.range("A1").value = 'Hello World!'
sht.range("A2").value = 'Hello World!'
# 读取
print(sht.range('A1').value)
# 保存
wb.save('file/test_1.xlsx')
# 关闭
wb.close()