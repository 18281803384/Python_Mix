import json
import os
import re
import sys
from bs4 import BeautifulSoup
import requests
import urllib3
from PySide2.QtCore import QFile
from PySide2.QtGui import QPixmap, QIcon
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QMainWindow, QFileDialog, QApplication, QMessageBox, QPushButton

urllib3.disable_warnings()


class Glory_Window(QMainWindow):
    def __init__(self):  # 初始化函数
        super(Glory_Window, self).__init__()
        # 从文件中加载UI定义
        ui_file = QFile('file/UI/7.Glory_Window.ui')
        ui_file.open(QFile.ReadOnly)
        ui_file.close()
        self.ui = QUiLoader().load(ui_file)
        # 设置窗口标题
        self.ui.setWindowTitle('王者荣耀壁纸下载器')
        # 监听按钮事件,关联方法
        self.ui.Button_query.clicked.connect(self.Hero_img)
        self.ui.Button_file_path.clicked.connect(self.file_path)
        self.ui.Button_download.clicked.connect(self.get_img_url)
        # 组织请求头参数
        self.headers = {
            'Accept': 'application/json, text/plain, */*',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'
        }
        # 自定义属性
        self.Hero_dict = {}  # 字典属性储存英雄资料,包含了{'英雄姓名':英雄ID}
        self.hero_title_list = []  # 列表属性储存英雄皮肤标题['星辰之子', '归虚梦演', '云鹰飞将', '李逍遥']
        # 初始化时调用该方法
        self.Hero_list()

    def MessageBox(self, text):  # 自定义消息弹窗
        mb = QMessageBox(self.ui)
        mb.setWindowTitle('温馨提示')  # 设置标题
        mb.setText(text)  # 设置显示内容
        mb.addButton(QPushButton('关闭', mb), QMessageBox.RejectRole)  # 添加关闭按钮
        mb.show()  # 显示消息窗

    def Hero_title_re(self, hero_title):  # 字符串的截取
        self.hero_title_list.clear()
        ul_text = str.split(hero_title, '|')  # 对文本进行分割并保存到列表中
        for i in ul_text:  # 遍历列表
            ii = ''.join(re.findall(r'[\u4e00-\u9fa5]', i))  # 提取str格式中的中文字符
            self.hero_title_list.append(ii)  # 保存到列表属性中

    def Hero_list(self):  # 获取所有英雄的ID和姓名
        url = 'https://pvp.qq.com/web201605/js/herolist.json'  # 请求地址
        try:
            response = requests.get(url, headers=self.headers, verify=False, timeout=10)  # 发起get请求获取数据
        except Exception:
            choice = QMessageBox.question(self.ui, '提示', '请检查网络.... ^_^', QMessageBox.Yes)
            if choice == QMessageBox.Yes:
                sys.exit()
        else:
            data = json.loads(response.text)  # 将str格式数据转为json格式数据
            for i in range(len(data)):  # 遍历获取英雄的ID和英雄的名字
                ID = data[i]['ename']
                NAME = data[i]['cname']
                self.Hero_dict[NAME] = ID  # 保存在字典属性中
            all_hero = list(self.Hero_dict.keys())  # 从字典属性中获取所有英雄
            self.ui.log_text.insertPlainText(str(list(all_hero)))  # 控件显示出文本

    def file_path(self):  # 选择文件夹方法
        file_url = QFileDialog.getExistingDirectory(self.ui, '选择路径', 'D:\Python_Pycharm\Python_PySide2')  # 选择文件夹
        self.ui.file_path.setText(file_url)  # 控件显示出文本

    def get_img_url(self):  # 获取指定皮肤标题的url
        hero_title = self.ui.skin_Box.currentText()  # 获取英雄皮肤标题
        if hero_title:
            file_path = self.ui.file_path.text()  # 获取文件夹路径
            if file_path:
                hero_name = self.ui.hero_name.text()  # 获取指定英雄名称
                indexes = self.hero_title_list.index(hero_title) + 1  # 获取
                img_url = 'https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{}/{}-bigskin-{}.jpg'.format(
                    self.Hero_dict[hero_name], self.Hero_dict[hero_name], indexes)
                self.img_download(img_url, file_path, hero_name, hero_title)
            else:
                self.MessageBox('请选择保存路径.... ^_^')
        else:
            self.MessageBox('请先选择皮肤标题.... ^_^')

    def img_download(self, img_url, file_path, hero_name, hero_title):  # 下载图片保存在指定路径
        img_content = requests.get(img_url, verify=False)  # 请求img_url的二进制数据
        hero_file_path = file_path + '/' + hero_name
        if not os.path.exists(hero_file_path):  # os判断文件夹如果不存在
            os.makedirs(hero_file_path)  # 创建文件夹
        hero_img_path = '{}/{}.JPEG'.format(hero_file_path, hero_title)
        with open(hero_img_path, 'wb') as f:
            f.write(img_content.content)
        self.ui.label_preview.setScaledContents(True)  # 自适应尺寸显示
        self.ui.label_preview.setPixmap(QPixmap(hero_img_path))
        self.ui.log_text.clear()
        self.ui.log_text.insertPlainText('{}/{} 高清壁纸下载完成.... ^_^'.format(hero_name, hero_title))  # 控件显示出文本

    def Hero_detail(self, hero_url):  # 获取指定英雄的壁纸
        response = requests.get(hero_url, headers=self.headers, verify=False, timeout=10)
        response.encoding = response.apparent_encoding  # 设置编码格式
        soup = BeautifulSoup(response.text, 'lxml')
        for ul in soup.select('.pic-pf ul'):
            ul_text = ul['data-imgname']
            self.Hero_title_re(ul_text)
            self.ui.log_text.clear()
            self.ui.log_text.insertPlainText(str(self.hero_title_list))  # 控件显示出文本
            self.ui.skin_Box.clear()
            self.ui.skin_Box.addItems(self.hero_title_list)

    def Hero_img(self):
        hero_name = self.ui.hero_name.text()
        if hero_name:
            Hero_name_test = self.Hero_dict.get(hero_name, None)
            if Hero_name_test:
                hero_url = 'https://pvp.qq.com/web201605/herodetail/{}.shtml'.format(self.Hero_dict[hero_name])
                self.Hero_detail(hero_url)
            else:
                self.MessageBox('英雄池没有 "{}" 英雄,请重新输入.... ^_^ '.format(hero_name))
                self.ui.hero_name.clear()
        else:
            self.MessageBox('请输入英雄名称.... ^_^')


if __name__ == '__main__':
    app = QApplication([])  # 初始化图形界面程序的底层管理功能
    app.setWindowIcon(QIcon('file/logo/hero_logo.png'))  # 加载 icon
    glory_window = Glory_Window()  # 实例化类
    glory_window.ui.show()  # 显示图形界面的所有控件
    app.exec_()  # 使QApplication的事件处理循环
