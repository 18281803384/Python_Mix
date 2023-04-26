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


# 选择一个li节点
result = html.xpath("//li[1]/a/text()")
print(result)

# 选择最后一个li节点
result = html.xpath("//li[last()]/a/text()")
print(result)

# 选择位置小于3的li节点
result = html.xpath("//li[position()<3]/a/text()")
print(result)

# 选择了倒数第三个li节点
result = html.xpath("//li[last()-2]/a/text()")
print(result)