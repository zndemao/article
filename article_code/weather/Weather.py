#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   Weather.py    
@Contact :   cubecats@icloud.com
@License :   (C)Copyright 2017-2018, DAMN-CAT

@Modify Time        @Author     @Version    @Desciption
------------        --------    --------    -----------
2020/3/7 下午7:43    damn cat    1.0         None
'''

# import lib
import requests
from bs4 import BeautifulSoup
import re
import pymongo
import time
import urllib.request


# from utils import download_image


# 解析出城市中的信息
def parse_city():
    # url = "https://www.baidu.com/"
    #
    # urlopen = urllib.request.urlopen('https://www.baidu.com')
    # print(urlopen.read())
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'
    }

    url = r"http://m.ip138.com/ip.asp?="
    # ip_ = requests.get(url='http://ip.42.pl/raw', params={'wd': 'python'}).text
    r = requests.get('https://www.amap.com/', headers=headers)
    # a = r.status_code
    print(r.text)
    text = r.text
    print(type(text))
    print(text[-100:])
    find = text.find(text[-100:])
    print(find)
    # print(a)
    # print(r.text)
    # c = r.text
    # soup = BeautifulSoup(c, 'lxml')
    # jd_name = soup.find_all('p')
    # print(jd_name)
    # print('爬取失败')

    # url = 'https://www.baidu.com/'
    #
    # ip_ = requests.get(url='http://ip.42.pl/raw', params={'wd': 'python'}).text
    # data = {'ip': ip_}

    # response = requests.get(url, headers=headers)
    # response = (response.text)
    # text = response
    # print(type(text))
    # print(text)
    # re.search(r'document.cookie="NOJS=;expires=Sat,', response).group(1)

    # address1 = response['text']['location']  # 获得ip地址
    # print(address1)
    # headers = {
    #     'User-Agent': 'Mozilla/4.0(compatible;MSIE 5.5;Windows NT)', }
    # # url = 'http://data.people.com.cn/rmrb/s?type=2&qs=%7B%22cds%22%3A%5B%7B%22fld%22%3A%22dataTime%22%2C%22cdr%22%3A%22AND%22%2C%22hlt%22%3A%22false%22%2C%22vlr%22%3A%22OR%22%2C%22qtp%22%3A%22DEF%22%2C%22val%22%3A%222020-' + month + '-' + day + '%22%7D%5D%2C%22obs%22%3A%5B%7B%22fld%22%3A%22dataTime%22%2C%22drt%22%3A%22DESC%22%7D%5D%7D'
    # # url = 'http://data.people.com.cn/rmrb/s?type=2&qs=%7B%22cds%22%3A%5B%7B%22fld%22%3A%22dataTime%22%2C%22cdr%22%3A%22AND%22%2C%22hlt%22%3A%22false%22%2C%22vlr%22%3A%22OR%22%2C%22qtp%22%3A%22DEF%22%2C%22val%22%3A%222020-01-23%22%7D%5D%2C%22obs%22%3A%5B%7B%22fld%22%3A%22dataTime%22%2C%22drt%22%3A%22DESC%22%7D%5D%7D'
    # url = "https://www.baidu.com/s?tn=baidutop10&rsv_idx=2&wd=驻马店天气预报"
    # print(url)
    # html = requests.get(url, headers=headers)
    # html = html.text
    # print(html)
    # soup = BeautifulSoup(html, 'lxml')
    # jingdian = soup.find_all('a', {'class': 'open_detail_link'})
    # # print(jingdian)
    # count = 0

    # return count
    # print(c)
    # for c in jingdian:
    #     # 景点图片
    #     jd_image_info = c.find_all('img', {'class': 'img_opacity load'})
    #     image_text = jd_image_info[0]
    #     # print(type(image_text))
    #     # x = print(text.parent.find_all(text=re.compile('data-original')))
    #     image_str = str(image_text)
    #     jd_image_url = re.search(r' data-original="(https://imgs.qunarzz.com\S*.\S{3})" ', image_str).group(1)
    #     # group = search.group()r
    #     # print(jd_image_url)
    #
    #     # find_all = text.find_all('img', {'data-original'})
    #
    #     # 景点名
    #     jd_name = c.find_all('a', {'data-click-type': 'l_title', 'class': 'name'})[0].text
    #     # print(jd_name)
    #     # 景点级别，有的景区无级别，所以要设置一个异常
    #     try:
    #         jd_jb = c.find_all('span', {'class': 'level'})[0].text
    #     except:
    #         jd_jb = '普通景区'
    #     # text得到的是  地址：北京市东城区景山前街4号  这种格式，所以以空格拆分，取后面那个
    #     jd_address = c.find_all('p', {'class': {'address', 'color999'}})[0].text.split()[-1]
    #     # 景点介绍
    #     jd_jieshao = c.find_all('div', {'class': {'intro', 'color999'}})[0].text
    #     # 景点价格，有的是免费，并无价格这一参数，所以设置一个异常
    #     try:
    #         jd_price = c.find_all('span', {'class': 'sight_item_price'})[0].find_all('em')[0].text
    #     except:
    #         jd_price = 0
    #     # 有的是免费，并销量这一参数，所以设置一个异常
    #     try:
    #         jd_xiaoliang = c.find_all('span', {'class': 'hot_num'})[0].text
    #         # 景点销量
    #         jd_xiaoliang = int(jd_xiaoliang)
    #     except:
    #         jd_xiaoliang = 0
    #     # print('{0}  {1}  {2}  {3}  {4}'.format(jd_name, jd_jb, jd_jieshao, jd_price, jd_xiaoliang))
    #
    #     file_extension = re.search(r'https://imgs.qunarzz.com\S*(.\S{3})', jd_image_url).group(1)
    #     image_path = jd_name + file_extension
    #     # print(image_path)
    #     print(city_name, jd_name, jd_jb, jd_jieshao, jd_price, jd_xiaoliang, jd_image_url, image_path)
    #
    #


def parse_city2(month, day):
    url2 = 'http://data.people.com.cn/rmrb/s?qs=%7B%22cds%22%3A%5B%7B%22fld%22%3A%22dataTime%22%2C%22cdr%22%3A%22AND%22%2C%22hlt%22%3A%22false%22%2C%22vlr%22%3A%22OR%22%2C%22qtp%22%3A%22DEF%22%2C%22val%22%3A%222020-01-23%22%7D%5D%2C%22obs%22%3A%5B%7B%22fld%22%3A%22dataTime%22%2C%22drt%22%3A%22DESC%22%7D%5D%7D&tr=A&ss=1&pageNo=1&pageSize=20'

    html = requests.get(url2, headers=headers)
    html = html.text
    # print(html)
    soup = BeautifulSoup(html, 'lxml')
    jingdian = soup.find_all('div', {'class': 'pageNav_wrap'})
    '<a data-index="5">5</a>'
    print(jingdian)
    count = 0
    for c in jingdian:
        print(c)


def url_add(month, day, page):
    return 'http://data.people.com.cn/rmrb/s?qs=%7B%22cds%22%3A%5B%7B%22fld%22%3A%22dataTime%22%2C%22cdr%22%3A%22AND%22%2C%22hlt%22%3A%22false%22%2C%22vlr%22%3A%22OR%22%2C%22qtp%22%3A%22DEF%22%2C%22val%22%3A%222020-' + month + '-' + day + '%22%7D%5D%2C%22obs%22%3A%5B%7B%22fld%22%3A%22dataTime%22%2C%22drt%22%3A%22DESC%22%7D%5D%7D&tr=A&ss=1&pageNo=' + page + '&pageSize=20'


if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/4.0(compatible;MSIE 5.5;Windows NT)', }
    # start_url = 'https://piao.qunar.com/ticket/list.htm?keyword=' + '开封' + '&region=&from=mpl_search_suggest'
    parse_city()
    # parse_city(start_url)
    # month = '02'
    # day = '23'
    # page = '1'
    # # parse_city2('01', '23')
    # 'http://data.people.com.cn/rmrb/s?type=2&qs=%7B%22cds%22%3A%5B%7B%22fld%22%3A%22dataTime%22%2C%22cdr%22%3A%22AND%22%2C%22hlt%22%3A%22false%22%2C%22vlr%22%3A%22OR%22%2C%22qtp%22%3A%22DEF%22%2C%22val%22%3A%222020-02-23%22%7D%5D%2C%22obs%22%3A%5B%7B%22fld%22%3A%22dataTime%22%2C%22drt%22%3A%22DESC%22%7D%5D%7D'
    # 'http://data.people.com.cn/rmrb/s?type=2&qs=%7B%22cds%22%3A%5B%7B%22fld%22%3A%22dataTime%22%2C%22cdr%22%3A%22AND%22%2C%22hlt%22%3A%22false%22%2C%22vlr%22%3A%22OR%22%2C%22qtp%22%3A%22DEF%22%2C%22val%22%3A%222020-01-23%22%7D%5D%2C%22obs%22%3A%5B%7B%22fld%22%3A%22dataTime%22%2C%22drt%22%3A%22DESC%22%7D%5D%7D'
    # 'http://data.people.com.cn/rmrb/s?qs=%7B%22cds%22%3A%5B%7B%22fld%22%3A%22dataTime%22%2C%22cdr%22%3A%22AND%22%2C%22hlt%22%3A%22false%22%2C%22vlr%22%3A%22OR%22%2C%22qtp%22%3A%22DEF%22%2C%22val%22%3A%222020-01-23%22%7D%5D%2C%22obs%22%3A%5B%7B%22fld%22%3A%22dataTime%22%2C%22drt%22%3A%22DESC%22%7D%5D%7D&tr=A&ss=1&pageNo=2&pageSize=20'
    # 'http://data.people.com.cn/rmrb/s?qs=%7B%22cds%22%3A%5B%7B%22fld%22%3A%22dataTime%22%2C%22cdr%22%3A%22AND%22%2C%22hlt%22%3A%22false%22%2C%22vlr%22%3A%22OR%22%2C%22qtp%22%3A%22DEF%22%2C%22val%22%3A%222020-01-23%22%7D%5D%2C%22obs%22%3A%5B%7B%22fld%22%3A%22dataTime%22%2C%22drt%22%3A%22DESC%22%7D%5D%7D&tr=A&ss=1&pageNo=1&pageSize=20'
    # 'http://data.people.com.cn/rmrb/s?qs=%7B%22cds%22%3A%5B%7B%22fld%22%3A%22dataTime%22%2C%22cdr%22%3A%22AND%22%2C%22hlt%22%3A%22false%22%2C%22vlr%22%3A%22OR%22%2C%22qtp%22%3A%22DEF%22%2C%22val%22%3A%222020-' + month + '-' + day + '%22%7D%5D%2C%22obs%22%3A%5B%7B%22fld%22%3A%22dataTime%22%2C%22drt%22%3A%22DESC%22%7D%5D%7D&tr=A&ss=1&pageNo=' + page + '&pageSize=20'
    # 'http://data.people.com.cn/rmrb/s?qs=%7B%22cds%22%3A%5B%7B%22fld%22%3A%22dataTime%22%2C%22cdr%22%3A%22AND%22%2C%22hlt%22%3A%22false%22%2C%22vlr%22%3A%22OR%22%2C%22qtp%22%3A%22DEF%22%2C%22val%22%3A%222020-02-23%22%7D%5D%2C%22obs%22%3A%5B%7B%22fld%22%3A%22dataTime%22%2C%22drt%22%3A%22DESC%22%7D%5D%7D&tr=A&ss=1&pageNo=2&pageSize=20'
    # count = 0
    # for i in range(21, 32):
    #     for j in range(1, 15):
    #         url = url_add('01', str(i), str(j))
    #         page_cont = parse_city('', '', url=url)
    #         time.sleep(3)
    #         count = count + page_cont
    #     i_count = '01月' + str(i) + '日：'
    #     print(i_count, count)
    #     count = 0
    # # for i in range(1, 29):
    # #     print(i)
