'''
注册账户窗口
'''
import sys

from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from distributed.utils import palette
from PyQt5.QtCore import Qt
from designer import home, login, registered
from views import Window_app, Login_Dialog
from control import user_control


class Registered_Dialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.registered_Dialog = registered.Ui_Dialog()
        self.registered_Dialog.setupUi(self)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)  # 屏蔽父亲窗口操作

        self.registered_Dialog.reg_close.clicked.connect(self.registered_window_close)
        self.registered_Dialog.reg_reg.clicked.connect(self.registered_window_registered)

    def registered_window_close(self):
        print('这里是取消注册')
        self.reject()

    def registered_window_registered(self):
        print('这里是点击注册')
        registered = self.registered_Dialog
        name = registered.reg_name.text()
        phone = registered.reg_phone.text()
        pass_1 = registered.reg_pass_1.text()
        pass_2 = registered.reg_pass_2.text()
        mailbox = registered.reg_mailbox.text()

        control = user_control.User_Control()
        registered = control.user_registered(name, phone, pass_1, pass_2, mailbox)
        print(registered)

        self.window = Login_Dialog.Login_Dialog()
        self.window.show()
        self.accept()

    def MessageBox(self, text):
        msgBox = QMessageBox(QMessageBox.NoIcon, '提示', text)
        # msgBox.setIconPixmap(QPixmap("beauty.png"))
        msgBox.exec()
