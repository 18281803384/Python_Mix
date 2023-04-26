from lxml import etree

text = '''
<div> 
<ul> 
<li class="item-O"><a href="link1.html">first item</a></li> 
<li class="item-1"><a href="link2.html">second item</a></li> 
<li class="item-inactive"><a href="link3.html">third item</a></li> 
<li class="item-1"><a href="link4.html">fourth item</a></li> 
<li class="item-0"><a href="ink5.html">fifth item</a> 
</ul> 
</div>
'''

# etree模块可以自动修正HTML文本
html = etree.HTML(text)

# tostring()方法可以输出修正后的HTML文本,结果为bytes类型
result = etree.tostring(html)

# 利用decode()方法将其转成str类型
print(result.decode('UTF-8'))