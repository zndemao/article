# 设置窗口居中
# QDesktopWidget

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget
from PyQt5.QtGui import QIcon


class CenterForm(QMainWindow):
    def __init__(self, parent=None):
        super(CenterForm, self).__init__(parent)

        # set main title
        self.setWindowTitle("my title")

        # 设置窗口的尺寸
        self.resize(1230, 670)
        self.center_window()

        # 获得状态栏
        # self.status = self.statusBar()
        # 在状态栏上显示信息
        # self.status.showMessage('欢迎来到此程序，此提示仅显示5s', 5000)

    '''让窗口居中'''

    def center_window(self):
        print('窗口居中')
        # 获取屏幕坐标系
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        new_left = (screen.width() - size.width()) / 2
        new_top = (screen.height() - size.height()) / 2
        self.move(new_left, new_top)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setWindowIcon('..images/*.*')
    main = CenterForm()
    main.show()

    sys.exit(app.exec_())