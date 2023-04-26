from PySide2.QtCore import QFile
from PySide2.QtWidgets import QApplication, QMessageBox, QFileDialog
from PySide2.QtUiTools import QUiLoader


class Translate:  # 创建一个类对象

    def __init__(self):  # 初始化
        # 从文件中加载UI定义
        ui_file = QFile('file/UI/1.upgrade_dbc.ui')
        ui_file.open(QFile.ReadOnly)
        ui_file.close()
        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load(ui_file)

        self.ui.pushButton_2.clicked.connect(self.file_upgrade_1)
        self.ui.pushButton_5.clicked.connect(self.file_upgrade_2)
        self.ui.pushButton_11.clicked.connect(self.file_upgrade_3)
        self.ui.pushButton_24.clicked.connect(self.open_dbc_file)

    def file_upgrade_1(self):
        file_name = QFileDialog.getOpenFileName(self.ui, '选择文件 ', 'd:/', '*.*')
        self.ui.lineEdit.setText(file_name[0])

    def file_upgrade_2(self):
        file_name = QFileDialog.getOpenFileName(self.ui, '选择文件 ', 'd:/', '*.*')
        self.ui.lineEdit_3.setText(file_name[0])

    def file_upgrade_3(self):
        file_name = QFileDialog.getOpenFileName(self.ui, '选择文件 ', 'd:/', '*.*')
        self.ui.lineEdit_10.setText(file_name[0])

    def open_dbc_file(self):
        file_name = QFileDialog.getOpenFileName(self.ui, '选择文件 ', 'd:/', '*.dbc')


app = QApplication([])  # 初始化图形界面程序的底层管理功能
translate = Translate()  # 实例化计算器类
translate.ui.show()  # 显示图形界面的所有控件
app.exec_()  # 使QApplication的事件处理循环