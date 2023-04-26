# 作者: ZengCheng
# 时间: 2022/8/5
# 描述: 爬取免费可用的ip代理地址

import requests
from lxml import etree

# 目标网址
website = "https://free.kuaidaili.com/free/inha"
# 请求头协议
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36"
}
# 目标网址页数
page = 1


# 获取要请求的所有页地址
def get_url_all():
    url_list = []
    for i in range(1, page + 1):
        url_list.append(website + "/{}/".format(i))
    return url_list


# 获取代理ip地址并以列表形式返回
def get_proxies_ip():
    proxies_ip_list = []
    for url in get_url_all():
        str_html = requests.get(url, headers=header).text
        element_html = etree.HTML(str_html)
        IP_list = element_html.xpath('//td[@data-title="IP"]/text()')
        PORT_list = element_html.xpath('//td[@data-title="PORT"]/text()')
        for i in list(zip(IP_list, PORT_list)):
            proxies_ip_list.append(i[0] + ":" + i[1])
    return proxies_ip_list


# print(get_proxies_ip())