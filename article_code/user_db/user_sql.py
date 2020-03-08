#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   user_sql.py    
@Contact :   cubecats@icloud.com
@License :   (C)Copyright 2017-2018, DAMN-CAT

@Modify Time        @Author     @Version    @Desciption
------------        --------    --------    -----------
2020/3/5 下午8:15    damn cat    1.0         None
'''

# import lib
# 用户登陆 用户名 密码 邮箱 访问记录 等


# 注册 增 检查是否注册过，没有就注册
# 登陆 查 以用户名为查询数据库
# 修改 该  检查是否注册过，数据匹配就修改
import pymongo
from bson import ObjectId


class User_db:
    # 连接到数据库
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    # 数据库名称
    mydb = myclient["db_user"]
    # 表名称
    mycol = mydb["user_data"]

    # mydict = {"name": "cat2", "age": 17}
    # mydict = {"group": "admin-test", "username": "admin_test", "user_phone": "18500000000", "password": "admin",
    #           "mailbox": "cubecats@icloud.com",
    #           "recording": '0'}
    #
    # x = mycol.insert_one(mydict)
    # print(x)
    # print(x)

    # x = mycol.find()
    # print(type(x))

    # for x in mycol.find():
    #     print(x)

    # 增 用户注册
    def add_user(self, user_info):
        '''
        用户和管理员的注册
        :param user_info: 字典
        :return: _id 字段
        '''
        x = User_db.mycol.insert_one(user_info)
        print(x)
        return x

    def find_ID(self):
        '''
        根据id查询数据,测试。
        :return:
        '''
        myquery = {'_id': ObjectId('5e33a1982215f4a362a51e9d')}
        name = {"username": 1, "user_phone": 1}
        # print(type(name))
        find = User_db.mycol.find(myquery, name)
        for x in find:
            print(x)
        return find

    # 以用户用查询 ,注册
    def query_registered(self, user_name):
        '''
        以用户名查询
        :param user_name:用户名
        :return:字典{'_id': ObjectId('*'), 'username': '*', 'user_phone': '*'}
        '''

        myquery = {"username": user_name}
        name = {"username": 1, "user_phone": 1}
        # print(type(name))
        find = User_db.mycol.find(myquery, name)
        # print(len(find))
        query = {}
        # print(find)
        for x in find:
            # print(x)
            # print(type(x))
            query = x
        # print(query)
        # print(type(query))
        return query

    def query_all(self):
        '''
        查询全部的数据
        :return:pymongo.cursor.Cursor
        '''
        find = User_db.mycol.find()
        # print(find)
        for x in find:
            print(x)
        # print(type(find))

    # 查
    def query_login(self, phone):
        '''
        根据手机号查询用户信息
        :param phone: 手机号，
        :return: 查询到的结果。字典
        '''
        login_phone = {"user_phone": phone}
        field = {"group": 1,"username": 1, "user_phone": 1, "password": 1}

        find = User_db.mycol.find(login_phone, field)
        query = {}
        for x in find:
            # print(x)
            query = x
        return query

    # 改 修改密码
    def update_pass(self, phone, new_password, mailbox):
        '''
        修改密码
        :param phone: 用户手机号
        :param new_password: 新的密码
        :param mailbox: 用户注册时使用的邮箱
        :return: True 修改成功，
        '''
        query = {"user_phone": phone, "mailbox": mailbox}
        find = User_db.mycol.find(query)
        old_info = {}
        for x in find:
            print(x)
            old_info = x

        # 判断与旧密码相同否
        password = old_info.get("password")
        # print(password)
        if password == new_password:
            return True

        new_pass = {"$set": {"password": new_password}}
        update = User_db.mycol.update_one(old_info, new_pass)
        # print(type(update))
        print(update.modified_count)
        if update.modified_count >= 1:
            return True
        else:
            return False

    def find_group(self, group_name):
        '''
        根据'组'查询用户信息,
        :param group_name: 组名称( admin , user )
        :return: 'pymongo.cursor.Cursor'
        '''
        login_phone = {"group": group_name}
        # field = {"username": 1, "user_phone": 1, "password": 1}

        find = User_db.mycol.find(login_phone)
        # print(type(find))
        # for x in find:
        #     print(x)
        return find

    def find_phone(self, phone):
        '''
        根据手机号查询用户信息
        :param phone: 手机号，
        :return: 'pymongo.cursor.Cursor'
        '''
        login_phone = {"user_phone": phone}
        field = {"username": 1, "user_phone": 1, "password": 1}

        find = User_db.mycol.find(login_phone, field)

        return find

    def add_love(self):
        '''
        添加收藏。为每个用户建一个数据库，拉到吧。
        :return:
        '''

    def delete_user(self, user_phone):
        '''
        删除用户
        :param user_phone: 用户的手机号
        :return: 删除了几条数据
        '''
        myquery = {"user_phone": user_phone}
        one = User_db.mycol.delete_one(myquery)
        # print(type(one))
        # print(one)
        # print(one.deleted_count)
        # for x in one:
        #     print(x)
        return one.deleted_count


if __name__ == '__main__':
    db = User_db()
    mydict = {"group": "admin-temp", "username": "admin_temp", "user_phone": "18500000001", "password": "admin",
              "mailbox": "cubecats@icloud.com",
              "recording": '0'}
    # db.add_user(mydict)
    # find = db.query_registered('admin_temp')
    # print(find)
    # print(type(find))
    # print(db.find_ID())
    print(db.query_all())
    # print('group')
    # group = db.find_group('user-temp')
    # for x in group:
    #     print(x)
    # login = db.query_login("18500000001")
    # print(login)
    # update_pass = db.update_pass('18500000001', 'new_admin', "cubecats@icloud.com")
    # print(update_pass)
    # db.delete_user('1234')

