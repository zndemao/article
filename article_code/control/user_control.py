from MongoDB import users_data


class User_Control():
    mydict = {"group": "admin-temp", "username": "admin_temp", "user_phone": "18500000001", "password": "admin",
              "mailbox": "cubecats@icloud.com",
              "recording": '0'}
    db = users_data.User_db()

    # 注册
    def user_registered(self, name, phone, password_1, password_2, mailbox):
        if password_1 != password_2:
            return '密码不一致'
        password = password_1
        user_info = {"group": "user-temp", "username": name, "user_phone": phone, "password": password,
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
            return '登陆成功'
        else:
            return '登陆失败'



    pass


if __name__ == '__main__':
    control = User_Control()
    # registered = control.user_registered(name='test', phone='123', password_1='1234', password_2='1234',
    #                                           mailbox='t')
    # print(registered)
    password = control.update_password('123', '12', '12', 't')
    print(password)
    login = control.login('123', '12')
    print(login)
