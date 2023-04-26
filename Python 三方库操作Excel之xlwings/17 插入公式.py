import xlwings as xw

wb = xw.Book()
sht = wb.sheets.active
sht.range('A1').value = [['语文', '数学', '总分'], [100, 100, None]]
sht.range('C2').formula = '=SUM(A2:B2)'
input('Enter to quit')
wb.close()