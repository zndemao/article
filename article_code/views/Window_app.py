import sys
import os
from PyQt5.QtGui import QPalette, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog, QListView
from PyQt5 import QtCore, QtGui, QtWidgets
from distributed.utils import palette
from PyQt5.QtCore import Qt, QStringListModel
from designer import home, login, registered, list_item
from views import Registered_Dialog, Forget_Password_Dialog, Login_Dialog, home_page
from images import *


class Window_app(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.main_ui = home.Ui_MainWindow()
        self.main_ui.setupUi(self)
        # 获得子窗口对象
        self.chick_window = Login_Dialog.Login_Dialog()
        # 弹出子窗口
        self.main_ui.login_but.clicked.connect(self.chick_window.show)

        index = self.main_ui.stackedWidget.setCurrentIndex(1)
        about_page = self.main_ui.page_about
        self.stacked_Widget = self.main_ui.stackedWidget
        # print(widget.currentIndex())
        #  切换页面
        self.main_ui.home_but.clicked.connect(self.home_page)
        self.main_ui.locad_but.clicked.connect(self.locad_page)
        self.main_ui.suggest_but.clicked.connect(self.suggest_page)
        self.main_ui.about_but.clicked.connect(self.about_page)

        self.init()

    def init(self):
        add_widget = self.stacked_Widget.addWidget(self.main_ui.page_home)
        self.stacked_Widget.setCurrentIndex(add_widget)
        # 初始化home内部按钮
        # 图片路径
        path = os.path.abspath(os.path.join(os.getcwd(), '..'))
        print(os.getcwd())
        print(path)
        print(path + '/images/xjj.jpg')

        pix = QPixmap(path + '/images/xjj.jpg')

        # lb1 = QLabel(self)
        # lb1.setGeometry(0, 0, 300, 200)
        # lb1.setStyleSheet("border: 2px solid red")
        # lb1.setPixmap(pix)

        self.main_ui.home_scenic_image.setPixmap(pix)
        # self.main_ui.home_scenic_image.setScaledContents(True)
        self.main_ui.home_scenic_image.setAlignment(Qt.AlignCenter)

    def home_page(self):
        add_widget = self.stacked_Widget.addWidget(self.main_ui.page_home)
        self.stacked_Widget.setCurrentIndex(add_widget)

        home = home_page.Home_Page()
        self.main_ui.home_scenic_name.setText(home.get_name())
        self.main_ui.home_scenic_image.setPixmap(home.get_image())
        self.main_ui.home_scenic_introduction.setText(home.get_introduction())
    def locad_page(self):
        add_widget = self.stacked_Widget.addWidget(self.main_ui.page_locad)
        self.stacked_Widget.setCurrentIndex(add_widget)

        path = os.path.abspath(os.path.join(os.getcwd(), '..'))
        print(path + '/images/xjj.jpg')
        pix = QPixmap(path + '/images/xjj2.jpg')

        self.main_ui.locad_scenic_image_1.setPixmap(pix)
        self.main_ui.locad_scenic_image_1.setScaledContents(True)
        self.main_ui.locad_scenic_image_1.setAlignment(Qt.AlignCenter)

        view = QListView()
        model = QStringListModel()
        self.l = ['1', '2', '3']
        model.setStringList(self.l)
        print(type(model))
        print(type(list_item.Ui_Frame()))
        # self.main_ui.listView.setModel(model)
        # self.main_ui.listWidget.addItem("1")
        # self.main_ui.listWidget.addItem('2')

    def suggest_page(self):
        add_widget = self.stacked_Widget.addWidget(self.main_ui.page_suggest)
        self.stacked_Widget.setCurrentIndex(add_widget)

    def about_page(self):
        widget = self.main_ui.stackedWidget
        print(widget.currentIndex())
        add_widget = widget.addWidget(self.main_ui.page_about)
        print(add_widget)
        widget.setCurrentIndex(add_widget)
        pass
