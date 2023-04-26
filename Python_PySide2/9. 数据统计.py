import os
import time
import json
import jsonpath
from PySide2 import QtCore, QtWidgets
from PySide2.QtCore import QFile, QDate
from PySide2.QtGui import Qt, QIcon
from PySide2.QtWidgets import QApplication, QMessageBox, QTableWidgetItem
from PySide2.QtUiTools import QUiLoader


class Data_total:  # 创建一个接口类对象
    def __init__(self):
        # 从文件中加载UI定义
        ui_file = QFile('file/UI/9.Data_Statistics.ui')
        ui_file.open(QFile.ReadOnly)
        ui_file.close()
        self.ui = QUiLoader().load(ui_file)
        # 监听按钮事件,关联方法
        self.ui.calendar.clicked.connect(self.calendar_time)  # 日历控件
        self.ui.onekey_add.clicked.connect(self.noekey_add)  # ‘一键添加人员’按钮
        self.ui.Buuton_clear.clicked.connect(self.tabel_clear)  # ‘清空’按钮
        self.ui.Buuton_save.clicked.connect(self.save_table_json)  # ‘保存当日数据’按钮
        # 表格单元格改动事件,关联方法
        self.ui.tableWidget.cellChanged.connect(self.tableWidget_item_changed)
        # 初始化时调用的方法
        self.initial_method()  # 调用方法,运行该函数
        self.judge_file()  # 调用方法,验证本地json文件路径
        # 自定义属性
        self.time = ''  # 用于存储点击日历后保存的时间
        self.data_dict = {}  # 用于存储表格中单元格内容
        self.names = ['蒙瑞霞', '吴晓龙', '陈一鸣', '武彤', '孙慧倩', '何鹿川', '杨鹏', '周鲁鑫', '刘道红', '刘媛']  # 自定义名单列表数据

    def initial_method(self):  # 初始化方法
        self.ui.setWindowTitle('数据统计管理系统')  # 设置窗口标题
        self.ui.move(600, 20)  # 设置窗口的位置
        # 设置表格内标题字体加粗
        font = self.ui.tableWidget.horizontalHeader().font()
        font.setBold(True)
        self.ui.tableWidget.horizontalHeader().setFont(font)
        self.ui.calendar.setGridVisible(True)  # 设置日历显示表格样式
        self.calendar_max_time()  # 调用方法,设置日历可点击的最大日期范围
        self.ui.tableWidget.horizontalHeader().resizeSection(3, 300)  # 设置指定列的宽度

    @staticmethod
    def get_day_time():  # 获取当日日期 方法
        # 获取当前日期时间
        times = time.time()
        local_time = time.localtime(times)
        y = int(time.strftime("%Y", local_time))  # 年
        m = int(time.strftime("%m", local_time))  # 月
        d = int(time.strftime("%d", local_time))  # 日
        ymd = time.strftime("%Y-%m-%d", time.localtime())  # 转化为指定格式,例: 2020-07-01
        return ymd, y, m ,d

    def calendar_max_time(self):  # 控制日历可选择日期范围 方法
        ymd, y, m, d = self.get_day_time()  # 调用方法,获取当前日期的年月日
        self.ui.calendar.setMaximumDate(QDate(y, m, d))  # 设置日历最大可选择的日期为当日,大于当日的日期不可选择

    def tabel_clear(self):  # 清空表格单元格内容 方法  扩展功能
        self.ui.tableWidget.setRowCount(0)  # 删除表格所有的内容
        self.noekey_add()  # 调用方法,一键添加人员名单单元格数据
        self.show_total_data()  # 调用方法,对表格单元格的数据进行统计

    def MessageBox(self, message):  # 自定义弹窗内容 方法
        QMessageBox.question(self.ui, '提示', message, QMessageBox.Yes)  # 弹出内容提示

    @staticmethod
    def time_data_integration(time_data):  # 对本地文件获取的json数据进行整合 方法
        time_data_key_list = list(time_data.keys())  # 获取所有的key值并转为列表储存
        time_data_value1 = jsonpath.jsonpath(time_data, '$..value1')  # 获取json中所有匹配的值,返回为列表
        time_data_value2 = jsonpath.jsonpath(time_data, '$..value2')  # 获取json中所有匹配的值,返回为列表
        time_data_remarks = jsonpath.jsonpath(time_data, '$..remarks')  # 获取json中所有匹配的值,返回为列表
        time_data_zip_list = []  # 创建一个空列表
        time_data_zip = list(zip(time_data_key_list, time_data_value1, time_data_value2, time_data_remarks))  # zip迭代器对列表对应元素一个个打包成元组,再把外层元组转为列表
        for data in time_data_zip:  # 循环列表中的元组数据
            time_data_zip_list.append(list(data))  # 将元组数据转为列表,并追加到上述空列表中
        return time_data_zip_list

    def show_time_data(self, time_data_zip_list):  # 对本地json文件获取整合后的数据进行表格单元格赋值显示 方法
        for i in range(len(time_data_zip_list)):  # 循环数据的长度,从0开始,步长为1
            row, column = self.get_row_column()  # 调用方法,得到表格单元格的行和列数
            if row in range(len(time_data_zip_list)):  # 如果行数在数据长度内
                self.ui.tableWidget.insertRow(row)  # 为表格行数内添加单元格
            for j in range(len(time_data_zip_list[i])):  # 循环数据内列表数据的长度,从0开始,步长为1
                item = QTableWidgetItem(str(time_data_zip_list[i][j]))  # 把列表数据转为item
                if not self.judge_day_time(self.time):  # 如果点击的日历日期不是当日
                    item.setFlags(QtCore.Qt.ItemIsEnabled)  # 写入单元格的数据为只读状态,不可编辑
                self.ui.tableWidget.setItem(i, j, item)  # 对相应(行, 列)单元添加item数据
                item.setTextAlignment(Qt.AlignHCenter)  # 使item数据水平居中

    @staticmethod
    def judge_file():  # 判断本地json文件保存的位置是否有效 方法
        if not os.path.exists('file/json'):  # 如果json文件夹不存在
            os.makedirs('file/json')  # 创建json文件夹
        json_path = 'file/json/Data_total.json'
        if not os.path.exists(json_path):  # 如果json文件不存在
            with open(json_path, 'a') as f:  # 以追加方法打开文件,文件不存在则创建文件
                f.write("{}")  # 写入空数据

    def get_table_day_json(self):  # 获取本地json文件中日历日期的数据 方法
        with open('file/json/Data_total.json', 'r', encoding='UTF-8') as f:  # 以只读方式打开文件
            try:  # 如果遇到异常则抛出
                data = json.load(f)  # 直接读取json格式文件
                time_data = data[self.time]  # 获取日历日期的数据
                self.data_dict[self.time] = time_data  # 修改data_dict中日历日期的数据为本地json文件获取的数据
                time_data = self.time_data_integration(time_data)  # 调用方法,对获取的日历日期的数据进行整合
                return time_data
            except Exception:  # 异常情况,本地json文件没有日历日期的数据
                self.ui.tableWidget.setRowCount(0)  # 删除表格所有的内容
                self.data_dict = {}  # 修改data_dict为空字典
                self.ui.label_1.setText('当日完成: ')  # 对相应控件写入当日完成文本
                self.ui.label_2.setText('当日提交: ')  # 对相应控件写入当日提交文本
                if not self.judge_day_time(self.time):  # 如果点击的日历日期不是当日
                    self.MessageBox(self.time + ' 没有数据.... ^_^')  # 弹出内容提示
                return None

    @staticmethod  # 静态方法
    def get_table_all_json():  # 获取本地json文件的所有数据 方法
        with open('file/json/Data_total.json', 'r', encoding='UTF-8') as f:  # 以只读方式打开文件
            data = json.load(f)  # 直接读取json格式文件
            return data

    def save_table_json(self):  # 保存表格单元格数据到本地json文件 方法
        data = self.get_table_all_json()  # 调用方法,以获取本地json文件的所有数据
        data[self.time] = self.data_dict[self.time]  # 写入当前日历时间的表格数据
        data = json.dumps(data, ensure_ascii=False)  # 用于将 Python 字典对象编码成 JSON 字符串,数据存在中文时输出真正的中文
        with open('file/json/Data_total.json', 'w', encoding='utf-8') as f:  # 以可写方式打开文件
            f.write(data)  # 直接写入json格式文件
        self.MessageBox(self.time + ' 数据保存成功.... ^_^')  # 调用提示弹窗

    def judge_day_time(self, ca_time):  # 判断点击日历的时间是否为当日 方法
        ymd, y, m, d = self.get_day_time()  # 调用方法,获取当前日期的年月日
        if ymd == ca_time:  # 如果当前年月日 = 日历点击年月日,表示点击日历时间是为当日
            return True
        else:  # 点击日历时间不为当日
            return False

    def butoon_setEnabled(self, ca_time):  # 决定按钮显示隐藏 方法
        day_time = self.judge_day_time(ca_time)  # 调用方法,判断点击的日历日期是否为当日,返回True则是当日,返回False则不为当日
        if day_time:
            self.ui.onekey_add.setEnabled(True)  # 按钮启用
            self.ui.Buuton_clear.setEnabled(True)  # 按钮启用
            self.ui.Buuton_save.setEnabled(True)  # 按钮启用
        else:
            self.ui.onekey_add.setEnabled(False)  # 按钮禁用
            self.ui.Buuton_clear.setEnabled(False)  # 按钮禁用
            self.ui.Buuton_save.setEnabled(False)  # 按钮禁用

    def calendar_time(self):  # 日历控件点击后的事件方法
        ca_time = self.ui.calendar.selectedDate().toString('yyyy-MM-dd')  # 获取点击日历控件后的时间,并转为指定格式时间显示,例: 2020-07-01
        self.ui.Box_Data.setTitle('数据统计 {}'.format(ca_time))  # 对相应控件写入日历日期文本
        self.butoon_setEnabled(ca_time)  # 调用方法,如果日历日期不是当日就对相关按钮禁用,反之则启用
        try:  # 如果遇到异常则抛出
            self.data_dict[ca_time] = self.data_dict.pop(self.time)  # 提取出字典的key值,赋予新的key值
        except KeyError:
            pass
        self.time = ca_time  # 赋值
        file_data = self.get_table_day_json()  # 调用方法,获取本地json文件日历日期的数据,,则返回该数据,如果没有获取到则为None
        if file_data:  # 如果获取到了日历日期在本地json文件的数据
            self.show_time_data(file_data)  # 对日历日期的数据进行表格赋值显示
        else:  # 为None
            self.data_dict[self.time] = {}  # 修改data_dict中日历日期的数据为空字典

    def noekey_add(self):  # 一键添加人员名单单元格数据 方法
        row, column = self.get_row_column()  # 调用方法,得到表格单元格的行和列数
        if self.time:  # 判断是否选择了日历日期,选择了则
            if row in range(len(self.names)):  # 如果行数在名单数据长度内
                for i in range(len(self.names)):
                    self.ui.tableWidget.insertRow(i)  # 为表格行数内添加单元格
                    item = QTableWidgetItem(self.names[i])  # 把列表数据转为item
                    self.ui.tableWidget.setItem(i, 0, item)  # 对相应(行, 0列)单元添加item数据
                    item.setTextAlignment(Qt.AlignCenter)  # 使item数据水平居中
                    item.setFlags(QtCore.Qt.ItemIsEnabled)  # 写入单元格的数据为只读状态,不可编辑
                    self.data_dict[self.time][self.names[i]] = {
                        "value1": 0,
                        "value2": 0,
                        "remarks": ""
                    }  # 对表格中非0列单元格写入默认空数据
            else:
                self.MessageBox('名单已经生成.... ^_^')  # 调用提示弹窗
        else:  # 没有选择则
            self.MessageBox('请选择日历的日期.... ^_^')  # 调用提示弹窗

    def show_total_data(self):  # 对表格单元格的数据进行统计 方法
        value1_total = jsonpath.jsonpath(self.data_dict, '$..value1')  # 获取json中所有匹配的值,返回为列表
        value2_total = jsonpath.jsonpath(self.data_dict, '$..value2')  # 获取json中所有匹配的值,返回为列表
        total1 = self.sumOfList(value1_total, len(value1_total))  # 调用递归函数求出列表数据之和
        total2 = self.sumOfList(value2_total, len(value2_total))  # 调用递归函数求出列表数据之和
        self.ui.label_1.setText('当日完成: ' + str(total1))  # 对相应控件写入当日完成统计文本
        self.ui.label_2.setText('当日提交: ' + str(total2))  # 对相应控件写入当日提交统计文本

    def sumOfList(self, value_list, size):  # 递归获取列表之和 方法
        if size == 0:
            return 0
        else:
            total = value_list[size - 1] + self.sumOfList(value_list, size - 1)
            return total

    def get_row_column(self):  # 获取表格的行数和列数 方法
        row = self.ui.tableWidget.rowCount()  # 获取表格控件的行数
        column = self.ui.tableWidget.columnCount()  # 获取表格控件的列数
        return row, column

    def tableWidget_item_changed(self, row, column):  # 表格事件监听 方法
        if column > 0:  # 判断所改变的列数大于0列的单元格
            # 获取更改内容
            Name = self.ui.tableWidget.item(row, 0).text()  # 获取表格(所有行, 0列)单元格的数据,首列为名单人员
            Value = self.ui.tableWidget.item(row, column).text()  # 获取表格(所有行, 大于0列)单元格的数据
            if column == 1:  # 如果单元格列数等于1,当日完成
                if Value:  # 获取的内容不为空
                    try:  # 如果遇到异常则抛出
                        self.data_dict[self.time][Name]['value1'] = int(Value)  # 写入数据到data_dict中
                    except ValueError:  # 异常情况,获取到的文本不是整数数字
                        self.MessageBox('请输入整数数字.... ^_^') # 调用提示弹窗
                        self.ui.tableWidget.item(row, column).setText('')  # 对该单元格(行, 列)的数据置为空
            elif column == 2:  # 如果列数等于2,当日提交
                if Value:  # 获取的内容不为空
                    try: # 如果遇到异常则抛出
                        self.data_dict[self.time][Name]['value2'] = int(Value)  # 写入数据到dict中
                    except ValueError:   # 异常情况,获取到的文本不是整数数字
                        self.MessageBox('请输入整数数字.... ^_^') # 调用提示弹窗
                        self.ui.tableWidget.item(row, column).setText('')  # 对该单元格(行, 列)的数据置为空
            elif column == 3:  # 如果列数等于3,备注
                if Value:  # 获取的内容不为空
                    self.data_dict[self.time][Name]['remarks'] = Value  # 写入数据到dict中
            self.show_total_data()  # 调用方法,对表格单元格的数据进行统计


app = QApplication([])  # 初始化图形界面程序的底层管理功能
app.setWindowIcon(QIcon('file/logo/python_logo.png'))  # 加载 icon
reptile = Data_total()  # 实例化类
reptile.ui.show()  # 显示图形界面的所有控件
app.exec_()  # 使QApplication的事件处理循环
