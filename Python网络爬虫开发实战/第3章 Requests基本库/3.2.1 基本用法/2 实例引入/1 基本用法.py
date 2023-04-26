import requests

r = requests.get('http://www.baidu.com')

# Response 类型
print( type(r) )

#状态码
print( r.status_code )

# 响应体的类型
print( type(r.text) )

# 响应体的内容
print( r.text )

# Cookies
print( r.cookies )

# 其他请求方式
r = requests.post('http://httpbin.org/post')
r = requests.put('http://httpbin.org/put')
r = requests.delete('http://httpbin.org/delete')
r = requests.head('http://httpbin.org/head')
r = requests.options('http://httpbin.org/options')