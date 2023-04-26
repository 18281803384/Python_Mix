import xlwings as xw
from xlwings.utils import rgb_to_int

if __name__ == '__main__':
    wb = xw.Book()
    sht = wb.sheets['Sheet1']

    '''5左上角对角线'''
    sht.range('A2', 'B3').api.Borders(5).LineStyle = 1  # 实线
    sht.range('A2', 'B3').api.Borders(5).Weight = 1  # 细
    sht.range('A2', 'B3').api.Borders(5).Color = 0x0  # 黑色

    '''6左下角对角线'''
    sht.range('C2', 'D3').api.Borders(6).LineStyle = -4119  # 双线
    sht.range('C2', 'D3').api.Borders(6).Weight = 2  # 细长
    sht.range('C2', 'D3').api.Borders(6).Color = 0xFF  # 红色

    '''7 8 9 10 左上下右'''
    for i in [7, 8, 9, 10]:
        sht.range('E2', 'F3').api.Borders(i).LineStyle = 4  # 点划相间线
        sht.range('E2', 'F3').api.Borders(i).Weight = 4  # 粗
        sht.range('E2', 'F3').api.Borders(i).Color = 0xFF00  # 绿色

    '''11内部垂直线'''
    sht.range('G2', 'H3').api.Borders(11).LineStyle = 5  # 划线后跟两个点
    sht.range('G2', 'H3').api.Borders(11).Weight = -4138  # 中
    sht.range('G2', 'H3').api.Borders(11).Color = rgb_to_int((0, 128, 128))  # 紫色

    '''12内部水平线'''
    sht.range('I2', 'J3').api.Borders(12).LineStyle = -4115  # 虚线
    sht.range('I2', 'J3').api.Borders(12).Weight = 4  # 粗
    sht.range('I2', 'J3').api.Borders(12).Color = rgb_to_int((0, 0, 255))  # 蓝色

    input('任意输入保存')
    wb.save('file/test_15.xlsx')
    wb.close()
