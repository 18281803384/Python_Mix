from PySide2.QtCore import QFile
from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader


class Reptile:  # 创建一个接口类对象

    def __init__(self):  # 初始化
        # 从文件中加载UI定义
        ui_file = QFile('file/UI/4.Reptile.ui')
        ui_file.open(QFile.ReadOnly)
        ui_file.close()
        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load(ui_file)


app = QApplication([])  # 初始化图形界面程序的底层管理功能
reptile = Reptile()  # 实例化接口类
reptile.ui.show()  # 显示图形界面的所有控件
app.exec_()  # 使QApplication的事件处理循环