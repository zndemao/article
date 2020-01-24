# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.login_close = QtWidgets.QPushButton(Dialog)
        self.login_close.setGeometry(QtCore.QRect(70, 180, 113, 32))
        self.login_close.setObjectName("login_close")
        self.login_registered = QtWidgets.QPushButton(Dialog)
        self.login_registered.setGeometry(QtCore.QRect(270, 260, 113, 32))
        self.login_registered.setAutoDefault(False)
        self.login_registered.setObjectName("login_registered")
        self.login_login_button = QtWidgets.QPushButton(Dialog)
        self.login_login_button.setGeometry(QtCore.QRect(220, 180, 113, 32))
        self.login_login_button.setAutoDefault(False)
        self.login_login_button.setObjectName("login_login_button")
        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(70, 70, 261, 61))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.user_name = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.user_name.setObjectName("user_name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.user_name)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.user_password = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.user_password.setObjectName("user_password")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.user_password)
        self.login_forget_password = QtWidgets.QPushButton(Dialog)
        self.login_forget_password.setGeometry(QtCore.QRect(20, 260, 113, 32))
        self.login_forget_password.setAutoDefault(False)
        self.login_forget_password.setObjectName("login_forget_password")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "登陆"))
        self.login_close.setText(_translate("Dialog", "取消"))
        self.login_registered.setText(_translate("Dialog", "注册"))
        self.login_login_button.setText(_translate("Dialog", "登陆"))
        self.label.setText(_translate("Dialog", "用户名"))
        self.label_2.setText(_translate("Dialog", "密  码"))
        self.login_forget_password.setText(_translate("Dialog", "忘记密码"))
