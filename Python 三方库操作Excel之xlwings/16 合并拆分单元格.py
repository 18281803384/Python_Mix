import xlwings as xw

wb = xw.Book()
sht = wb.sheets.active
# 合并单元格
sht.range('A1:D5').merge()
input('Enter to unmerge')
# 拆分单元格
sht.range('A1:D5').unmerge()
input('Enter to quit')
wb.close()

