'''
案例窗口跳转
点击按键，串口跳转到模拟的登陆、注册界面。并屏蔽父亲窗口操作。
# ui.buttontest.clicked.connect(window.close)# 关闭父窗口
要求，规范化
'''

import sys

from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from distributed.utils import palette
from PyQt5.QtCore import Qt
from designer import home, login,registered
from views import Registered_Dialog

# class Registered_Dialog(QDialog):
#     def __init__(self):
#         QDialog.__init__(self)
#         self.registered_Dialog = registered.Ui_Dialog()
#         self.registered_Dialog.setupUi(self)
#         # self.setWindowFlags(Qt.WindowStaysOnTopHint)  # 屏蔽父亲窗口操作
#




class Chikd_Window(QDialog):
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
        print('login button on')
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
        pass


class Home_Window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.main_ui = home.Ui_MainWindow()
        self.main_ui.setupUi(self)
        # 获得子窗口对象
        self.chick_window = Chikd_Window()
        # 弹出子窗口
        self.main_ui.buttontest.clicked.connect(self.chick_window.show)


if __name__ == '__main__':
    # 创建   类实例
    app = QApplication(sys.argv)

    window = Home_Window()  # 主窗口
    login_window = Chikd_Window  # 子窗口

    # _translate = QtCore.QCoreApplication.translate
    # ui.login.setText(_translate("MainWindow", "退出test"))
    # ui.buttontest.clicked.connect(window.close)# 关闭父窗口
    # ui.labeltest.clicked.connect(Run.showMessage)
    window.show()
    sys.exit(app.exec_())
