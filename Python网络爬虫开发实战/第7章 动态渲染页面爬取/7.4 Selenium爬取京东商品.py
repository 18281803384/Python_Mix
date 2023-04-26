# 目标: 爬取商品信息
import csv
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import warnings
from pyquery import PyQuery as pq
from selenium.webdriver.common.by import By

warnings.filterwarnings("ignore", category=DeprecationWarning)


# 保存数据方法
def save_data(price, title_text, shop):
    data = [price, title_text, shop]
    with open('file/save_data.csv', 'a', newline='', encoding='utf-8-sig') as f:  # 已追加的方法打开文件
        writer = csv.writer(f)
        writer.writerow(data)  # 一次写入一行


# 验证csv文件
def judgment_file():
    if os.path.exists("file/save_data.csv"):  # 判断csv文件如果存在
        print("file/save_data.csv 文件已存在,进行删除后再下载数据")
        os.remove("file/save_data.csv")  # 删除csv文件
    else:
        pass


# 解析html
def get_products(page_source):  # 解析html获取所需数据
    doc = pq(page_source)  # 字符串初始化
    ul_lis = doc('.gl-warp.clearfix li')  # li字段选择
    for item in ul_lis.items():  # 遍历所有的li标签
        title_text = item.find('.p-name.p-name-type-2 a em').text()  # 查找li标签下子节点的文本
        title_text = str(title_text.replace('\n','').replace('京品手机 ',''))
        if title_text:
            price = item.find('.gl-i-wrap .p-price strong').text()  # 查找li标签下子节点的文本
            price = str(price)
            shop = item.find('.gl-i-wrap .p-shop a').text()  # 查找li标签下子节点的文本
            shop = str(shop)
            img = item.find('.gl-i-wrap .p-img img').attr('src')  # 查找li标签下子节点的属性
            img = str(img)
            raw_text = price + '丨' + title_text + '丨' + shop  # 文本拼接
            save_data(price, title_text, shop)
    else:
        pass


# 获取每页数据方法
def get_pages():
    s = Service('C:\Program Files\Google\Chrome\Application/chromedriver.exe')  # Service传参,取消掉警告提示
    driver = webdriver.Chrome(service=s)  # 实例化一个浏览器对象
    driver.maximize_window()  # 设置窗口为最大化
    driver.get('https://www.jd.com/')  # chrome发起请求
    driver.find_element_by_xpath("//li[@class='cate_menu_item']/a[text()='手机']").click()  # 点击手机链接
    handles = driver.window_handles  # 获取当前全部窗口句柄集合
    for handle in handles:  # 切换窗口
        if handle != driver.current_window_handle:
            driver.close()  # 关闭第一个窗口
            driver.switch_to.window(handle)  # 切换到第二个窗口
    page = driver.find_element_by_xpath("//span[@class='p-skip']/em/b").text  # 获取页数
    page = 2
    for i in range(1,int(page)+1):
        js = "var q=document.documentElement.scrollTop=10000"
        driver.execute_script(js)  # 自向下滚动页面到底部
        time.sleep(5)  # 等待5秒钟
        driver.find_element_by_xpath("//span[@class='p-skip']/input").clear()  # 清空输入框
        driver.find_element_by_xpath("//span[@class='p-skip']/input").send_keys(i)  # 输入页数
        time.sleep(2)  # 等待2秒钟
        driver.find_element_by_xpath("//span[@class='p-skip']/a").click()  # 点击确定按钮
        js = "var q=document.documentElement.scrollTop=10000"
        driver.execute_script(js) # 自向下滚动页面到底部
        time.sleep(10)  # 等待5秒钟
        print('第{}页开始下载中...'.format(i))
        get_products(driver.page_source)
    print('一共{}页下载完成!!! \n'.format(page))
    time.sleep(5)  # 等待5秒钟
    driver.quit()  # 关闭窗口,结束程序


# 主方法
def main():
    judgment_file()
    get_pages()


if __name__ == "__main__":
    main()