import xlwings as xw
from itertools import product

# 隐藏Excel
app = xw.App(visible=False)
# 打开工作薄
wb = app.books.open('file/test_11.xlsx')
# 实例化工作表
sht = wb.sheets['Sheet1']
for cell in list(map(''.join, product('ABCDEFGH', '1'))):
    # 填充颜色
    print(cell, sht.range(cell).color)

wb.close()