# 退出应用程序

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QDesktopWidget, QHBoxLayout, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from study import FirstMainWin


class QuitApplication(QMainWindow):
    def __init__(self, parent=None):
        super(QuitApplication, self).__init__(parent)

        # set main title
        self.setWindowTitle("退出应用程序")

        # 设置窗口的尺寸
        self.resize(1230, 670)
        self.center_window()

        # 获得状态栏
        # self.status = self.statusBar()
        # 在状态栏上显示信息
        # self.status.showMessage('欢迎来到此程序，此提示仅显示5s', 5000)
        #
        self.add_button()

    '''让窗口居中'''

    def center_window(self):
        print('窗口居中')
        # 获取屏幕坐标系
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        new_left = (screen.width() - size.width()) / 2
        new_top = (screen.height() - size.height()) / 2
        self.move(new_left, new_top)

    def add_button(self):
        self.quit_button = QPushButton('退出应用程序')
        self.quit_button.clicked.connect(self.on_click_quit_button)

        layout = QHBoxLayout()
        layout.addWidget(self.quit_button)

        q_widget = QWidget()
        q_widget.setLayout(layout)
        self.setCentralWidget(q_widget)

    # 自定义的槽，自定义的事件
    def on_click_quit_button(self):
        sender = self.sender()
        print(sender.text() + 'on click')
        app = QApplication.instance()
        app.quit()

    def test(self):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setWindowIcon('..images/*.*')
    main = QuitApplication()
    main.show()

    sys.exit(app.exec_())
