#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   user_love.py    
@Contact :   cubecats@icloud.com
@License :   (C)Copyright 2017-2018, DAMN-CAT

@Modify Time        @Author     @Version    @Desciption
------------        --------    --------    -----------
2020/3/8 上午11:38    damn cat    1.0         None
'''

# import lib
import sys
import json
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets


def add_user_love_item(love_list):
    # print('list')

    def user_love_item():
        jd_city = 'city2'
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



    for i in range(3):
        item = QtWidgets.QListWidgetItem()
        item.setSizeHint(QSize(740, 40))
        widget = user_love_item()
        love_list.addItem(item)
        love_list.setItemWidget(item, widget)
