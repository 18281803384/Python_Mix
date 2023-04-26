import requests

proxies = {
    'https': '106.75.22.218:80'
}

r = requests.get('https://www.taobao.com',proxies=proxies)

print(r.text)