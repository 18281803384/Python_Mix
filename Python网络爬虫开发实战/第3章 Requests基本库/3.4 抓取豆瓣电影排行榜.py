import re
import requests
import urllib3


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def get_one_page(url):
    headers = {
        'Accept': 'application/json',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',
        'Host': 'movie.douban.com'
    }

    response = requests.get(url, headers=headers, verify=False)

    if response.status_code == 200:
        # print(response.text)
        pattern = re.compile(r'class="item">.*?"">(.*?)</em>.*?src="(.*?)".*?title">(.*?)</span>.*?导演:(.*?)&.*?<br>.*?(\d{4}).*?/&nbsp;(.*?)&nbsp;.*?/&nbsp;.*?</p>.*?average">(.*?)</span>.*?<span>.*?(.*?)</span>.*?class="inq">(.*?)</span>', re.S)
        response = re.findall(pattern, response.text)
        for result in response:
            print(result)

    else:
        return '数据获取失败', response.status_code


def main():
    for i in range(0,250,25):
        url = 'https://movie.douban.com/top250?start={}'.format(i)
        html = get_one_page(url)
        # print(url)


if __name__ == '__main__':
    main()
