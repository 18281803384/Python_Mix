# 作者: ZengCheng
# 时间: 2022/10/12
import csv
import json
import os
import re
import pandas as pd
from lxml import etree
import pymysql
import requests
from pymysql import *
from sqlalchemy import create_engine


class spider(object):
    # 构造函数
    def __init__(self):
        # 电影列表页面地址
        self.spiderUrl = 'https://m.douban.com/rexxar/api/v2/movie/recommend?refresh=0&count=20&selected_categories=%7B%7D&sort=T&tags='
        # 请求头
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36',
            'Referer': 'https://movie.douban.com/explore',
            'Cookie': 'll="118318"; bid=SMXcM0F8ur0; __utmv=30149280.20614; douban-fav-remind=1; ct=y; __utmc=30149280; dbcl2="206144561:uSxzw/4ZSJE"; ck=nhYI; __utmz=30149280.1666590134.14.2.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; push_noty_num=0; push_doumail_num=0; frodotk="13bb0187facd119c3b310497f06734d4"; __utma=30149280.2018025655.1661740815.1666590134.1666592869.15; __utmt=1; __utmb=30149280.2.10.1666592869'
        }
        # 连接数据库
        self.conn = connect(host='192.168.174.100', port=3306, user='root', password='Mm18095577363!',database='Dou_Ban_Data', charset='utf8mb4')
        # 获取游标
        self.cursor = self.conn.cursor()

    # 析构函数
    def __del__(self):
        # 关闭游标
        self.cursor.close()
        # 关闭数据库连接
        self.conn.close()

    # 初始函数，构建页数txt文件，构建数据库表结构
    def init(self):
        if not os.path.exists('./spiderPage.txt'):  # 判断,当不存在该csv文件时
            with open('./spiderPage.txt', 'w', encoding="utf-8") as w_f:  # 创建csv文件并写入一行列表数据
                w_f.write('0\n')

        # SQL语句创建movie表
        sql = '''
                CREATE TABLE movie (
                    id INT PRIMARY KEY auto_increment comment 'ID',
                    move_directors VARCHAR(255) comment '电影导演',
                    move_score VARCHAR(255) comment '电影评分',
                    move_name VARCHAR(50) comment '电影名字',
                    move_actor VARCHAR(2000) comment '电影演员',
                    move_cover VARCHAR(255) comment '电影封面',
                    move_DatailsLink VARCHAR(255) comment '电影详情链接',
                    move_year VARCHAR(255) comment '电影年份',
                    move_types VARCHAR(255) comment '电影类型',
                    move_country VARCHAR(255) comment '电影国家',
                    move_language VARCHAR(255) comment '电影语言',
                    move_ReleaseTime VARCHAR(255) comment '电影上映时间',
                    move_location VARCHAR(255) comment '电影片场',
                    ShortFilm_num VARCHAR(255) comment '短片个数',
                    move_Star_Rating VARCHAR(255) comment '电影星级',
                    move_information VARCHAR(1000) comment '电影信息介绍',
                    move_ShortFilm text	comment '电影短评',
                    Img_List VARCHAR(255) comment '图片列表',
                    Trailer_Link VARCHAR(255) comment '预告片链接'
                );
        '''
        try:
            # 运行SQL语句
            self.cursor.execute(sql)
        except:
            pass
        else:
            # 提交当前事务
            self.conn.commit()

    # 读取爬取的页数
    @staticmethod
    def get_spiderPage():
        with open('./spiderPage.txt', 'r') as r_f:
            return r_f.readlines()[-1].strip()

    # 写入爬取的页数
    @staticmethod
    def set_spiderPage(newPage):
        with open('./spiderPage.txt', 'a') as a_f:
            a_f.write(str(newPage) + '\n')

    # 爬取数据主函数
    def spiderMain(self):
        # 调用函数获取页数
        page = self.get_spiderPage()
        print('----正在爬取第{}页数据----'.format(int(page) + 1))
        # 创建动态参数
        params = {
            'start': int(page) * 20
        }
        # 请求电影列表页面,获取json数据
        respJson = requests.get(self.spiderUrl, headers=self.headers, params=params).json()
        # 获取json数据中items字段数据
        respJson = respJson['items']
        # 遍历获取电影详情页面ID
        for index, move_Data in enumerate(respJson):
            print('正在爬取{}个电影数据......   '.format(index + 1), end='')
            # 创建电影数据空列表 ---- 进行组合数据
            movie_resultData = []
            # 获取电影详情链接
            move_DatailsLink = 'https://movie.douban.com/subject/{}/'.format(move_Data['id'])
            # 请求电影详情页面,获取HTML数据
            respDatailHTML = requests.get(move_DatailsLink, headers=self.headers)
            # 解析HTML数据
            respDatailHTMLXpath = etree.HTML(respDatailHTML.text)
            # 电影导演（move_directors）
            move_directors = respDatailHTMLXpath.xpath('//*[@id="info"]/span/span[@class="attrs"]/a/text()')
            movie_resultData.append(move_directors[0])
            # 电影评分（move_score）
            move_score = respDatailHTMLXpath.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()')
            movie_resultData.append(move_score[0])
            # 电影名字（move_name）
            move_name = move_Data['title']
            movie_resultData.append(move_name)
            # 如果该电影存在则跳过这次循环
            if self.select_movie_name(move_name) == 1:
                print('《{}》 数据已存在'.format(move_name))
                continue
            # 电影演员（move_actor）
            move_actor_list = respDatailHTMLXpath.xpath('//*[@id="info"]/span[3]/span[2]/a/text()')
            move_actor = ','.join(move_actor_list)
            movie_resultData.append(move_actor)
            # 电影封面（move_cover）
            move_cover = respDatailHTMLXpath.xpath('//*[@id="mainpic"]/a/img/@src')
            movie_resultData.append(move_cover[0])
            # 电影详情链接（move_DatailsLink）
            movie_resultData.append(move_DatailsLink)
            # 电影年份（move_year）
            move_year_text = respDatailHTMLXpath.xpath('//*[@id="content"]/h1/span[2]/text()')
            move_year = re.search('\d+', move_year_text[0]).group()
            movie_resultData.append(move_year)
            # 电影类型（move_types）
            move_types_list = respDatailHTMLXpath.xpath('//*[@id="info"]/span[@property="v:genre"]/text()')
            move_types = ','.join(move_types_list)
            movie_resultData.append(move_types)
            # 电影国家（move_country）
            info_text = respDatailHTMLXpath.xpath('//*[@id="info"]/text()')
            info_text_list = []
            for i in info_text:
                if i.strip() and i.strip() != '/':
                    info_text_list.append(i.strip())
            move_country = info_text_list[0]
            movie_resultData.append(move_country)
            # 电影语言（move_language）
            move_language = info_text_list[1].replace(" / ", ",")
            movie_resultData.append(move_language)
            # 电影上映时间（move_ReleaseTime）
            move_ReleaseTime = respDatailHTMLXpath.xpath('//*[@id="info"]/span[@property="v:initialReleaseDate"][1]/text()')
            if self.is_chinese(move_ReleaseTime[0][0:10]):
                # 含有中文就截取[0:7]
                movie_resultData.append(move_ReleaseTime[0][0:7])
            else:
                # 不含有中文就截取[0:10]
                movie_resultData.append(move_ReleaseTime[0][0:10])
            # 电影片场（move_location）
            move_location_text = respDatailHTMLXpath.xpath('//*[@id="info"]/span[@property="v:runtime"]/text()')
            move_location = re.search('\d+', move_location_text[0]).group()
            movie_resultData.append(move_location)
            # 短片个数（ShortFilm_num）
            ShortFilm_text = respDatailHTMLXpath.xpath('//*[@id="comments-section"]/div[1]/h2/span/a/text()')
            ShortFilm_num = re.search('\d+', ShortFilm_text[0]).group()
            movie_resultData.append(ShortFilm_num)
            # 电影星级（move_Star_Rating）
            move_Star_Rating_list = respDatailHTMLXpath.xpath('//*[@class="ratings-on-weight"]/div/span[2]/text()')
            move_Star_Rating = ','.join(move_Star_Rating_list)
            movie_resultData.append(move_Star_Rating)
            # 电影信息介绍（move_information）
            move_information_text = respDatailHTMLXpath.xpath('//*[@property="v:summary"]/text()')
            move_information = move_information_text[0].strip().replace('"', "“").replace("'", "’")
            movie_resultData.append(move_information)
            # 电影短评（短评用户，短评评分，评论时间，评论内容）move_ShortFilm(ShortFilm_user,ShortFilm_cover,ShortFilm_time,ShortFilm_content)
            move_ShortFilm = []
            comment_item = respDatailHTMLXpath.xpath('//*[@id="hot-comments"]/div')
            for item in comment_item:
                ShortFilm_user = item.xpath('.//h3/span[@class="comment-info"]/a/text()')[0].replace('"', "“").replace("'", "’")
                try:
                    ShortFilm_cover = re.search('\d+', item.xpath('.//h3/span[@class="comment-info"]/span[2]/@class')[0]).group()
                except:
                    ShortFilm_cover = '0'
                else:
                    ShortFilm_time = item.xpath('.//h3/span[@class="comment-info"]/span[@class="comment-time "]/@title')[0]
                    ShortFilm_content = item.xpath('.//p/span[@class="short"]/text()')[0].replace("\n", "").replace("\r", "").replace('"', "“").replace("'", "’")
                    move_ShortFilm.append({
                        "ShortFilm_user": ShortFilm_user,
                        "ShortFilm_cover": ShortFilm_cover,
                        "ShortFilm_time": ShortFilm_time,
                        "ShortFilm_content": ShortFilm_content
                    })
            movie_resultData.append(move_ShortFilm)
            # movie_resultData.append(json.dumps(move_ShortFilm))
            # 图片列表（Img_List）
            Img_List = respDatailHTMLXpath.xpath('//*[@class="related-pic-bd  wide_videos"]/li/a/img/@src')
            Img_List = ','.join(Img_List)
            movie_resultData.append(Img_List)
            # 预告片链接（Trailer_Link）
            try:
                Trailer_src = respDatailHTMLXpath.xpath('//*[@class="label-trailer"]/a[@class="related-pic-video"]/@href')[0]
            except:
                Trailer_Link = ''
            else:
                # 请求预告片页面,获取HTML数据
                Trailer_src_HTML = requests.get(Trailer_src, headers=self.headers)
                # 解析HTML数据
                Trailer_src_HTMLXpath = etree.HTML(Trailer_src_HTML.text)
                Trailer_Link = Trailer_src_HTMLXpath.xpath('//*[@id="movie_player"]//source/@src')[0]
            movie_resultData.append(Trailer_Link)
            # 对数据进行存储
            self.save_to_sql(movie_resultData)
            print('《{}》 数据保存成功!'.format(move_name))

        self.set_spiderPage(int(page) + 1)
        self.spiderMain()

    # 保存数据至数据库
    def save_to_sql(self, row_movie_Data):
        # SQL语句创建表
        sql = '''
            INSERT INTO movie (
            move_directors,
            move_score,
            move_name,
            move_actor,
            move_cover,
            `move_DatailsLink`,
            move_year,
            move_types,
            move_country,
            move_language,
            `move_ReleaseTime`,
            move_location,
            `ShortFilm_num`,
            `move_Star_Rating`,
            move_information,
            `move_ShortFilm`,
            `Img_List`,
            `Trailer_Link` 
        )VALUES(
            "{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}"
        );
        '''.format(
            row_movie_Data[0],
            row_movie_Data[1],
            row_movie_Data[2],
            row_movie_Data[3],
            row_movie_Data[4],
            row_movie_Data[5],
            row_movie_Data[6],
            row_movie_Data[7],
            row_movie_Data[8],
            row_movie_Data[9],
            row_movie_Data[10],
            row_movie_Data[11],
            row_movie_Data[12],
            row_movie_Data[13],
            row_movie_Data[14],
            row_movie_Data[15],
            row_movie_Data[16],
            row_movie_Data[17]
        )
        # 运行SQL语句
        try:
            self.cursor.execute(sql)
        except:
            print(sql)
        else:
            # 提交当前事务
            self.conn.commit()

    # 查询数据库的电影数据
    def select_movie_name(self, move_name):
        select_sql = "SELECT COUNT(*) FROM movie WHERE move_name = '{}';".format(move_name)
        # 运行SQL语句
        self.cursor.execute(select_sql)
        select_result = self.cursor.fetchone()[0]
        return select_result

    @staticmethod
    # 判断字符串是否含有中文
    def is_chinese(move_ReleaseTime):
        for ch in move_ReleaseTime:
            if u'\u4e00' <= ch <= u'\u9fff':
                return True
        return False


if __name__ == "__main__":
    spiderObj = spider()  # 实例化类
    spiderObj.init()  # 调用初始化函数
    try:
        spiderObj.spiderMain()  # 调用爬虫主函数
    except IndexError:
        print("Cookie 失效")
