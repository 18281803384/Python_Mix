import numpy as np
import xlwings as xw

wb = xw.Book()
sht = wb.sheets['Sheet1']
sht.range('A1').value = np.eye(3)
print(sht.range('A1').options(np.array, expand='table').value)

input('Enter to quit')
wb.close()