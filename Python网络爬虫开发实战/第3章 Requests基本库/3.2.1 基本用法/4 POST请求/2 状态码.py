import requests

r = requests.get('http://www.baidu.com')

exit() if not r.status_code == requests.codes.ok else print("Request Successfully")