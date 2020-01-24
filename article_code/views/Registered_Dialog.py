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
from views import Window_app,Login_Dialog

class Registered_Dialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.registered_Dialog = registered.Ui_Dialog()
        self.registered_Dialog.setupUi(self)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)  # 屏蔽父亲窗口操作

        self.registered_Dialog.pushButton.clicked.connect(self.registered_window_close)
        self.registered_Dialog.pushButton_2.clicked.connect(self.registered_window_registered)

    def registered_window_close(self):
        print('这里是取消注册')
        self.reject()

    def registered_window_registered(self):
        print('这里是点击注册')
        self.window = Login_Dialog.Login_Dialog()
        self.window.show()
        self.accept()