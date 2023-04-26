import datetime
import json
import jsonpath
import requests
import urllib3
from bs4 import BeautifulSoup

urllib3.disable_warnings()


# 获取每页url地址参数,再获取每页的微博内容数据 方法
def get_page(url, headers):
    # 发送get请求
    response = requests.get(url, headers=headers, verify=False, timeout=5)

    # 请求状态码为200则继续执行,否则请求失败
    if response.status_code == 200:
        # 把获取的str类型数据转换为json格式对象
        response = json.loads(response.text)
        # 利用jsonpath分别获取所需字段内容
        since_id = jsonpath.jsonpath(response, "$..since_id")[0]
        lists = jsonpath.jsonpath(response, "$..list")[0]
        # 把获取的数据返回回去
        return since_id, lists
    else:
        # 返回请求失败状态码
        return '数据获取失败', response.status_code


# 获取微博话题的所有
def expand_content(mblogid_url, headers):
    # 发送get请求
    response = requests.get(mblogid_url, headers=headers, verify=False,  timeout=5)

    # 请求状态码为200则继续执行,否则请求失败
    if response.status_code == 200:
        # 把获取的str类型数据转换为json格式对象
        response = json.loads(response.text)
        # 程序异常用法
        try:
            # 利用jsonpath分别获取所需字段内容
            longTextContent = jsonpath.jsonpath(response, "$..longTextContent")[0]
            # 把获取的数据返回回去
            return longTextContent
        except:
            return None
    else:
        # 返回请求失败状态码
        return '数据获取失败', response.status_code


# UTC时间格式转标准字符串
def format_creation_time(time_str):
    str2 = time_str[0:-10] + time_str[-10:].split(" ")[-1]
    dt = datetime.datetime.strptime(str2, '%a %b %d %H:%M:%S %Y') + datetime.timedelta(hours=0)
    return dt.strftime("%Y-%m-%d %H:%M:%S")


# 主方法
def main():
    # 自定义cookies
    cookies = 'SINAGLOBAL=5869885526194.922.1653984191527; ULV=1653984191550:1:1:1:5869885526194.922.1653984191527:; XSRF-TOKEN=W6bDF0FFnW69Or3D63s9tMrw; SUB=_2A25PkrEsDeRhGeBL61AT9SbFyzWIHXVs6aXkrDV8PUNbmtAfLWuikW9NR0uIVGwK_tu9v4ySCZc76bDxP-Iw5xyq; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5A9Qf8McW6G1cmu9JfS1VL5JpX5KzhUgL.FoqfehzESKn4eh.2dJLoI0qLxKnL1KqL1hBLxKnL12BLBoMLxK-LBo5L1K2LxK-LBo.LBoBLxK-L1hML1h.LxKBLBonLBoqt; ALF=1685583099; SSOLoginState=1654047100; WBPSESS=Dt2hbAUaXfkVprjyrAZT_OaLGgnIbMMghx3VyFihO-C7s99chpMCDOfF5h38i7gpe9olz00sptzgci9qcJa2BcBuAmZjR11EbMiUuzJCwqowj0pCXWBU0uF9cvqafM3yp76OSySKnXXy0kPoR_E4_MLlQx1UvZOIL1EigOwC79enYhw1F2PUgKwfupjqcVGwVVqWZV-qQCjQqaVbVdR2Qg=='
    # 数据对象id
    uid = 3859193849
    # 每页地址的动态参数
    since_id = ''
    # 页数
    page = 1

    # 自定义请求头
    header = {
        'Accept': 'application/json, text/plain, */*',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',
        'cookie': cookies
    }

    # 循环获取n页的微博话题内容
    for i in range(page):
        # 请求地址
        url = "https://www.weibo.com/ajax/statuses/mymblog?uid={}&page={}&feature=0&since_id={}".format(uid, i+1, since_id)
        # 调用get_page方法获取每页url地址参数,再获取每页的微博内容数据
        since_id, lists = get_page(url, header)
        # 循环遍历提取lists列表中的数据
        for ii in range(len(lists)):
            # 置顶
            try:
                isTop = jsonpath.jsonpath(lists[ii], '$..isTop')[0]
            except:
                isTop = 0
            if isTop == 1:
                print('【置顶】')
            else:
                pass
            # 时间
            created_at_CTU = jsonpath.jsonpath(lists[ii], '$..created_at')[0]
            created_at = format_creation_time(created_at_CTU)
            print('[', end='')
            print('发布时间: ' + created_at, end='  ')
            # 由什么发布
            print('来自: ' + jsonpath.jsonpath(lists[ii], '$..source')[0], end='')
            print(']')
            # 微博完整内容
            mblogid = jsonpath.jsonpath(lists[ii], '$..mblogid')[0]
            mblogid_url = "https://weibo.com/ajax/statuses/longtext?id={}".format(mblogid)
            mblogid_raw = expand_content(mblogid_url, header)
            if mblogid_raw != None:
                print(mblogid_raw, end='\n------------------------------------------------------------\n')
            else:
                text_raw = jsonpath.jsonpath(lists[ii], '$..text_raw')[0]
                print(text_raw, end='\n------------------------------------------------------------\n')


# 启动程序 方法
if __name__ == '__main__':
    try:
        main()
    except:
        print('cookie 过期 ！  请更新')