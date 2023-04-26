import requests
import re

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'
}

r = requests.get("http://www.zhihu.com/explore", headers=headers)
pattern = re.compile('"og:description" content="(.*?)"/><link', re.S)
titles = re.findall(pattern, r.text)
print(titles)