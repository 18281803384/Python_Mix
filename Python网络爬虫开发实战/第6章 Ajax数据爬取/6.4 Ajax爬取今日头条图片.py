import json
import os.path
import re
import jsonpath
import requests
import urllib3
from tqdm import tqdm

urllib3.disable_warnings()


def request_url_text(url, page_num, keyword):
    # 自定义请求头
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',
        'Cookie': 'msToken=5AScfJwbF3hmJmOSQh-k41m3QiRCHhRhyY2L6VZfuXd-wn_tPpGbQMKV-cbgSRLiUnTCfusayv7fH3tCQw8ABuMhfqGzDp2LW_bBH_3GUkOQ; tt_webid=7104145721603868191; _S_DPR=1.25; _S_IPAD=0; MONITOR_WEB_ID=7104145721603868191; ttwid=1%7Cm0iwBU7zZ-aXPp_MXFoSIjGhkYWH9G4at6QDEGvqFIU%7C1654063623%7Ca94230b1a6b4738f86ff3e4cd21772b9c0e2ef0ae443d37cc5e5061bc7d929df; _S_WIN_WH=1536_722'
    }

    # 发送get请求
    response = requests.get(url, headers=headers, verify=False, timeout=5)

    # 请求状态码为200则继续执行,否则请求失败
    if response.status_code == 200:
        # 把获取的str类型数据转换为json格式对象
        response = json.loads(response.text)
        # 利用jsonpath获取data字段的数据
        datas = jsonpath.jsonpath(response, "$..data")[0]
        # 遍历datas列表分别获取里面的数据
        for i in tqdm(range(len(datas))):
            # 利用jsonpath获取图片的地址
            img_url = jsonpath.jsonpath(datas[i], "$..img_url")[0]
            # 利用jsonpath获取图片的标题
            img_title = jsonpath.jsonpath(datas[i], "$..text")[0]
            # 请求img_url的二进制数据
            img_content = requests.get(img_url, verify=False)
            # 调用保存图片方法
            save_img(img_content.content, img_url, page_num, i, keyword)
    else:
        # 返回请求失败状态码
        return '数据获取失败', response.status_code


def save_img(img_content, img_url, page_num, i, keyword):
    # 正则表达式提取图片后边的后辍
    result = re.findall(r"x\d{3}(.*)", img_url)

    folder_path = 'img'
    keyword_path = 'img/{}'.format(keyword)
    pate_path = 'img/{}/第{}页'.format(keyword, page_num + 1)
    file_os(folder_path)
    file_os(keyword_path)
    file_os(pate_path)

    img_path = 'img/{}/第{}页/{}_{}{}'.format(keyword, page_num + 1, keyword, i + 1, result[0])
    # os判断img_path文件如果不存在
    if not os.path.exists(img_path):
        with open(img_path, 'wb') as f:
            f.write(img_content)
    else:
        print('\n {} 文件已存在'.format(img_path))


def file_os(file_path):
    # os判断file_path文件夹如果不存在
    if not os.path.exists(file_path):
        # 创建file_path文件夹
        os.makedirs(file_path)


# 主方法入口
def main():
    # 搜索关键字
    keyword = '原神'
    # 页数
    page_num = 4

    for i in range(page_num):
        # 请求地址
        request_url = 'https://so.toutiao.com/search?keyword={}&pd=atlas&source=input&dvpf=pc&aid=4916&page_num={}&rawJSON=1'.format(keyword, i)
        print(' {}第{}页开始下载中...'.format(keyword, i + 1))
        request_url_text(request_url, i, keyword)
        print(' {}第{}页下载完成!!! \n'.format(keyword, i + 1))


# 程序运行入口
if __name__ == '__main__':
    main()
