import requests

data = {
    'name':'zeng_cheng',
    'age':24
}

# verify=False: requests设置移除SSL认证
r = requests.get('http://httpbin.org/get', params=data, verify=False)

print(type(r.text) )
print(r.json())
print(type(r.json()))