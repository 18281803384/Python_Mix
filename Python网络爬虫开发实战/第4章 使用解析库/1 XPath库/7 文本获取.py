from lxml import etree

html = etree.parse('file/test.html', etree.HTMLParser())

result = html.xpath('//li[@class="item-0"]/a/text()')
result1 = html.xpath('//li[@class="item-0"]//text()')

print(result)
print(result1)