import xlwings as xw

# 设置是否可视化
visualization = False
# 界面设置
app = xw.App(visible=visualization, add_book=False)
# 关闭提示信息
app.display_alerts = visualization
# 关闭显示更新
app.screen_updating = visualization


# 创建新的工作薄
wb = app.books.add()
# 实例化工作表
sht = wb.sheets['Sheet1']
# 写入
sht.range('A1').value = 'Hello World!'
# 读取
print(sht.range('A1').value)
# 关闭
wb.close()

