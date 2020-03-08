#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   Current_User.py    
@Contact :   cubecats@icloud.com
@License :   (C)Copyright 2017-2018, DAMN-CAT

@Modify Time        @Author     @Version    @Desciption
------------        --------    --------    -----------
2020/3/7 上午11:50    damn cat    1.0         None
'''


# import lib
class Current_User:
    current_user_name = '未登陆'
    current_user_phone = 'null'
    current_user_group = 'user'

    def get_current_user_name(self):
        return Current_User.current_user_name

    def set_current_user_name(self, name):
        Current_User.current_user_name = name

    def get_current_user_phone(self):
        return Current_User.current_user_phone

    def set_current_user_phone(self, phone):
        Current_User.current_user_phone = phone

    def get_current_user_group(self):
        return Current_User.current_user_group

    def set_current_user_group(self, group):
        Current_User.current_user_group = group

    def set_user_info(self, group, name, phone):
        Current_User.current_user_group = group
        Current_User.current_user_name = name
        Current_User.current_user_phone = phone


if __name__ == "__main__":
    pass
