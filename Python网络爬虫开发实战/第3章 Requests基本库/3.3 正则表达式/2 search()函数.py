import re

content = 'Extra stings Extra stings Hello  1234567 World Th is is a Regex Demo Extra  stings Extra stings'
content1 = '''
<div id="songs-list"> 
<h2 class＝气itle”>经典老歌</h2>
<p class=”introduction”>经典老歌列表</p> 
<ul id=”list” class=”list-group”>
<li data-view="2”>一路上有你</li>
<li data-view="7”><a href＝”/2.mp3” singer＝”任贤齐”>沧海一卢笑</a></li> 
<li data-view=”4” class=”active"><a href＝”/3.mp3” singer＝”齐泰”>往事随风</a></li> 
<li data-view=”6”><a href＝”/4.mp3” singer＝”beyond”>光辉岁月</a></li>
<li data-view=”5”><a href＝”/5.mp3” singer＝”陈慧琳”>记事本</a></li>
<li data-view=“5”><a href＝”/6.mp3” singer＝”邓丽君”>但愿人长久</a></li> 
</ul>
</div>
'''

result = re.search('Hello.*?(\d+).*?Demo', content)

print(result)

result1 = re.search('singer＝”(.*?)”>(.*?)</a>', content1, re.S)

if result1:
    print(result1.group(1), result1.group(2))
