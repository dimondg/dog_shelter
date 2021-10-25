import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from dog_shelter_designer import Ui_MainWindow
from dog_shelter_second_form_designer import Ui_SecondWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class SecondWidget(QMainWindow, Ui_SecondWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex2 = SecondWidget()
    ex.show()
    ex2.show()
    sys.exit(app.exec_())
