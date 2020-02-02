import sys
import os
import threading
import time
import logging
from PyQt5.QtGui import QPalette, QPixmap, QImage
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog, QListView
from PyQt5 import QtCore, QtGui, QtWidgets
from distributed.utils import palette
from PyQt5.QtCore import Qt, QStringListModel, QThread, pyqtSignal
from designer import home, login, registered, list_item
from views import Registered_Dialog, Forget_Password_Dialog, Login_Dialog, home_page
from images import *
from utils import ip_get_location, download_image
from base import home_and_locad_data
from MongoDB import locad_jd
from control import local_control


class Window_app(QMainWindow):
    data = home_and_locad_data.Data()
    local_info_class = local_control.Local_Control()

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
        self.main_ui.locad_but.clicked.connect(self.local_page)
        self.main_ui.suggest_but.clicked.connect(self.suggest_page)
        self.main_ui.about_but.clicked.connect(self.about_page)

        self.main_ui.next_page.clicked.connect(self.next_page_info)
        self.main_ui.previous_page.clicked.connect(self.previous_page_info)
        # 初始化
        self.init()

    def init(self):
        add_widget = self.stacked_Widget.addWidget(self.main_ui.page_home)
        self.stacked_Widget.setCurrentIndex(add_widget)
        # 初始化home内部按钮
        # 图片路径
        path = os.path.abspath(os.path.join(os.getcwd(), '..'))
        # print(os.getcwd())
        # print(path)
        print(path + '/images/xjj.jpg')
        pix = QPixmap(path + '/images/xjj.jpg')
        pix = QPixmap(path + '/images/xjj.jpg')

        self.main_ui.home_scenic_image.setPixmap(pix)
        # self.main_ui.home_scenic_image.setScaledContents(True)
        self.main_ui.home_scenic_image.setAlignment(Qt.AlignCenter)

        # 获取位置,使用线程
        threading.Thread(target=self.work).start()

        location = Window_app.data.get_location()
        # 获取本地景点信息
        locad_jd.parse_city(location)
        # 初始化本地内容
        Window_app.local_info_class.init_local()

    def home_page(self):
        add_widget = self.stacked_Widget.addWidget(self.main_ui.page_home)
        self.stacked_Widget.setCurrentIndex(add_widget)

        home = home_page.Home_Page()
        self.main_ui.home_scenic_name.setText(home.get_name())
        self.main_ui.home_scenic_image.setPixmap(home.get_image())
        self.main_ui.home_scenic_introduction.setText(home.get_introduction())

    def local_page(self):
        add_widget = self.stacked_Widget.addWidget(self.main_ui.page_locad)
        self.stacked_Widget.setCurrentIndex(add_widget)

        # path = os.path.abspath(os.path.join(os.getcwd(), '..'))
        # print(path + '/images/xjj.jpg')


        # self.main_ui.locad_scenic_image_1.setPixmap(pix)
        # self.main_ui.locad_scenic_image_1.setScaledContents(True)
        # self.main_ui.locad_scenic_image_1.setAlignment(Qt.AlignCenter)

        # date = download_image.download_date(
        #     'https://imgs.qunarzz.com/sight/p0/1701/88/885ec9c1584a572aa3.img.png_280x200_91ebdc7b.png')
        # img = QImage.fromData(date.content)
        # image = QPixmap.fromImage(img)

        # self.main_ui.locad_scenic_image_2.setPixmap(image)
        # self.main_ui.next_page.clicked.connect(self.next_page_info)
        # self.main_ui.previous_page.clicked.connect(self.previous_page_info)

        self.add_local_info()

        # 获取位置
        # self.main_ui.locad_city.setText('定位：'+ip_get_location.get_location())

    def add_local_info(self):
        # 内容补充
        self.main_ui.locad_scenic_name_1.setText(Window_app.data.get_locad_scenic_name_1())
        self.main_ui.locad_scenic_introduction_1.setText(Window_app.data.get_locad_scenic_introduction_1())
        # print(Window_app.data.get_locad_scenic_image_1(),'s')
        pix = QPixmap(Window_app.data.get_locad_scenic_image_1())
        self.main_ui.locad_scenic_image_1.setPixmap(pix)
        self.main_ui.locad_scenic_image_1.setScaledContents(True)
        self.main_ui.locad_scenic_image_1.setAlignment(Qt.AlignCenter)
        self.main_ui.locad_scenic_name_2.setText(Window_app.data.get_locad_scenic_name_2())
        self.main_ui.locad_scenic_introduction_2.setText(Window_app.data.get_locad_scenic_introduction_2())
        q_pixmap = QPixmap(Window_app.data.get_locad_scenic_image_2())
        # print(Window_app.data.get_locad_scenic_image_2())
        self.main_ui.locad_scenic_image_2.setPixmap(q_pixmap)
        self.main_ui.locad_scenic_image_2.setScaledContents(True)
        self.main_ui.locad_scenic_image_2.setAlignment(Qt.AlignCenter)

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

    def next_page_info(self):
        # print('sfdfs')
        info = Window_app.local_info_class.next_page_info()
        if len(info) == 0:
            self.MessageBox('已经是最后一页')
            return
        self.add_local_info()
        pass

    def previous_page_info(self):
        info = Window_app.local_info_class.previous_page_info()
        if len(info) == 0:
            self.MessageBox("已经是第一页")
            return
        self.add_local_info()
        pass

    def MessageBox(self, text):
        msgBox = QMessageBox(QMessageBox.NoIcon, '提示', text)
        # msgBox.setIconPixmap(QPixmap("beauty.png"))
        msgBox.exec()

    # 以下是用线程更新UI
    class MyThread(QThread):
        # signal = pyqtSignal(int)

        def __init__(self):
            super().__init__()

        def __del__(self):
            self.wait()

        def run(self):
            print("run")
            # self.work()

    def work(self):
        # location = ip_get_location.get_location()
        location = Window_app.data.get_location()
        print('Window_app:' + location)
        self.main_ui.locad_city.setText('定位：' + location)
        # print('Window_app2:' + Window_app.data.get_location())

        # for i in range(1, n + 1):
        #     print(str(i) + ": do something...")
        #     #
        #     time.sleep(1)
