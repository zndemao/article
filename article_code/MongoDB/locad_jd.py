import requests
from bs4 import BeautifulSoup
import re
import pymongo
from utils import download_image


# 解析出城市中的信息
def parse_city(city_name):
    headers = {
        'User-Agent': 'Mozilla/4.0(compatible;MSIE 5.5;Windows NT)', }
    url = 'https://piao.qunar.com/ticket/list.htm?keyword=' + city_name + '&region=&from=mpl_search_suggest'
    html = requests.get(url, headers=headers)
    html = html.text
    soup = BeautifulSoup(html, 'lxml')
    jingdian = soup.find_all('div', {'class': 'result_list', 'id': 'search-list'})[0].find_all('div',
                                                                                               {'class': 'sight_item'})
    for c in jingdian:
        # 景点图片
        jd_image_info = c.find_all('img', {'class': 'img_opacity load'})
        image_text = jd_image_info[0]
        # print(type(image_text))
        # x = print(text.parent.find_all(text=re.compile('data-original')))
        image_str = str(image_text)
        jd_image_url = re.search(r' data-original="(https://imgs.qunarzz.com\S*.\S{3})" ', image_str).group(1)
        # group = search.group()r
        # print(jd_image_url)

        # find_all = text.find_all('img', {'data-original'})

        # 景点名
        jd_name = c.find_all('a', {'data-click-type': 'l_title', 'class': 'name'})[0].text
        # print(jd_name)
        # 景点级别，有的景区无级别，所以要设置一个异常
        try:
            jd_jb = c.find_all('span', {'class': 'level'})[0].text
        except:
            jd_jb = '普通景区'
        # text得到的是  地址：北京市东城区景山前街4号  这种格式，所以以空格拆分，取后面那个
        jd_address = c.find_all('p', {'class': {'address', 'color999'}})[0].text.split()[-1]
        # 景点介绍
        jd_jieshao = c.find_all('div', {'class': {'intro', 'color999'}})[0].text
        # 景点价格，有的是免费，并无价格这一参数，所以设置一个异常
        try:
            jd_price = c.find_all('span', {'class': 'sight_item_price'})[0].find_all('em')[0].text
        except:
            jd_price = 0
        # 有的是免费，并销量这一参数，所以设置一个异常
        try:
            jd_xiaoliang = c.find_all('span', {'class': 'hot_num'})[0].text
            # 景点销量
            jd_xiaoliang = int(jd_xiaoliang)
        except:
            jd_xiaoliang = 0
        # print('{0}  {1}  {2}  {3}  {4}'.format(jd_name, jd_jb, jd_jieshao, jd_price, jd_xiaoliang))

        file_extension = re.search(r'https://imgs.qunarzz.com\S*(.\S{3})', jd_image_url).group(1)
        image_path = jd_name + file_extension
        # print(image_path)
        print(city_name, jd_name, jd_jb, jd_jieshao, jd_price, jd_xiaoliang, jd_image_url, image_path)
        mysql(city_name, jd_name, jd_jb, jd_jieshao, jd_price, jd_xiaoliang, jd_image_url, image_path)


# 定义一个类，将连接MySQL的操作写入其中,使用的mongodb数据库

class down_mongdb:

    def __init__(self, city_name, scenic_name, scenic_level, scenic_introduction, scenic_price, scenic_sales,
                 scenic_image, scenic_image_path):
        '''
        city_name, Scenic_name, Scenic_level, Scenic_Introduction, Scenic_price, Scenic_sales,scenic_image,scenic_image_path
        城市       景点名        景点等级        介绍                  价钱          销量              图片url
        '''
        self.city_name = city_name
        self.scenic_name = scenic_name
        self.scenic_level = scenic_level
        self.scenic_introduction = scenic_introduction
        self.scenic_price = scenic_price
        self.scenic_sales = scenic_sales
        self.scenic_image = scenic_image
        self.scenic_image_path = scenic_image_path

        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["db_locad_tourism"]
        self.mycol = mydb["locad_tourism_data"]

    # 保存数据到MySQL中
    def save_mysql(self):
        mydict = {"city": self.city_name, "scenic": self.scenic_name, "level": self.scenic_level,
                  "introduction": self.scenic_introduction,
                  "price": self.scenic_price,
                  "sales": self.scenic_sales,
                  "image": self.scenic_image,
                  "image_path": self.scenic_image_path}
        try:
            self.mycol.insert(mydict)
            print('数据插入成功')
        except:
            print('数据插入错误')
    def find_write(self):
        find = self.mycol.find({'scenic':self.scenic_name})
        print(find)
        temp={}
        for x in find:
            temp=x
            print()
        return len(temp)


def mysql(city_name, jd_name, jd_jb, jd_jieshao, jd_price, jd_xiaoliang, scenic_image, scenic_image_path):
    down = down_mongdb(city_name, jd_name, jd_jb, jd_jieshao, jd_price, jd_xiaoliang, scenic_image, scenic_image_path)
    # 新建类，将数据保存在MySQL中
    # 保存到数据库
    if down.find_write() > 0:
        print('已经存在')
        return
    download_image.download_image(scenic_image, jd_name, city_name)
    # 下载图片
    down.save_mysql()


if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/4.0(compatible;MSIE 5.5;Windows NT)', }
    start_url = 'https://piao.qunar.com/ticket/list.htm?keyword=' + '开封' + '&region=&from=mpl_search_suggest'
    # parse_city(start_url)
    parse_city('开封')
