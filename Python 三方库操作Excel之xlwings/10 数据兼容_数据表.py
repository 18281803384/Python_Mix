import pandas as pd
import xlwings as xw

wb = xw.Book()
sht = wb.sheets['Sheet1']
df = pd.DataFrame([[1,2], [3,4]], columns=['a', 'b'])
sht.range('A1').value = df
print(sht.range('A1').options(pd.DataFrame, expand='table').value)

input('Enter to quit')
wb.close()