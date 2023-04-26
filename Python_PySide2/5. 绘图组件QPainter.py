from PySide2.QtCore import QFile
from PySide2.QtGui import QPainter, QPixmap
from PySide2.QtWidgets import QApplication, QMessageBox, QFileDialog, QMainWindow
from PySide2.QtUiTools import QUiLoader


class Translate(QMainWindow):  # 创建一个类对象

    def __init__(self):  # 初始化
        super(Translate, self).__init__()
        # 从文件中加载UI定义
        ui_file = QFile('file/UI/5.QPainter.ui')
        ui_file.open(QFile.ReadOnly)
        ui_file.close()
        self.ui = QUiLoader().load(ui_file)

        dialog = QFile('file/UI/6.show_img.ui')
        dialog.open(QFile.ReadOnly)
        dialog.close()
        self.dialog = QUiLoader().load(dialog)

        self.ui.pushButton.clicked.connect(self.open_img_file)
        self.ui.pushButton_2.clicked.connect(self.open_img)
        self.file_name = ''

    def open_img_file(self):
        file_name = QFileDialog.getOpenFileName(self.ui, '选择图片 ', 'D:\ZengCheng\Python_Pycharm\Python网络爬虫开发实战\第6章 Ajax数据爬取\img', '*.JPEG')
        self.file_name = file_name[0]
        self.ui.lineEdit.setText(self.file_name)

    def open_img(self):
        self.setCentralWidget(self.dialog)
        self.resize(600, 600)
        self.setWindowTitle('画图')
        self.show()

    def paintEvent(self, event):
        painter = QPainter()
        self.pixmap()

    def pixmap(self):
        painter = QPainter(self)
        pix = QPixmap(self.file_name)
        painter.drawPixmap(100, 100, 400, 400, pix)


app = QApplication([])  # 初始化图形界面程序的底层管理功能
translate = Translate()  # 实例化计算器类
translate.ui.show()  # 显示图形界面的所有控件
app.exec_()  # 使QApplication的事件处理循环