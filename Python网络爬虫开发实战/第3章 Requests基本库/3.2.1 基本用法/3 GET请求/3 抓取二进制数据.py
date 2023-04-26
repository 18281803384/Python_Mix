import requests

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'
}

r = requests.get('http://www.zhihu.com/favicon.ico', headers=headers)
with open('favicon.ico', 'wb') as f:
    f.write(r.content)