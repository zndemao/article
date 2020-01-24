import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon


class MainWin(QMainWindow):
    def __init__(self, parent=None):
        super(MainWin, self).__init__(parent)

        # set main title
        self.setWindowTitle("my title")

        # 设置窗口的尺寸
        self.resize(1230, 670)

        # 获得状态栏
        # self.status = self.statusBar()
        # 在状态栏上显示信息
        # self.status.showMessage('欢迎来到此程序，此提示仅显示5s', 5000)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setWindowIcon('..images/*.*')
    main = MainWin()
    main.show()

    sys.exit(app.exec_())
