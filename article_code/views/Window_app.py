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
from designer import home, login, registered, list_item, item_test
from views import Registered_Dialog, Forget_Password_Dialog, Login_Dialog, home_page
from images import *
from utils import ip_get_location, download_image, city_all_name
from base import home_and_locad_data
from MongoDB import locad_jd
from control import local_control, local_xia_la_list_control
from app_global import Current_User
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import item.user_love


class Window_app(QMainWindow):
    data = home_and_locad_data.Data()
    local_info_class = local_control.Local_Control()

    def __init__(self):
        QMainWindow.__init__(self)
        self.main_ui = home.Ui_MainWindow()
        self.main_ui.setupUi(self)
        # 获得子窗口对象
        # self.chick_window = Login_Dialog.Login_Dialog()
        # 弹出子窗口
        # self.main_ui.login_but.clicked.connect(self.chick_window.show)
        self.main_ui.login_but.clicked.connect(self.login_user)

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
        pix = QPixmap(path + '/images/开封/清明上河园.jpg')

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

        # 初始化主页信息
        self.web = self.main_ui.home_webEngineView
        self.web.load(QUrl('https://tianqi.qq.com/index.htm'))
        self.web.show()

        # 初始化用户收藏
        self.love_list = self.main_ui.user_love_listWidget
        self.user_love()
        # item.user_love.add_user_love_item(self.love_list)

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

        self.fenlei = self.main_ui.ld_fenlei
        # 下啦列表的使用
        self.city = self.main_ui.ld_city
        city_name = city_all_name.get_all_city_name()
        for key, value in city_name.items():
            self.fenlei.addItem(key)
        current_text = self.fenlei.currentText()
        name_city = city_name.get('热门')
        for name in name_city:
            self.city.addItem(name)
        # self.fenlei.activated.connect(self.ld_currentIndexChanged)
        self.fenlei.activated.connect(self.ld_currentIndexChanged)

        # 获取位置
        # self.main_ui.locad_city.setText('定位：'+ip_get_location.get_location())

    def ld_currentIndexChanged(self):
        # print('fsdafdfasfsafsa')
        city_name = city_all_name.get_all_city_name()
        # print(self.fenlei.currentText())
        city_name_get = city_name.get(self.fenlei.currentText())
        self.city.clear()
        for name in city_name_get:
            self.city.addItem(name)
        self.city.activated.connect(self.change_city)

    def add_local_info(self):
        # print('add_local_info')
        data = Window_app.data
        # 内容补充
        # 景点名
        self.main_ui.locad_scenic_name_1.setText(data.get_locad_scenic_name_1())
        # 景点介绍
        self.main_ui.locad_scenic_introduction_1.setText(data.get_locad_scenic_introduction_1())
        # print(Window_app.data.get_locad_scenic_image_1(),'s')
        # 景点图片
        pix = QPixmap(data.get_locad_scenic_image_1())
        self.main_ui.locad_scenic_image_1.setPixmap(pix)
        self.main_ui.locad_scenic_image_1.setScaledContents(True)
        self.main_ui.locad_scenic_image_1.setAlignment(Qt.AlignCenter)
        # 价格
        self.main_ui.locad_scenic_jiage_1.setText('价格：' + str(data.get_locad_scenic_info_1().get('price')))
        # 等级
        # print(type())
        self.main_ui.locad_scenic_dengji_1.setText('等级：' + str(data.get_locad_scenic_info_1().get('level')))

        # 喜欢
        # 分享
        # 虚拟订单
        self.main_ui.locad_scenic_name_2.setText(data.get_locad_scenic_name_2())
        self.main_ui.locad_scenic_introduction_2.setText(data.get_locad_scenic_introduction_2())
        q_pixmap = QPixmap(data.get_locad_scenic_image_2())
        # print(Window_app.data.get_locad_scenic_image_2())
        self.main_ui.locad_scenic_image_2.setPixmap(q_pixmap)
        self.main_ui.locad_scenic_image_2.setScaledContents(True)
        self.main_ui.locad_scenic_image_2.setAlignment(Qt.AlignCenter)
        # 价格
        self.main_ui.locad_scenic_jiage_2.setText('价格：' + str(data.get_locad_scenic_info_2().get('price')))
        # 等级
        # print(type())
        self.main_ui.locad_scenic_dengji_2.setText('等级：' + str(data.get_locad_scenic_info_2().get('level')))

    def suggest_page(self):
        '''
        搜索页面
        :return:
        '''
        add_widget = self.stacked_Widget.addWidget(self.main_ui.page_suggest)
        self.stacked_Widget.setCurrentIndex(add_widget)
        #


        self.main_ui.ss_ssbutton.clicked.connect(self.ss_jd)

    def ss_jd(self):
        self.ss_comboBox = self.main_ui.ss_comboBox
        self.line_edit = self.main_ui.ss_lineEdit
        index = self.ss_comboBox.currentText()
        if index == '城市':
            pass
        if index == '景点':
            pass

        input_text = self.line_edit.text()

        pass

    def about_page(self):
        '''
        我的页面
        :return:
        '''
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

    def login_user(self):
        # user = Current_User.Current_User()
        user = Current_User.Current_User()
        # print(user.get_current_user_phone())
        if user.get_current_user_phone() == 'null':
            # 去登陆
            print('去登陆')
            self.main_ui.login_but.setText('正在登陆')
            self.chick_window = Login_Dialog.Login_Dialog()
            # self.connect(self.chick_window,QtCore.PYQT_SIGNAL("transfer_father"),self.updata_login_info)
            # self.emit(QtCore.PYQT_SIGNAL("transfer_father"), str)
            show = self.chick_window.show()
            # self.connect(self.chick_window,QtCore.PYQT_SIGNAL("transfer_child"),self.chick_window.updata_login_info)
            print(type(show))
            print(show)
            # print('333333333444ddd',self.main_ui)
        else:
            print('改文字')
            self.main_ui.login_but.setText('退出?2')
            # self.main_ui.login_but.setText('登陆')
            # print('333333333444ddd',self.main_ui)
            # app = Window_app()
            # app.main_ui.login_but.setText('dsfs')

            pass

    # 接受子窗口的值
    def updata_login_info(self, m):
        self.login_but.setText('退出2')

    def user_love(self):

        def user_love_item():
            jd_city = 'city'
            jd_name = 'namenamenamenamename'
            jd_js = 'jsjsjsjsjsjsjsjsjsjsjsjsjsjsjsjsjsjsjsjsjsjsjsjsjsjsjsjsjs'
            wight = QtWidgets.QWidget()
            layout_main = QtWidgets.QHBoxLayout()

            city = QtWidgets.QLabel(jd_city)
            name = QtWidgets.QLabel(jd_name)
            js = QtWidgets.QLabel(jd_js)
            delete = QtWidgets.QPushButton('删除')
            dg = QtWidgets.QPushButton("订购")
            layout_main.addWidget(city)

            layout_main.addWidget(name)
            layout_main.addWidget(js)
            layout_main.addWidget(delete)
            layout_main.addWidget(dg)
            layout_main.setStretchFactor(city, 2)
            layout_main.setStretchFactor(name, 2)
            layout_main.setStretchFactor(js, 20)

            wight.setLayout(layout_main)
            return wight

        # self.love_list = self.main_ui.user_love_listWidget

        for i in range(3):
            item = QtWidgets.QListWidgetItem()
            item.setSizeHint(QSize(740, 40))
            widget = user_love_item()
            self.love_list.addItem(item)
            self.love_list.setItemWidget(item, widget)

    def change_city(self):
        '''
        修改推荐城市了，
        :return:
        '''
        # 获取本地景点信息
        # print(self.city.currentText())

        index = self.city.currentText()
        locad_jd.parse_city(index)
        # 初始化本地内容
        Window_app.data = home_and_locad_data.Data()
        Window_app.local_info_class = local_xia_la_list_control.Local_Control(index + '市')
        Window_app.local_info_class.init_local()
        data = Window_app.data
        print(data.get_locad_scenic_name_2())

        self.add_local_info()
