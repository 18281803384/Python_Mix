import requests
from pyquery import PyQuery as pq


html = '''
<div>
<ul>
<li class="item-0">first item</li>
<li class="item-0 active">first item</li>
</ul>
</div>
'''

print('------------字符串初始化----------------')
doc = pq(html)
print(doc('li'))

print('------------URL初始化----------------')
doc = pq(url='https://cuiqingcai.com')
print(doc('title'))

doc = pq(requests.get('https://cuiqingcai.com').text)
print(doc('title'))

print('------------文件初始化----------------')
doc = pq(filename='file/demo.html')
print(doc('li'))