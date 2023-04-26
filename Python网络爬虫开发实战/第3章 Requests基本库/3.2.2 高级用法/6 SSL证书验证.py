import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

response = requests.get('http://www.12306.cn', verify=False)

print(response.status_code)
