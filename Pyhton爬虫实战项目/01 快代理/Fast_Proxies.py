# 作者: ZengCheng
# 时间: 2022/8/5
# 描述: 爬取目标地址获取免费可用的ip代理地址

import requests
from lxml import etree


def get_proxies_ip(page=1):
    """
    :param page: 自定义需要获取数据的页数
    :return: 获取的代理ip地址；例：['117.68.195.56:9999', '115.29.170.58:8118']
    """
    # 目标网址
    website = "https://www.kuaidaili.com/free/inha/"
    # 自定义请求头协议
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36"
    }

    # 定义一个空列表，用于存放每次循环拼接后的每页地址
    url_list = []
    for i in range(1, page + 1):
        url_list.append(website + "/{}/".format(i))

    # 定义一个空列表，用于存放每次循环拼接后的代理ip地址
    proxies_ip_list = []
    for url in url_list:
        str_html = requests.get(url, headers=header).text
        element_html = etree.HTML(str_html)
        IP_list = element_html.xpath('//td[@data-title="IP"]/text()')
        PORT_list = element_html.xpath('//td[@data-title="PORT"]/text()')
        for i in list(zip(IP_list, PORT_list)):
            proxies_ip_list.append(i[0] + ":" + i[1])
    return proxies_ip_list


print(get_proxies_ip())