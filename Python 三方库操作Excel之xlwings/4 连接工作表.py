import xlwings as xw

wb = xw.Book()
# 连接工作表
sht = wb.sheets.active
# 连接工作表
# sht = wb.sheets[0]
# 连接工作表
# sht = wb.sheets['sheet1']
# 连接工作表
# sht = wb.sheets.add()
# 连接工作表
sht = wb.sheets.add('新表', after=sht)
input('Enter to quit')
wb.close()