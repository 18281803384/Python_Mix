from pyquery import PyQuery as pq


html = '''
<div class="wrap">
<div id="container">
<ul class="list">
<li class="item-0">first item</li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
<li class="item-1 active"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div>
</div>
'''

print('----------------子节点---------------------')

# css选择器
doc = pq(html)
items = doc('.list')
print(type(items))
print(items)

# find()方法查询节点的所有子孙节点
lis = items.find("li")
print(type(lis))
print(lis)

# children()方法查询节点的子节点
lis = items.children()
print(lis)

# children()方法筛选节点
lis = items.children('.active')
print(lis)


print('----------------父节点---------------------')
items = doc('.list')
container = items.parent()
print(type(container))
print(container)

print('----------------祖先节点---------------------')
# parents() 返回所有的祖先节点
items = doc('.list')
parents = items.parents()
print(type(parents))
print(parents)

# parents() 传入css选择器筛选某个祖先节点
parents = items.parents('.wrap')
print(type(parents))
print(parents)

print('----------------兄弟节点---------------------')
li = doc('.list .item-0.active')
print(li.siblings())

# 筛选出某一个兄弟节点
print(li.siblings('.active'))

