import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    # 创建   类实例
    app = QApplication(sys.argv)
    # 创建窗口
    w = QWidget()
    #
    w.resize(400,200)
    #
    w.move(300,300)

    #
    w.setWindowTitle('pyqt5')
    #
    w.show()
    #
    sys.exit(app.exec_())