import json

strs = '''
[{
    "name": "Bob",
    "gender": "male",
    "birthday": "1992-10-18"
},{
    "name": "Selina",
    "gender": "female",
    "birthday": "1995-10-18"
},{
    "name": "王伟",
    "gender": "男",
    "birthday": "1992-10-18"
}]
'''

print('-----------读取JSON--------------------')

print(type(strs))

# 使用loads()方法将字符串转为JSON对象
data = json.loads(strs)

print(data)
print(type(data))

print(data[0]['name'])

# get()方法还可以传入第二个参数(即默认值)
print(data[0].get('name','zeng_cheng'))

print('-----------输出JSON--------------------')

with open('file/data.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(strs, ensure_ascii=False))

print('json文件存储成功')