import requests

r = requests.get('https://www.taobao.com',timeout=2)

print(r.status_code)