import user_db.user_sql as users_data
from user_db import user_love_sql
from utils import MyLog
import sys
from app_global import Current_User


class User_Control():
    mydict = {"group": "admin-temp", "username": "admin_temp", "user_phone": "18500000001", "password": "admin",
              "mailbox": "cubecats@icloud.com",
              "recording": '0'}
    db = users_data.User_db()

    # 注册用户
    def user_registered(self, group_name, name, phone, password_1, password_2, mailbox):
        '''
        注册用户
        :param group:
        :param name:用户名
        :param phone:手机号
        :param password_1:密码
        :param password_2:确认密码
        :param mailbox:邮箱
        :return: str 注册成功
        '''

        if group_name:
            group = 'admin'
        else:
            group = 'user'

        find_phone = User_Control.db.find_phone(phone)
        for x in find_phone:
            print('手机号已经创建过账户了')
            return '手机号已经创建过账户了'
        if password_1 != password_2:
            return '密码不一致'
        password = password_1
        user_info = {"group": group, "username": name, "user_phone": phone, "password": password,
                     "mailbox": mailbox,
                     "recording": '0'}
        User_Control.db.add_user(user_info)
        return '注册成功'

    # 忘记密码
    def update_password(self, phone, password_1, password_2, mailbox):
        if password_1 != password_2:
            return '密码不一致'
        password = password_1
        update_pass = User_Control.db.update_pass(phone, password, mailbox)
        if update_pass:
            return '修改成功'
        else:
            return '修改失败'

    # 登陆
    def login(self, phone, password):
        login_info = User_Control.db.query_login(phone)
        password_db = login_info.get('password')
        if password == password_db:
            return True
        else:
            return False

    # 删除用户。管理员权限可用。
    def delete_user(self, user_phone):
        '''
        # 删除用户。管理员权限可用。
        :param user_phone: 用户手机号
        :return: '删除成功'
        '''
        delete_count = User_Control.db.delete_user(user_phone=user_phone)
        if delete_count >= 1:
            return '删除成功'
        else:
            return "删除失败"

    def find_users(self):
        '''
        查询用户
        :return: <class 'pymongo.cursor.Cursor'>
        '''
        group = User_Control.db.find_group('user-temp')
        for x in group:
            print(x)
        # pass
        print(type(group))
        return group

    def add_user_love(self, user_phone, id):

        db = user_love_sql.User_Love_SQL()
        love = db.add_user_love(user_phone=user_phone, love_id=id)
        # love = User_Control.add_user_love(user_phone, id)
        # print(love)
        MyLog.my_print(self.__class__.__name__, MyLog.fun_name(), love)
        return '添加成功'

    def delete_user_love(self, user_phone, id):
        db = user_love_sql.User_Love_SQL()
        love = db.delete_user_love(user_phone=user_phone, love_id=id)
        return '删除成功'
        pass

    def find_user_love(self, user_phone):
        db = user_love_sql.User_Love_SQL()
        find_love = db.find_love(user_phone)
        # User_Control().print_info(find_love)
        return find_love

    def print_info(self, data):
        if True:
            for x in data:
                print(x)

    def set_user_info(self, phone):
        login_info = User_Control.db.query_login(phone)
        user = Current_User.Current_User()
        user.set_user_info(login_info.get('group'), login_info.get('username'), login_info.get('user_phone'))
        # user.set_user_info('', '', '')
        # for x in login_info:
        #     MyLog.my_print(self.__class__.__name__, MyLog.fun_name(), x)
        print(user.get_current_user_group())

        pass


if __name__ == '__main__':
    control = User_Control()
    # registered = control.user_registered(name='test', phone='123', password_1='1234', password_2='1234',
    #                                           mailbox='t')
    # print(registered)
    # password = control.update_password('123', '12', '12', 't')
    # print(password)
    # login = control.login('123', '12')
    # print(login)
    # control.add_user_love('1234', '控制测试')
    control.set_user_info('1234')
