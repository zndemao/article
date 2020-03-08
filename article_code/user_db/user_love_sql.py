#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   user_love_sql.py
@Contact :   cubecats@icloud.com
@License :   (C)Copyright 2017-2018, DAMN-CAT

@Modify Time        @Author     @Version    @Desciption
------------        --------    --------    -----------
2020/3/6 下午5:49    damn cat    1.0         None
'''

# import lib
import pymongo
from bson import ObjectId


class User_Love_SQL:
    pass

    def add_user_love(self, user_phone, love_id):
        # 连接到数据库
        user_client = pymongo.MongoClient("mongodb://localhost:27017/")
        # 数据库名称
        user_db = user_client["db_user"]
        # 表名称
        user_love = user_db["user_love_" + user_phone]

        user_love_data = {"time": "time", "love": love_id}
        one = user_love.insert_one(user_love_data)
        # print(type(one))
        # print(one)
        # for x in one:
        #     print(x)
        # pass

    def find_love(self, user_phone):
        # 连接到数据库
        user_client = pymongo.MongoClient("mongodb://localhost:27017/")
        # 数据库名称
        user_db = user_client["db_user"]
        # 表名称
        user_love = user_db["user_love_" + user_phone]
        find = user_love.find()
        # for x in find:
        #     print(x)
        return find


    def delete_user_love(self, user_phone, love_id):
        # 连接到数据库
        user_client = pymongo.MongoClient("mongodb://localhost:27017/")
        # 数据库名称
        user_db = user_client["db_user"]
        # 表名称
        user_love = user_db["user_love_" + user_phone]
        print("user_love_" + user_phone)
        user_love_data = {"time": "time", "love": love_id}

        one = user_love.delete_one(user_love_data)
        return one.deleted_count


if __name__ == '__main__':
    db = User_Love_SQL()
    db.add_user_love(user_phone='121', love_id='模拟数据2')
    db.find_love('121')
    # (db.find_love('121'))
    # print(db.delete_user_love(user_phone='123456', love_id='模拟数据2'))
