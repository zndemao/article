import requests
from bs4 import BeautifulSoup
import re
import pymongo


# 解析出每个城市及其该城市对应的url
def parse_city(url):
    html = requests.get(url, headers=headers)
    html = html.text
    soup = BeautifulSoup(html, 'lxml')
    jingdian = soup.find_all('div', {'class': 'result_list', 'id': 'search-list'})[0].find_all('div',
                                                                                               {'class': 'sight_item'})
    for c in jingdian:
        # 景点图片data-original target="_blank"
        # jd_image = c.find_all('a', {'data-click-type': 'l_pic', 'img': 'data-original'})[0].text
        jd_image = c.find_all('img', {'class': 'img_opacity load'})
        text = jd_image[0]
        print(type(text))
        # x = print(text.parent.find_all(text=re.compile('data-original')))
        print(type(str(text)))
        s = str(text)
        print(s)
        are = r'data-original='

        search = re.search('data-original=', s).span()
        print(search)
        # find_all = text.find_all('img', {'data-original'})

        # 景点名
        jd_name = c.find_all('a', {'data-click-type': 'l_title', 'class': 'name'})[0].text
        print(jd_name)
        # 景点级别，有的景区无级别，所以要设置一个异常
        try:
            jd_jb = c.find_all('span', {'class': 'level'})[0].text
        except:
            jd_jb = '普通景区'
        # text得到的是  地址：北京市东城区景山前街4号  这种格式，所以以空格拆分，取后面那个
        jd_address = c.find_all('p', {'class': {'address', 'color999'}})[0].text.split()[-1]
        # 景点介绍
        jd_jieshao = c.find_all('div', {'class': {'intro', 'color999'}})
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
        print('{0}  {1}  {2}  {3}  {4}'.format(jd_name, jd_jb, jd_jieshao, jd_price, jd_xiaoliang))
        # mysql(city_name, jd_name, jd_jb, jd_jieshao, jd_price, jd_xiaoliang)


# 解析出每个城市的url的下一页
def city_page(city_name, city_url):
    html = requests.get(city_url, headers=headers)
    html = html.text
    soup = BeautifulSoup(html, 'lxml')
    page = soup.find_all('div', {'class': 'pager'})[0].find_all('a')
    # 得到a标签中的href
    page_url = page[0]['href']
    # 得到下一页的url，这个url由我们来指定，只需把页数前面的字符串匹配出来即可
    page_select_url = re.findall('(.*page=)', page_url)[0]
    # 将完整的页数的url拼接起来
    page_select_url = 'http://piao.qunar.com' + page_select_url
    # 这里选-2是有深意的，因为在选择每一页的地方倒一是下一页，而倒二则是尾页数
    page_num = int(page[-2].text)
    print('有%s页的数据' % page_num)

    count = 0
    for i in range(1, page_num + 1):
        # 遍历得到某个城市中所有页数
        print('第%d页信息' % i)
        parse_page_url = page_select_url + str(i)
        print('网页地址：', parse_page_url)
        # 将每一页的url都传递到parse_page中进行解析
        parse_page(city_name, parse_page_url)

        count += 1
        if (count == 10):
            print(count)
            break


# 解析每个城市每一页的信息
def parse_page(city_name, parse_page_url):
    html = requests.get(parse_page_url, headers=headers)
    html = html.text
    soup = BeautifulSoup(html, 'lxml')
    jingdian = soup.find_all('div', {'class': 'result_list', 'id': 'search-list'})[0].find_all('div',
                                                                                               {'class': 'sight_item'})
    for c in jingdian:
        # 景点名
        jd_name = c.find_all('a', {'data-click-type': 'l_title', 'class': 'name'})[0].text
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
        print('{0}  {1}  {2}  {3}  {4}'.format(jd_name, jd_jb, jd_jieshao, jd_price, jd_xiaoliang))
        # mysql(city_name, jd_name, jd_jb, jd_jieshao, jd_price, jd_xiaoliang)


# 定义一个类，将连接MySQL的操作写入其中,使用的mongodb数据库

class down_mongdb:

    def __init__(self, city_name, scenic_name, scenic_level, scenic_introduction, scenic_price, scenic_sales):
        '''
        city_name, Scenic_name, Scenic_level, Scenic_Introduction, Scenic_price, Scenic_sales
        城市       景点名        景点等级        介绍                  价钱          销量
        '''
        self.city_name = city_name
        self.scenic_name = scenic_name
        self.scenic_level = scenic_level
        self.scenic_introduction = scenic_introduction
        self.scenic_price = scenic_price
        self.scenic_sales = scenic_sales

        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["db_tourism"]
        self.mycol = mydb["tourism_data"]

    # 保存数据到MySQL中
    def save_mysql(self):
        mydict = {"city": self.city_name, "scenic": self.scenic_name, "level": self.scenic_level,
                  "introduction": self.scenic_introduction,
                  "price": self.scenic_price,
                  "sales": self.scenic_sales}
        try:
            self.mycol.insert(mydict)
            print('数据插入成功')
        except:
            print('数据插入错误')


# def mysql(city_name, jd_name, jd_jb, jd_jieshao, jd_price, jd_xiaoliang):
#     # 新建类，将数据保存在MySQL中
#     down = down_mongdb(city_name, jd_name, jd_jb, jd_jieshao, jd_price, jd_xiaoliang)
#     down.save_mysql()


if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/4.0(compatible;MSIE 5.5;Windows NT)', }
    start_url = 'https://piao.qunar.com/ticket/list.htm?keyword=' + '开封' + '&region=&from=mpl_search_suggest'
    parse_city(start_url)
