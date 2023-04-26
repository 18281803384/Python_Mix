"""
目标： 深入学习json解析
"""
import random
import jsonpath
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox
import json


class Idiom_Solitaire(QMainWindow):
    def __init__(self):  # 初始化函数
        super(Idiom_Solitaire, self).__init__()
        # 从文件中加载UI定义
        ui_file = QFile('file/UI/8.idiom_Solitaire.ui')
        ui_file.open(QFile.ReadOnly)
        ui_file.close()
        self.ui = QUiLoader().load(ui_file)
        # 设置窗口标题
        self.ui.setWindowTitle('成语接龙')
        # 监听按钮事件,关联方法
        self.ui.Button_solitaire.clicked.connect(self.get_idiom)
        # 自定义属性
        self.json_data = self.get_json_data()  # 存储文件中获取的json数据
        self.choice_idiom = ''
        # 初始化时调用该方法
        self.idiom_random()

    @staticmethod
    def get_json_data():  # 从文件中获取json数据
        with open('file/json/idiom.json', 'r', encoding='UTF-8') as f:
            data = json.load(f)
            return data

    def idiom_random(self):  # 随机查询出指定数量的成语
        for i in range(20):
            idiom_json = self.json_data[random.randint(0, len(self.json_data))]
            word = jsonpath.jsonpath(idiom_json, '$..word')
            self.ui.idiom_list_1.addItem(word[0])

    def idiom_details(self, idiom):  # 查询指定成语的详情
        self.ui.Edit_log.clear()
        for i in self.json_data:
            ci = jsonpath.jsonpath(i, '$..word')
            if ci[0] == idiom:
                derivation = jsonpath.jsonpath(i, '$..derivation')
                example = jsonpath.jsonpath(i, '$..example')
                explanation = jsonpath.jsonpath(i, '$..explanation')
                pinyin = jsonpath.jsonpath(i, '$..pinyin')
                word = jsonpath.jsonpath(i, '$..word')
                idiom_details_log = ('''拼音: {}\n成语: {}\n起源: {}\n实例: {}\n解释: {}'''.format(pinyin[0], word[0], derivation[0], example[0], explanation[0]))
                # print(idiom_details_log)
                self.ui.Edit_log.insertPlainText(idiom_details_log)  # 控件显示出文本

    def idiom_Solitaire(self, idiom):  # 对指定成语接龙查询
        self.ui.idiom_list_1.clear()
        for i in self.json_data:
            ci = jsonpath.jsonpath(i, '$..word')
            if ci[0][0] == idiom[-1]:
                self.ui.idiom_list_1.addItems(ci)
        try:
            idiom = self.ui.idiom_list_1.item(0).text()
        except Exception:
            self.ui.idiom_list_1.addItem('成语接龙已到底....^_^')
            self.ui.Button_solitaire.setEnabled(False)

    def get_idiom(self):  # 获取指定成语
        try:
            idiom = self.ui.idiom_list_1.currentItem().text()
        except Exception:
            QMessageBox.question(self.ui, '提示', '请选择下一个成语.... ^_^', QMessageBox.Yes)
        else:
            if idiom == self.choice_idiom:
                QMessageBox.question(self.ui, '提示', '请选择下一个成语.... ^_^', QMessageBox.Yes)
            else:
                self.ui.idiom_list_2.addItem(idiom)
                self.choice_idiom = idiom
                self.idiom_Solitaire(self.choice_idiom)
                self.idiom_details(self.choice_idiom)


if __name__ == '__main__':
    app = QApplication([])  # 初始化图形界面程序的底层管理功能
    idiom_solitaire = Idiom_Solitaire()  # 实例化类
    idiom_solitaire.ui.show()  # 显示图形界面的所有控件
    app.exec_()  # 使QApplication的事件处理循环

