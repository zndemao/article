from PyQt5.Qt import *
from designer import ui_frame_test
from designer.ui_frame_test import Ui_MainWindow
from designer.one import Ui_MainWindow1
from designer.two import Ui_MainWindow2
import sys


class Test(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.www = ui_frame_test.Ui_MainWindow()

        self.www.setupUi(self)

        self.Stack = self.www.stackedWidget

        # one1 = Ui_MainWindow1()
        # two1 = Ui_MainWindow2()
        #
        # self.qsl.addWidget(one1)
        # self.qsl.addWidget(two1)

        self.leftlist = QListWidget()
        self.leftlist.insertItem(0, "联系方式")
        self.leftlist.insertItem(1, "个人信息")
        self.leftlist.insertItem(2, "教育程度")
        self.stack1 = QWidget()
        self.stack2 = QWidget()
        self.stack3 = QWidget()
        self.stack1UI()
        self.stack2UI()
        self.stack3UI()
        # self.Stack = QStackedWidget(self)
        self.Stack.addWidget(self.stack1)
        self.Stack.addWidget(self.stack2)
        self.Stack.addWidget(self.stack3)
        hbox = QHBoxLayout(self)
        hbox.addWidget(self.leftlist)
        hbox.addWidget(self.Stack)
        self.setLayout(hbox)
        self.leftlist.currentRowChanged.connect(self.display)

    def stack1UI(self):
        layout = QFormLayout()
        layout.addRow("姓名", QLineEdit())
        layout.addRow("地址", QLineEdit())
        self.stack1.setLayout(layout)

    def stack2UI(self):
        layout = QFormLayout()
        sex = QHBoxLayout()
        sex.addWidget(QRadioButton("男"))
        sex.addWidget(QRadioButton("女"))
        layout.addRow(QLabel("性别"), sex)
        layout.addRow("生日", QLineEdit())
        self.stack2.setLayout(layout)

    def stack3UI(self):
        layout = QHBoxLayout()
        layout.addWidget(QLabel("科目"))
        layout.addWidget(QCheckBox("物理"))
        layout.addWidget(QCheckBox("高数"))
        self.stack3.setLayout(layout)

    def display(self, i):
        self.Stack.setCurrentIndex(i)


    def show_panel(self):
        dic = {
            "pushButton_1": 0,
            "pushButton_2": 1,
        }
        index = dic[self.sender().objectName()]
        self.qsl.setCurrentIndex(index)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Test()
    win.show()
    sys.exit(app.exec_())
