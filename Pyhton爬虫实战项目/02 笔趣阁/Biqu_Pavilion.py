# 作者: ZengCheng
# 时间: 2022/8/5
# 描述: 爬取笔趣阁小说相关章节并下载
import os
import re
import urllib.parse
import requests
from lxml import etree
from prettytable import PrettyTable


# 下载小说
def download_hour(website, header, proxies):
    # ------- 获取每一章章节地址 -------#
    # 发起get请求
    response = requests.get(website, headers=header, proxies=proxies)
    # 设置网页响应的编码格式
    response.encoding = response.apparent_encoding
    # 获取响应文本,字符串格式
    str_html = response.text
    # 正则匹配书名
    book_name = re.findall('book_name" content="(.*?)"/>', str_html)[0]
    # 正则匹配章节url
    href_list = re.findall('<dd><a href="/(.*?)">.*?</a></dd>', str_html)
    # 列表截取,以获取需要下载的章节数
    href_list_z = href_list[0:]

    # ------- 请求章节地址获取然后保存 -------#
    # 判断文件夹是否存在
    if not os.path.exists('{}/'.format(book_name)):  # False
        # 创建文件夹
        os.makedirs('{}/'.format(book_name))
    # 判断文件是否存在
    if os.path.exists('{}/{}.txt'.format(book_name, book_name)):  # True
        # 删除文件
        os.remove('{}/{}.txt'.format(book_name, book_name))
    print('书名: {}   正在努力下载中... \t'.format(book_name))
    # 遍历列表数据
    for i in href_list_z:
        # 拼接章节完整地址
        chapter_url = website + i
        # 发起get请求
        response = requests.get(chapter_url, headers=header, proxies=proxies)
        # 设置网页响应的编码格式
        response.encoding = response.apparent_encoding
        # 获取响应文本,字符串格式
        str_html = response.text
        # 解析响应数据
        element_html = etree.HTML(str_html)
        # xpath获取章节标题
        chapter_name_sub = element_html.xpath('//h1/text()')[0]
        # 替换字符串中的特殊字符
        chapter_name = re.sub(r'[?*:"<>\\/|]', ' ', chapter_name_sub)
        # xpath获取内容
        content_list = element_html.xpath('//div[@id="content"]/text()')
        # 列表转为字符串
        content_str = "".join(content_list)
        print(chapter_name)
        # 指定路径保存章节标题和内容
        save_data_a(chapter_name, content_str, book_name)


# 按小说章节保存
def save_data_w(chapter_name, content_str, book_name):
    # 以写的方式打开指定路径文件,并写入数据
    with open('{}/{}.txt'.format(book_name, chapter_name), 'w', encoding='UTF-8') as f:
        f.write(chapter_name)
        f.write('\n')
        f.write('\n')
        f.write(content_str)


# 按小说书名保存
def save_data_a(chapter_name, content_str, book_name):
    # 以写的方式打开指定路径文件,并写入数据
    with open('{}/{}.txt'.format(book_name, book_name), 'a', encoding='UTF-8') as f:
        f.write(chapter_name)
        f.write('\n')
        f.write('\n')
        f.write(content_str)
        f.write('\n')
        f.write('\n')


# 搜索小说
def search_hour(website, header, proxies):
    # 发起get请求
    response = requests.get(website, headers=header, proxies=proxies)
    # 设置网页响应的编码格式
    response_encoding = response.apparent_encoding
    while True:
        book_name = input("请输入小说名称进行搜索: ")
        # 判断,如果书名字节小于4个字节,就停止程序
        if len(book_name.encode(response_encoding)) < 4:
            print('对不起，搜索关键字请不要少于 4 个字节!')
            continue
        # 把书名编码转为gb2312格式
        book_name_encode = book_name.encode('gb2312')  # 如果编码格式为utf-8，那么这一步可以省略
        # 对书名进行编码成ASCII字符
        book_name_quote = urllib.parse.quote(book_name_encode)
        # 默认查询的页数
        default_page_num = 1
        while True:
            # 搜索路径
            search_path = 'modules/article/search.php?searchkey={}&page={}'.format(book_name_quote, default_page_num)
            # 拼接搜索网址
            search_website = website + search_path
            # 发起get请求,对书名进行搜索
            response_search = requests.get(search_website, headers=header, proxies=proxies)
            # 设置网页响应的编码格式
            response_search.encoding = response_search.apparent_encoding
            # 获取响应文本,字符串格式
            search_html = response_search.text
            # 解析响应数据
            element_html = etree.HTML(search_html)
            # xpath获取搜索结果
            search_tr = element_html.xpath('//tr[@id="nr"]')
            # 判断如果没有搜索结果
            if not search_tr:
                print('抱歉，搜索没有结果^_^')
                break
            # xpath获取页数
            page_text = element_html.xpath('//em[@id="pagestats"]/text()')[0]
            # 分割字符串得到页数
            page_num = page_text.split('/')[1]
            # 小说字典,保存小说列表
            hour_dict = {}
            # 小说字典,排列数字
            dict_key_num = 1
            # 循环获取文章内容
            for tr in search_tr:
                # 把文章内容加入到小说字典中
                hour_dict[str(dict_key_num)] = {
                    # 文章名称
                    "article_name": tr.xpath('td[1]/a/text()')[0],
                    # 最新章节
                    "latest_chapter": tr.xpath('td[2]/a/text()')[0],
                    # 作者
                    "article_author": tr.xpath('td[3]/text()')[0],
                    # 字数
                    "word_number": tr.xpath('td[4]/text()')[0],
                    # 更新
                    "article_update": tr.xpath('td[5]/text()')[0],
                    # 状态
                    "article_state": tr.xpath('td[6]/text()')[0],
                    # 文章地址
                    "article_website": tr.xpath('td[1]/a/@href')[0],
                }
                # 给排列数字+1操作
                dict_key_num += 1

            # 创建表格
            tb = PrettyTable()
            # 设置表格名称
            tb.title = '搜索列表第{}页'.format(default_page_num)
            # 设置表头
            tb.field_names = ["文章序号", "文章名称", "最新章节", "作者", "数字", "更新", "状态"]
            # 循环添加表格行数据
            for k, v in hour_dict.items():
                tb.add_row(
                    [k, v["article_name"], v["latest_chapter"], v["article_author"], v["word_number"],
                     v["article_update"],
                     v["article_state"]])

            # 显示表格文章列表
            print(tb)
            if int(page_num) > 1:
                print('*****  选择是否进行翻页!  *****')
                print('********* <.上一页  *********')
                print('********* >.下一页  *********')
                # 用户选择功能
                while True:
                    select_function = input("请输入文章序号进行下载, 或者输入 <  > 符号翻页: ")
                    # 判断如果选择是翻页功能
                    if select_function in ('<', '>'):
                        # 判断,如果选择下一页
                        if select_function == '>':
                            # 判断页数是否到达了末页
                            if default_page_num == int(page_num):
                                print(' ^_^ 已为末页, 请重新输入 ！')
                            else:
                                # 对页数进行+1
                                default_page_num += 1
                                break
                        # 判断,如果选择上一页
                        else:
                            # 判断页数是否到达了首页
                            if default_page_num == 1:
                                print('^_^ 已为首页, 请重新输入 ！')
                            else:
                                # 对页数进行-1
                                default_page_num -= 1
                                break
                    # 判断如果选择是文章下载功能
                    try:
                        if int(select_function) in range(1, 31):
                            # 获取保存在字典里面的文章地址
                            hour_website = hour_dict[select_function]["article_website"]
                            # 调用函数下载文章
                            download_hour(hour_website, header, proxies)
                            return
                        else:
                            print('^_^ 输入有误, 请重新输入 ！')
                    except ValueError:
                        print('^_^ 输入有误, 请重新输入 ！')
            else:
                while True:
                    # 用户选择下载文章
                    select_article = input("请输入文章序号进行下载: ")
                    # 判断如果选择是文章下载功能
                    try:
                        if int(select_article) in range(1, 31):
                            # 获取保存在字典里面的文章地址
                            hour_website = hour_dict[select_article]["article_website"]
                            # 调用函数下载文章
                            download_hour(hour_website, header, proxies)
                            return
                        else:
                            print('^_^ 输入有误, 请重新输入 ！')
                    except ValueError:
                        print('^_^ 输入有误, 请重新输入 ！')


if __name__ == '__main__':
    # 小说目标地址
    website = 'https://www.qbiqu.com/'
    # 请求头协议
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36",
        'Connection': 'close'
    }

    # 获取代理地址列表
    ip_list = ['39.98.197.238:80']
    # 代理次数
    proxies_num = 0
    while True:
        # 代理
        proxies = {
            "http": 'http://{}'.format(ip_list[proxies_num])
        }
        # 显示使用的代理
        print('代理地址: {}  , 第{}次代理'.format(proxies["http"], proxies_num + 1))
        try:
            search_hour(website, header, proxies)
        except Exception:
            proxies_num += 1
            if proxies_num == len(ip_list):
                print("\n代理已用完！ 所属ip地段不可用  请稍后再试...")
                break
        else:
            break
