# 需求: 保存知乎上"发现"页面的"热门话题"部分,将其问题和答案统一保存成文本形式。
# 三方库: requests、pyquery
import re

import requests
from pyquery import PyQuery as pq
import urllib3

urllib3.disable_warnings()

url = 'https://www.zhihu.com/hot'
headers = {
    'Accept': 'application/json',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',
    'cookie': '_zap=5f32cb2a-6fa5-427f-8aed-a53314bf2d0a; d_c0="AUBQweYP5hSPThsib7R-w6eAMBNarQ7VwVw=|1651816590"; captcha_session_v2=2|1:0|10:1651816598|18:captcha_session_v2|88:VWdJdGlJZ0dyS3pYWm1iRUtacWthQkhhZ3MzUGhsdkFTejNSL044eTZFVm12Y1AyMHI5S1RDRXM2QWp4VmR4OQ==|b4e594d863b50cc9647818fa78c556f106cc50222ee6f13f6285b00d59aca88b; captcha_ticket_v2=2|1:0|10:1651816606|17:captcha_ticket_v2|704:eyJ2YWxpZGF0ZSI6IkNOMzFfRW1FaUkydGZCWEZtSi1Xb2xxS2prRENya3JOVGlOa2ZIQm5WVXlLQldRUnN4NzZ4SzZlUVltVnhvUGZBVVhmWW5PUXdkbW9fQk44T0w3MjVqZjBEbTcybldLNGo1WlBSYl9Qd3l0d0MwZXJUeWs1RWZQY2dQdnZlRUpMLmZQQnUwa29mLUdGYzZjc1g1N1FqR1FsWjlaSDBjRms1NXJYRWFGQjhhSEtfRmhKa2taR2puLXJZUHltNjBOY3Q1UmZ6Qno2TXA4b01JODZZSnNyeVZBeFlUcmtDS1EtLTBnNU9EYXhaMldxUFBGRXJpa3B5MGlTSEFxZndFd2dmSml3OTdJc1otVEFHQ24xWVdRRjJMRzQuN2YwYTA5elRzbThfWmNNREJEcWNUalVuLlVveXlvaXpxMlBqYWxwQldkOTBFSWVtVzVndm9yZTdkVXh4amd4RGRQRDVFclFaek02dEJsVkpDbzIuQjd6Vy45cUdPTjBnX3ZvNGg4anQ3b2xQMWsuVktnU0JEZFdMVjY5akt0WWFjV1g5VEZJcHFGdERGeVh6V3RWMlFHc1Z1RzBCS0NCR0J5OGdobC1oVmZVeHl6ejJUUHZkUElJcENobnZJYk92SUhBelJqZzQuNi53bTFNZERDckVoOFJEU1R0dllfOW1QME9La19yMyJ9|a07e9d449ee1da27b6f3bc6f0cfb058087cf68e44daeb270dc2067c9a6768581; z_c0=2|1:0|10:1651816615|4:z_c0|92:Mi4xZjdMbUV3QUFBQUFCUUZEQjVnX21GQ1lBQUFCZ0FsVk5wd1ppWXdEMjBTZWs3UXJQdDRsV3Vja3U0MnFRYWdya0xn|36f0eb00e60f6740d9e09ceddf0b6a2ef2bcce41476b2c69bd5f83d6f49181fb; q_c1=f7f88c04c0e5479db8a634f33d7e8e2c|1652170381000|1652170381000; ISSW=1; _xsrf=b35y1eanpBdV6O8x3RFUna02lSUQHU2C; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1653284934,1653356675,1653536235,1653639128; NOT_UNREGISTER_WAITING=1; SESSIONID=vzVEATc5Hz5tuKQi7fktqxt0WPS7xx6LWLHX1nnXN7F; JOID=VFwXC0hGr8WgZnRxKkjIXMXgL506MtOZ7iIiFBUL1_beGDoiRREqVMxhcH0rIu1nnRGFc7sQdBlD2EpJZWkJsrY=; osd=U10RAkpBrsOpZHNwLEHKW8TmJp89M9WQ7CUjEhwJ0PfYETglRBcjVstgdnQpJexhlBOCcr0Zdh5C3kNLYmgPu7Q=; SUBMIT_0=1ecc9118-1594-4a78-907c-afde017cb16f; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1653639736; tst=h; KLBRSID=cdfcc1d45d024a211bb7144f66bda2cf|1653639801|1653639126'
}

print('开始获取知乎热榜中！！！！')

html = requests.get(url, headers=headers, verify=False).text
doc = pq(html)
# 获取所有问题
HotItem = doc('#TopstoryContent .HotItem').items()

with open('file/explore.txt', 'w', encoding='utf-8') as f:
    for i in HotItem:
        # 获取排行编号
        HotItem_rank = i.find('.HotItem-rank').text()

        # 获取问题标题
        HotItem_title = i.find('.HotItem-title').text()

        # 获取问题的答案
        HotItem_excerpt = i.find('.HotItem-excerpt').text()
        if HotItem_excerpt:
            pass
        else:
            HotItem_excerpt = '没有答案!!!!!'

        # 获取问题的图片
        img = i.find('img').attr('src')
        if img:
            pass
        else:
            img = '没有图片!!!!!'

        # 获取问题的热度值
        HotItem_metrics = i.find('.HotItem-metrics').text()
        HotItem_metrics = HotItem_metrics.replace('\n', '')
        pattern = re.compile('}(.*?)分')
        HotItem_metrics = re.findall(pattern, HotItem_metrics)[0]

        f.write('\n'.join([HotItem_rank, HotItem_title, HotItem_excerpt, img, HotItem_metrics]))
        f.write('\n' + '=' * 50 + '\n\n')

print('知乎热榜问题获取完毕！！！！, 保存在当前下file/explore.txt文件中')