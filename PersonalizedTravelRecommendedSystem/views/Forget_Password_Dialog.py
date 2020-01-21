import sys

from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from distributed.utils import palette
from PyQt5.QtCore import Qt
from designer import home, login, registered, forget_password
from views import example_Window_Jump


class Forget_PassWord(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.forget_password_ui_dialog = forget_password.Ui_Dialog()
        self.forget_password_ui_dialog.setupUi(self)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)  # 屏蔽父亲窗口操作

        self.forget_password_ui_dialog.forget_password_cancel.clicked.connect(self.forget_password_window_close)
        self.forget_password_ui_dialog.modify_password.clicked.connect(self.forget_password_window_modify_password)

    def forget_password_window_close(self):
        print('这里是取消忘记密码')
        self.reject()

    def forget_password_window_modify_password(self):
        print('这里是点击忘记密码')
        self.window = example_Window_Jump.Chikd_Window()
        self.window.show()
        self.accept()
