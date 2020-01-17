import sys
from PyQt5.QtWidgets import QHBoxLayout, QMainWindow, QApplication, QPushButton, QWidget


def on_click():
    print('s')



q_application = QApplication(sys.argv)
q_widget = QWidget()
button = QPushButton(q_widget)
button.clicked.connect(on_click)
button.move(200, 100)

q_widget.resize(300, 200)

q_widget.show()

sys.exit(q_application.exec_())
