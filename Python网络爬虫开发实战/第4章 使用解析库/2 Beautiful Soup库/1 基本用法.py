from bs4 import BeautifulSoup

html = '''
<html><head><title>The Dormouse’ s story</title></head> 
<body> 
<p class="title" name="dromouse"><b>The Dormouse ’s story</b></p> 
<p class="story">Once upon a time there were three little sisters; and their names were 
<a href=”http://example.com/elsie" class=" sister”id="link1"><!-- Elsie --></a>, 
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and 
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>; 
and they lived at the bottom of a well.</p> 
<p class="story"> ... <Ip> 
'''

soup = BeautifulSoup(html, 'lxml')

# prettify()方法把要解析的字符串以标准的缩进格式输出
print(soup.prettify())

# 输出HTML中title节点的文本内容
print(soup.title.string)
