from PySide2.QtCore import QFile
from PySide2.QtGui import QPainter, QPixmap
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget


class Translate(QMainWindow):  # 创建一个类对象

    def __init__(self):  # 初始化
        super(Translate, self).__init__()
        # 从文件中加载UI定义
        ui_file = QFile('file/UI/5.Picture_preview.ui')
        ui_file.open(QFile.ReadOnly)
        ui_file.close()
        self.ui = QUiLoader().load(ui_file)

        # 监听Button_open_img按钮事件 关联方法
        self.ui.Button_open_img.clicked.connect(self.Button_open_img)

        # 变量
        self.file_name = ''

    def Button_open_img(self):
        file_name = QFileDialog.getOpenFileName(self.ui, '选择图片 ', 'D:\ZengCheng\Python_Pycharm\Python网络爬虫开发实战\第6章 Ajax数据爬取\img', "Image Files (*.png *.jpg *.bmp *.JPEG)")
        self.file_name = file_name[0]
        self.ui.Edit_route.setText(self.file_name)
        self.ui.label.setPixmap(QPixmap(self.file_name))


app = QApplication([])  # 初始化图形界面程序的底层管理功能
translate = Translate()  # 实例化计算器类
translate.ui.show()  # 显示图形界面的所有控件
app.exec_()  # 使QApplication的事件处理循环