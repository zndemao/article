import sys

from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from distributed.utils import palette
from PyQt5.QtCore import Qt
from designer import home, login


def showMessage(self):
    print('suff')
    QMessageBox.about(ui.buttontest, 'a', 'b')


class chikd_Window(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child = login.Ui_Dialog()
        self.child.setupUi(self)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)  # 屏蔽父亲窗口操作


class Run:

    def showMessage(self):
        print('suff2')
        QMessageBox.about(ui.buttontest, 'a', 'b')


if __name__ == '__main__':
    # 创建   类实例
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = home.Ui_MainWindow()
    zi = chikd_Window()
    ui.setupUi(window)

    # _translate = QtCore.QCoreApplication.translate
    # ui.login.setText(_translate("MainWindow", "退出test"))
    ui.buttontest.clicked.connect(zi.show)
    # ui.buttontest.clicked.connect(window.close)# 关闭父窗口
    # ui.labeltest.clicked.connect(Run.showMessage)
    window.show()
    sys.exit(app.exec_())
