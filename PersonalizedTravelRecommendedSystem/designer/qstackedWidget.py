# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qstackedWidget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_StackedWidget(object):
    def setupUi(self, StackedWidget):
        StackedWidget.setObjectName("StackedWidget")
        StackedWidget.resize(400, 300)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.pushButton = QtWidgets.QPushButton(self.page)
        self.pushButton.setGeometry(QtCore.QRect(120, 100, 113, 32))
        self.pushButton.setObjectName("pushButton")
        StackedWidget.addWidget(self.page)
        self.page1 = QtWidgets.QWidget()
        self.page1.setObjectName("page1")
        StackedWidget.addWidget(self.page1)

        self.retranslateUi(StackedWidget)
        QtCore.QMetaObject.connectSlotsByName(StackedWidget)

    def retranslateUi(self, StackedWidget):
        _translate = QtCore.QCoreApplication.translate
        StackedWidget.setWindowTitle(_translate("StackedWidget", "StackedWidget"))
        self.pushButton.setText(_translate("StackedWidget", "PushButton"))

