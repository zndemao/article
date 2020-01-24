import sys

from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from distributed.utils import palette
from PyQt5.QtCore import Qt
from designer import home, login, registered
from views import Window_app, Registered_Dialog, Forget_Password_Dialog

if __name__ == '__main__':
    # 创建   类实例
    app = QApplication(sys.argv)

    window = Window_app.Window_app()  # 主窗口
    # login_window = Chikd_Window  # 子窗口

    # _translate = QtCore.QCoreApplication.translate
    # ui.login.setText(_translate("MainWindow", "退出test"))
    # ui.buttontest.clicked.connect(window.close)# 关闭父窗口
    # ui.labeltest.clicked.connect(Run.showMessage)
    window.show()
    sys.exit(app.exec_())
