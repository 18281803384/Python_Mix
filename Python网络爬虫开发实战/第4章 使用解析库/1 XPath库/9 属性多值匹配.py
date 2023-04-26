from lxml import etree

html = etree.parse('file/test.html', etree.HTMLParser())

result = html.xpath('//li[contains(@class, "li")]/a/text()')

print(result)