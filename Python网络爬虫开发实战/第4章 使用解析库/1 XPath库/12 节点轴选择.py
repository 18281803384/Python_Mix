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


# 获取li节点的所有祖先节点
result = html.xpath("//li[1]/ancestor::*")
print(result)

# 获取li节点的div祖先节点
result = html.xpath("//li[1]/ancestor::div")
print(result)

# 获取li节点的所有属性值
result = html.xpath("//li[1]/attribute::*")
print(result)

# 获取li节点的所有子节点,但是限定a节点
result = html.xpath("//li[1]/child::a[@href='link1.html']")
print(result)

# 取li节点的所有子孙节点,但是限定span节点
result = html.xpath("//li[1]/descendant::span")
print(result)

# 取li节点后所有节点,但是索引第二个后续节点
result = html.xpath("//li[1]/following::*[2]")
print(result)

# 取li节点后所有同级节点,
result = html.xpath("//li[1]/following-sibling::*")
print(result)