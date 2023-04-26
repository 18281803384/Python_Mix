import xlwings as xw
from xlwings.utils import rgb_to_int

wb = xw.Book()
sht = wb.sheets['Sheet1']

# 全局字体
sht.range('A1', 'XFD1048576').api.Font.Name = '微软雅黑'

sht.range('A1').value = 'ABCDE'
# 字号
sht.range('A1').api.Font.Size = 12
# 加粗
sht.range('A1').api.Font.Bold = True
# 下标从1开始
start_index = 3
# 修改长度
length_string = 1
# 设为红色
sht.range('A1').api.GetCharacters(start_index, length_string).Font.Color = rgb_to_int((225, 0, 0))

sht.range('B1').value = 'ABCDE'
# 斜体
sht.range('B1').api.Font.Italic = True
# 删除线
sht.range('B1').api.Font.Strikethrough = True

sht.range('C1').value = 'ABCDE'
# 下划线 4普通 5双下划线 -4119粗双下划线
sht.range('C1').api.Font.Underline = True

sht.range('A2').value = 'a2'
# 上标
sht.range('A2').api.GetCharacters(2, 1).Font.Superscript = True

sht.range('B2').value = 'H20'
# 下标
sht.range('B2').api.GetCharacters(2, 1).Font.Subscript = True

# 自动调整
sht.autofit()
input('Enter to quit')
wb.close()