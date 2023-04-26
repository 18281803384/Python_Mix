from bs4 import BeautifulSoup

html = '''
<html><head><title>The Dormouse’ s story</title></head> 
<body> 
<p class="title" name="dromouse"><b>The Dormouse ’s story</b></p> 
<p class="story">Once upon a time there were three little sisters; and their names were 
<a href=”http://example.com/elsie" class=" sister”id="link1"><span><!-- Elsie --></span></a> 
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and 
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>; 
and they lived at the bottom of a well.</p> 
<p class="story"> ... </p> 
'''

soup = BeautifulSoup(html, 'lxml')

print("-----选择元素-----")
print(soup.title)
print(type(soup.title))
print(soup.title.string)
print(soup.head)
print(soup.p)

print("-----提取信息-----")
# 获取名称
print(soup.title.name)

# 获取属性
print(soup.p.attrs)
print(soup.p.attrs['name'])
print(soup.p['name'])
print(soup.p['class'])

# 获取内容
print(soup.p.string)

print("-----嵌套选择----")
print(soup.head.title)
print(type(soup.head.title))
print(soup.head.title.string)

print("-----关联选择----")
print(soup.p.contents)
print(soup.p.children)
# children获取所有子节点的列表
for i, child in enumerate(soup.p.children):
    print(i, child)

# descendants获取所有的子孙节点
print(soup.p.descendants)
for i, child in enumerate(soup.p.descendants):
    print(i, child)

# 获取a节点的父节点
print(soup.a.parent)
# 获取a节点所有的父节点
print(soup.a.parents)

# 同级节点
# 获取上一个
print(soup.a.next_sibling)
# 获取下一个
print(soup.a.prev_sibling)
# 获取前面所有
print(list(enumerate(soup.a.next_siblings)))
# 获取后面所有
print(list(enumerate(soup.a.prev_siblings)))