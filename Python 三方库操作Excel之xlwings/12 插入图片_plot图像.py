import xlwings as xw
import matplotlib.pyplot as plt

wb = xw.Book()
sht = wb.sheets['Sheet1']
fig = plt.figure()
plt.plot([1, 2, 3, 4, 5])
sht.pictures.add(fig, name='MyPlot', update=True)
wb.save('file/test_12.xlsx')
wb.close()