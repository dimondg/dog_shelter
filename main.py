import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap
from dog_shelter_designer import Ui_MainWindow
from dog_shelter_second_form_designer import Ui_SecondWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_search.clicked.connect(self.search)

    def search(self):
        self.second_window = SecondWidget()
        self.setupUi(self)
        self.second_window.pixmap = QPixmap("dog.jpg")
        self.second_window.image_lbl.setPixmap(self.second_window.pixmap)
        self.second_window.show()


class SecondWidget(QMainWindow, Ui_SecondWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pixmap = QPixmap("dog.jpg")
        self.image_lbl.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())