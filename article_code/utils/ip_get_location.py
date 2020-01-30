import geoip2.database
import requests
import os


# # r = requests.get(url='http://ip.42.pl/raw')  # 最基本的GET请求
# # print(r.status_code)  # 获取返回状态
#
# # 带参数的GET请求，http://dict.baidu.com/s?wd=python
# r = requests.get(url='http://ip.42.pl/raw', params={'wd': 'python'})
# # print(r.url)
# reader = geoip2.database.Reader('./GeoLite2-City.mmdb')
# ip = r.text
# response = reader.city(ip)  # 有多种语言，我们这里主要输出英文和中文print("你查询的IP的地理位置是:")
#
# print("地区：{}({})".format(response.continent.names["es"],
#                          response.continent.names["zh-CN"]))
#
# print("国家：{}({}) ，简称:{}".format(response.country.name,
#                                 response.country.names["zh-CN"],
#                                 response.country.iso_code))
#
# print("洲／省：{}({})".format(response.subdivisions.most_specific.name,
#                           response.subdivisions.most_specific.names["zh-CN"]))
#
# print("城市：{}({})".format(response.city.name,
#                          response.city.names["zh-CN"]))
#
# print("经度：{}，纬度{}".format(response.location.longitude,
#                           response.location.latitude))
#
# print("时区：{}".format(response.location.time_zone))
#
# print("邮编:{}".format(response.postal.code))


def get_location():
    path = os.path.abspath(os.path.join(os.getcwd(), '..'))
    reader = geoip2.database.Reader(path + '/utils/GeoLite2-City.mmdb')
    r = requests.get(url='http://ip.42.pl/raw', params={'wd': 'python'})
    ip = r.text
    ip = '182.127.196.182'
    response = reader.city(ip)  # 有多种语言，我们这里主要输出英文和中文print("你查询的IP的地理位置是:")

    state = response.subdivisions.most_specific.names["zh-CN"]
    city = response.city.names["zh-CN"]
    return city


#
# import socket
#
# def get_host_ip():
#     """
#     查询本机ip地址
#     :return:
#     """
#     try:
#         s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#         s.connect(('8.8.8.8',80))
#         ip=s.getsockname()[0]
#     finally:
#         s.close()
#
#     return ip
#
# import urllib3
# # my_ip = urllib3.urlopen('http://ip.42.pl/raw').read()
# # print('ip.42.pl', my_ip)
# http = urllib3.PoolManager()
# # 通过request()方法创建一个请求，该方法返回一个HTTPResponse对象：
# r = http.request('POST', 'http://ip.42.pl/raw')
# print(r.data)
#
# import requests
#
# r = requests.get(url='http://ip.42.pl/raw')  # 最基本的GET请求
# # print(r.status_code)  # 获取返回状态
#
# # 带参数的GET请求，http://dict.baidu.com/s?wd=python
# r = requests.get(url='http://ip.42.pl/raw', params={'wd': 'python'})
# # print(r.url)
# print(r.text)
#
# # from json import load
# #
# # my_ip = urllib3.load(urllib3.urlopen('http://jsonip.com'))['ip']
# # print('jsonip.com', my_ip)

if __name__ == '__main__':
    print(get_location())
