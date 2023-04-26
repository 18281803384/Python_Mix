from lxml import etree

html = etree.parse('file/test.html', etree.HTMLParser())

result = html.xpath('//li/a/@href')

print(result)