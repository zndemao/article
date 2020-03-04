# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forget_password.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(80, 60, 231, 116))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.pass_phone = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.pass_phone.setObjectName("pass_phone")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.pass_phone)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.pass_pass_1 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.pass_pass_1.setObjectName("pass_pass_1")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.pass_pass_1)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.pass_pass_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.pass_pass_2.setObjectName("pass_pass_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.pass_pass_2)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.pass_mailbox = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.pass_mailbox.setObjectName("pass_mailbox")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.pass_mailbox)
        self.forget_password_cancel = QtWidgets.QPushButton(Dialog)
        self.forget_password_cancel.setGeometry(QtCore.QRect(60, 210, 113, 32))
        self.forget_password_cancel.setObjectName("forget_password_cancel")
        self.modify_password = QtWidgets.QPushButton(Dialog)
        self.modify_password.setGeometry(QtCore.QRect(200, 210, 113, 32))
        self.modify_password.setAutoDefault(False)
        self.modify_password.setObjectName("modify_password")
        self.forget_admin = QtWidgets.QRadioButton(Dialog)
        self.forget_admin.setGeometry(QtCore.QRect(80, 30, 100, 20))
        self.forget_admin.setObjectName("forget_admin")
        self.forget_user = QtWidgets.QRadioButton(Dialog)
        self.forget_user.setGeometry(QtCore.QRect(210, 30, 100, 20))
        self.forget_user.setChecked(True)
        self.forget_user.setObjectName("forget_user")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "忘记密码"))
        self.label.setText(_translate("Dialog", "手机号"))
        self.label_2.setText(_translate("Dialog", "密码"))
        self.label_3.setText(_translate("Dialog", "确认密码"))
        self.label_4.setText(_translate("Dialog", "邮箱"))
        self.forget_password_cancel.setText(_translate("Dialog", "取消"))
        self.modify_password.setText(_translate("Dialog", "修改密码"))
        self.forget_admin.setText(_translate("Dialog", " 管理员"))
        self.forget_user.setText(_translate("Dialog", "用户"))

