import re

from bs4 import BeautifulSoup

html = '''
<div class="panel">
<div class="panel-heading">
<h4>Hello</h4>
</div>
<div class="panel-body">
<a>Hello, this is a link</a>
<a>Hello, this is a link, too</a>
<ul class="list" id="list-1" name="elements">
<li class="element">Foo</li>
<li class="element">Bar</li>
<li class="element">Jay</li>
</ul>
<ul class="list" id="list-2">
<li class="element">Foo</li>
<li class="element">Bar</li>
</ul>
</div>
</div>
'''

soup = BeautifulSoup(html, 'lxml')


print('-------------find_all()----------------------')
# find_all 查询所有符合条件的元素
print(soup.find_all(name='ul'))
print(soup.find_all(name='ul')[0])

# for查询其内部的li节点
for ul in soup.find_all(name='ul'):
    print(ul.find_all(name='li'))
    # 再for查询其内部的li文本
    for li in ul.find_all(name='li'):
        print(li.string)


# attrs传入属性来查询
print(soup.find_all(attrs={'id': 'list-1'}))
print(soup.find_all(attrs={'name': 'elements'}))

# 查询常用属性
print(soup.find_all(id = 'list-1'))
print(soup.find_all(class_ = "element"))

# text参数匹配节点的文本
print(soup.find_all(text=re.compile("link")))


print('-------------find()----------------------')
print(soup.find(name = 'ul'))
print(type(soup.find(name = 'ul')))
print(soup.find(class_ = 'list'))