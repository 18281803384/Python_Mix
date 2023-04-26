# 作者: ZengCheng
# 时间: 2022/8/9
import json
import os
import urllib.parse
import requests
from prettytable import PrettyTable
import Fast_Proxies


def main(ip_list):
    while True:
        music_name_input = input("请输入音乐名称（-1退出）: ")
        # 输入歌名时、输入的-1 就退出
        if music_name_input == '-1':
            break
        # 代理次数
        proxies_num = 0
        while True:
            # 设置代理
            proxies = {
                "http": 'http://{}'.format(ip_list[proxies_num])
            }
            # 显示使用的代理
            print('代理地址: {}  , 代理次数{}'.format(proxies["http"], proxies_num))
            # 目标地址
            website = 'http://www.kuwo.cn'
            try:
                # 对音乐名称进行编码成ASCII字符
                music_name_quote = urllib.parse.quote(music_name_input)
                # 请求头协议
                header = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36",
                    "Cookie": "_ga=GA1.2.2044940001.1660029306; Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1660029306,1660180501; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1660180501; _gid=GA1.2.969805937.1660180501; _gat=1; kw_token=I9OHC3BJSC",
                    "Referer": "http://www.kuwo.cn/search/list?key={}".format(music_name_quote),
                    "csrf": "I9OHC3BJSC"
                }
                # 拼接完整的请求地址
                search_music_url = '{}/api/www/search/searchMusicBykeyWord?key={}&pn=1&rn=10&httpsStatus=1'.format(website, music_name_quote)
                # 发起get请求
                response = requests.get(search_music_url, headers=header, proxies=proxies)
                # 设置网页响应的编码格式
                response_encoding = response.apparent_encoding
                try:
                    # 剔除字符串中不需要的字符
                    new_response = response.text.replace('&nbsp;', '')
                except json.decoder.JSONDecodeError:
                    continue
                # 将响应转为json格式
                response_json = json.loads(new_response)
                # 获取查询出来的歌曲列表
                music_list = response_json["data"]["list"]
                # 歌曲列表序号
                music_num = 1
                # 创建表格
                tb = PrettyTable()
                # 设置表头
                tb.field_names = ["序号", "歌曲", "歌手", "专辑", "时长"]
                # 循环取歌曲列表中每一首歌曲的详情
                for music_detail in music_list:
                    # 循环添加表格行数据
                    tb.add_row([music_num, music_detail["name"], music_detail["artist"], music_detail["album"], music_detail["songTimeMinutes"]])
                    # 歌曲列表序号+1
                    music_num += 1
                print(tb)
                while True:
                    music_serial_number_input = input("请输入要下载歌名序号（-1退出）: ")
                    # 输入歌名序号时、输入的-1 就退出
                    if music_serial_number_input == '-1':
                        break
                    try:
                        # 获取到歌曲的rid
                        music_rid = music_list[int(music_serial_number_input) - 1]["rid"]
                    except ValueError:
                        print('^_^ 输入有误, 请重新输入 ！')
                        continue
                    # 拼接完整的歌曲请求地址
                    music_playUrl = '{}/api/v1/www/music/playUrl?mid={}&type=music&httpsStatus=1'.format(website, music_rid)
                    # 发起get请求
                    response = requests.get(music_playUrl, headers=header, proxies=proxies)
                    # 设置网页响应的编码格式
                    response_encoding = response.apparent_encoding
                    # 将响应转为json格式
                    response_json = json.loads(response.text)
                    # 获取歌曲的url地址
                    try:
                        music_url = response_json["data"]["url"]
                    except KeyError:
                        print('^_^ VIP歌曲暂时无法支持下载, 请重新选择 ！')
                        continue
                    # 发起get请求
                    response = requests.get(music_url, headers=header, proxies=proxies)
                    # 获取歌手名
                    singer = music_list[int(music_serial_number_input) - 1]["artist"]
                    # 获取音乐名
                    music_name = music_list[int(music_serial_number_input) - 1]["name"]
                    # 调用函数下载歌曲
                    download_music(response, singer, music_name)
                    break
            except (requests.exceptions.ProxyError, requests.exceptions.ChunkedEncodingError):
                proxies_num += 1
                continue
            break
        break


# 下载歌曲
def download_music(response, singer, music_name):
    # 判断文件夹是否存在
    if not os.path.exists('{}/'.format(singer)):  # False
        # 创建文件夹
        os.makedirs('{}/'.format(singer))
    # 以写的方式打开指定路径文件,并写入数据
    with open('{}/{}-{}.mp3'.format(singer, music_name, singer), 'wb') as f:
        f.write(response.content)
    print('{} 音乐下载完成! ^_^ '.format(music_name))


if __name__ == '__main__':
    main(Fast_Proxies.get_proxies_ip())

