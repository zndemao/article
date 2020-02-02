# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registered.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(400, 300)
        self.formLayoutWidget = QtWidgets.QWidget(dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(80, 35, 231, 147))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.reg_phone = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.reg_phone.setObjectName("reg_phone")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.reg_phone)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.reg_pass_1 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.reg_pass_1.setObjectName("reg_pass_1")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.reg_pass_1)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.reg_pass_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.reg_pass_2.setObjectName("reg_pass_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.reg_pass_2)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.reg_mailbox = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.reg_mailbox.setObjectName("reg_mailbox")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.reg_mailbox)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.reg_name = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.reg_name.setObjectName("reg_name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.reg_name)
        self.reg_close = QtWidgets.QPushButton(dialog)
        self.reg_close.setGeometry(QtCore.QRect(60, 210, 113, 32))
        self.reg_close.setObjectName("reg_close")
        self.reg_reg = QtWidgets.QPushButton(dialog)
        self.reg_reg.setGeometry(QtCore.QRect(200, 210, 113, 32))
        self.reg_reg.setAutoDefault(False)
        self.reg_reg.setObjectName("reg_reg")

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "注册"))
        self.label.setText(_translate("dialog", "手机号"))
        self.label_2.setText(_translate("dialog", "密码"))
        self.label_3.setText(_translate("dialog", "确认密码"))
        self.label_4.setText(_translate("dialog", "邮箱"))
        self.label_5.setText(_translate("dialog", "用户名"))
        self.reg_close.setText(_translate("dialog", "取消"))
        self.reg_reg.setText(_translate("dialog", "注册"))

