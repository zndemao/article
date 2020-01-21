import sys

from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from distributed.utils import palette
from PyQt5.QtCore import Qt
from designer import home, login, registered
from views import Registered_Dialog, Forget_Password_Dialog,Login_Dialog


class Home_Window(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.main_ui = home.Ui_MainWindow()
        self.main_ui.setupUi(self)
        # 获得子窗口对象
        self.chick_window = Login_Dialog.Login_Dialog()
        # 弹出子窗口
        self.main_ui.login_but.clicked.connect(self.chick_window.show)
