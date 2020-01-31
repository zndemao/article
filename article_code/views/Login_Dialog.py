'''
登陆窗口
'''
import sys

from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from distributed.utils import palette
from PyQt5.QtCore import Qt
from designer import home, login, registered
from views import Registered_Dialog, Forget_Password_Dialog
from control import user_control
from PyQt5.QtGui import QPixmap


class Login_Dialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.login_window = login.Ui_Dialog()
        self.login_window.setupUi(self)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)  # 屏蔽父亲窗口操作

        # self.dialog = Registered_Dialog.Registered_Dialog()
        # 按键操作
        self.login_window.login_close.clicked.connect(self.close)
        self.login_window.login_login_button.clicked.connect(self.user_login)
        self.login_window.login_registered.clicked.connect(self.registered)
        self.login_window.login_forget_password.clicked.connect(self.forget_password)

    # 取消
    def close(self):
        print('取消登陆')
        # self.accept() # 可用于关闭窗口，但不知道与reject的区别
        self.reject()  # 用于关闭窗口
        pass

    # 登陆
    def user_login(self):
        # print('login button on')
        phone = self.login_window.user_phone.text()
        password = self.login_window.user_password.text()
        # toast = ''
        if phone == '':
            self.MessageBox('手机号不能为空')
            return
            # toast = '手机号不能为空'
        if password == '':
            self.MessageBox('密码不能为空')
            # toast = '密码不能为空'
            return
        print(phone)
        control = user_control.User_Control()
        login = control.login(phone, password)
        print(login)
        # msgBox = QMessageBox(QMessageBox.NoIcon, '提示', '不要意淫了，早点洗洗睡吧!')
        # msgBox.setIconPixmap(QPixmap("beauty.png"))
        # msgBox.exec()
        self.accept()  # 接受
        pass

    # 注册
    def registered(self):
        print('on registered button')
        # 打开登陆窗口
        self.dialog = Registered_Dialog.Registered_Dialog()
        self.dialog.show()
        # 关闭登陆窗口
        self.reject()  # 关闭窗口

        pass

    # 忘记密码
    def forget_password(self):
        print('on forget password')
        # Forget_Password_Dialog.Forget_PassWord().show()
        # 打开忘记密码子窗口
        self.forget_password = Forget_Password_Dialog.Forget_PassWord()
        self.forget_password.show()
        # print(self.forget_password)
        # forget_password2 = Forget_Password_Dialog.Forget_PassWord()
        # forget_password2.show()
        # print(forget_password2)
        self.reject()
        pass

    def MessageBox(self, text):
        msgBox = QMessageBox(QMessageBox.NoIcon, '提示', text)
        # msgBox.setIconPixmap(QPixmap("beauty.png"))
        msgBox.exec()
