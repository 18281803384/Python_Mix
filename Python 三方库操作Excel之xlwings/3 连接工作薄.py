import xlwings as xw

# 隐藏界面
app = xw.App(visible=True, add_book=False)
# 关闭提示信息
app.display_alerts = False
# 关闭显示更新
app.screen_updating = False

# 创建新的工作簿
wb = app.books.add()
# # 连接当前路径下的工作薄
# wb = app.books.open('file/test_1.xlsx')
# # 获取当前活动的工作薄
# wb = app.books.active
# # 创建新的工作薄
# wb = xw.Book()
# # 连接当前路径下的工作薄
# wb = xw.Book('file/test_1.xlsx')
# # Windows下绝对路径连接
# wb = xw.Book(r'C:/test_1.xlsx')
input('Enter to quit')
wb.close()