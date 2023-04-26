import re

context = 'v'
print(len(context))

result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}', context)
print(result)
print(result.group())
print(result.span())

# 匹配目标
result1 = re.match('^Hello\s(.+)\sWorld', context)
print(result1)
print(result1.group())
print(result1.group(1))
print(result1.span())

# 通用匹配
result2 = re.match('^Hello.*Demo$', context)
print(result2)
print(result2.group())
print(result2.span())

# 贪婪与非贪婪
result3 = re.match('^He.*?(\d+).*Demo$', context)
print(result3)
print(result3.group(1))

# 修饰符
context1 = '''Hello 123 4567 World_This
           is a Regex Demo
           '''
result4 = re.match('^He.*?(\d+).*Demo$', context, re.S)
print(result4.group(1))


# 转义匹配
context5 = '(百度)www.baidu.com'

result5 = re.match('\(百度\)www\.baidu\.com', context5)
print(result5)