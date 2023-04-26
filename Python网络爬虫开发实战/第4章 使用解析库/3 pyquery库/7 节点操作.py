from pyquery import PyQuery as pq

html = '''
<div class="wrap">
Hello, World
<p>This is a paragraph.</p>
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

doc = pq(html)

li = doc('.item-0.active')
print(li)

# 移除信息
li.removeClass('active')
print(li)

# 添加信息
li.addClass('active')
print(li)

# 对li添加属性
li.attr('name', 'link')
print(li)

# 对li替换文本
li.text('changed item')
print(li)

# 对li替换文本
li.html('<span>changed item</span>')
print(li)


wrap = doc('.wrap')
print(wrap.text())

print('-----remove()------')
wrap.find('p').remove()
print(wrap.text())