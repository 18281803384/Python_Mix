import numpy as np
import xlwings as xw

wb = xw.Book()
sht = wb.sheets['Sheet1']
d = {'a': 1,'b': 2}
sht.range('A1').value = d
print(sht.range('A1').options(np.array, expand='table').value)

input('Enter to quit')
wb.close()