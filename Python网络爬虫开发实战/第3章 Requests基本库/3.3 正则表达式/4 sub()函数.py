import re

content = '54aKS4yrsoiRS4ixSL2g'

# 修改文本
content = re.sub('\d+', '', content)
print(content)