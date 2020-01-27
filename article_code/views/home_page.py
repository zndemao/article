from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap

from designer import home
import os


class Home_Page(QtWidgets.QLabel):
    def __init__(self):
        self.name = '测试景点名称'
        self.image = ''
        self.introduction = '测试内容，测试内容，测试内容，测试内容，测试内容，测试内容' \
                            '，测试内容，测试内容，测试内容，测试内容，测试内容，测试内容，' \
                            '测试内容，测试内容，测试内容，测试内容，测试内容，测试内容，测试内容，测试内容'


    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_image(self):

        path = os.path.abspath(os.path.join(os.getcwd(), '..'))
        pix = QPixmap(path + '/images/xjj.jpg')

        return pix

    def set_image(self, image):
        self.image = image

    def get_introduction(self):
        return self.introduction

    def set_introduction(self, introduction):
        self.introduction = introduction
