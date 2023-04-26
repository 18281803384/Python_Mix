from PySide2.QtCore import QFile
from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader
from translate import Translator


class Translate_class:  # 创建一个类对象
    def __init__(self):  # 初始化
        # 从文件中加载UI定义
        ui_file = QFile('file/UI/2.Python_translate.ui')
        ui_file.open(QFile.ReadOnly)
        ui_file.close()
        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load(ui_file)
        self.ui.comboBox_1.addItems(['中文(简体)'])
        self.ui.comboBox_2.addItems(['英文'])
        self.ui.Button_translator.clicked.connect(self.translation_method)
        self.ui.Button_clear.clicked.connect(self.Button_clear)
        self.ui.Button_switch.clicked.connect(self.Button_switch)

    def translation_method(self):  # 中文转英文方法
        self.ui.Edit_2.clear()  # 清楚Edit_2文本框
        method = self.ui.comboBox_1.currentText()  # 获取comboBox_1组合选择框的选项
        if method == '中文(简体)':  # 如果为中文(简体)
            translator = Translator(from_lang="chinese", to_lang="english")  # 中文转英文
        else:
            translator = Translator(from_lang="english", to_lang="chinese")  # 英文转中文
        Edit_1 = self.ui.Edit_1.toPlainText()  # 获取Edit_1文本内容
        if Edit_1:
            try:
                translation = translator.translate(Edit_1)  # 对Edit_1进行翻译
            except:
                translation = '无法翻译 :' + Edit_1
            self.ui.Edit_2.appendPlainText(translation)  # 在Edit_2文本框中插入字符串

    def Button_clear(self):  # 清楚文本框方法
        self.ui.Edit_1.clear()
        self.ui.Edit_2.clear()

    def Button_switch(self):  # 切换语言翻译
        method = self.ui.comboBox_1.currentText()  # 获取comboBox_1组合选择框的选项
        if method == '中文(简体)':  # 如果为中文(简体)
            self.ui.comboBox_1.clear()  # 清空comboBox_1组合选择框的选项
            self.ui.comboBox_2.clear()  # 清空comboBox_2组合选择框的选项
            self.ui.comboBox_1.addItem('英文')  # comboBox_1添加选项
            self.ui.comboBox_2.addItem('中文(简体)')  # comboBox_2添加选项
        else:
            self.ui.comboBox_1.clear()
            self.ui.comboBox_2.clear()
            self.ui.comboBox_1.addItem('中文(简体)')
            self.ui.comboBox_2.addItem('英文')


app = QApplication([])  # 初始化图形界面程序的底层管理功能
translate = Translate_class()  # 实例化类
translate.ui.show()  # 显示图形界面的所有控件
app.exec_()  # 使QApplication的事件处理循环
