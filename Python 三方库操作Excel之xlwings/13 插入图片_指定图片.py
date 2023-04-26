import os
import xlwings as xw

wb = xw.Book()
sht = wb.sheets['Sheet1']
rng = sht.range('B1')
# 自定义图片
fileName = os.path.join(os.getcwd(), 'file/test_13.jpg')
# 指定图片大小
width, height = 60, 60
# 居中
left = rng.left + (rng.width - width) / 2
top = rng.top + (rng.height - height) / 2
sht.pictures.add(fileName, left=left, top=top, width=width, height=height)