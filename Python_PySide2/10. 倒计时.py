import time

from PySide2.QtCore import QFile
from PySide2.QtWidgets import QApplication, QMessageBox, QLCDNumber
from PySide2.QtUiTools import QUiLoader


class Count_Down:  # 创建一个类对象

    def __init__(self):  # 初始化
        # 从文件中加载UI定义
        ui_file = QFile('file/UI/10.count_down.ui')
        ui_file.open(QFile.ReadOnly)
        ui_file.close()
        self.ui = QUiLoader().load(ui_file)

        self.num = 10
        self.ui.pushButton.clicked.connect(self.lcd_change)

    def lcd_change(self):
        self.ui.lcdNumber.display(self.num)  # 设置lcdNumber的值
        self.num += 1



if __name__ == '__main__':
    app = QApplication([])  # 初始化图形界面程序的底层管理功能
    count_down = Count_Down()  # 实例化类
    count_down.ui.show()  # 显示图形界面的所有控件
    app.exec_()  # 使QApplication的事件处理循环