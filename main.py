import sys

import sqlite3

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPixmap
from dog_shelter_designer import Ui_MainWindow
from dog_shelter_second_form_designer import Ui_SecondWindow
from PyQt5.QtWidgets import QApplication


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_search.clicked.connect(self.search)
        self.second_window = SecondWidget()

    def search(self):
        self.gender = self.gender_edit.text()
        self.breed = self.breed_edit.text()
        con = sqlite3.connect("dog_shelter_db")
        cur = con.cursor()
        file_name = cur.execute("""SELECT
            dog_image_file_name FROM dogs WHERE
            gender == :gender AND breed_id == (SELECT id FROM breeds WHERE
            breed == :breed)
        """, {'gender': self.gender, 'breed': self.breed}).fetchall()
        con.close()
        self.second_window.pixmap = QPixmap(f"images\{file_name}.jpg")
        self.second_window.image_lbl.setPixmap(self.second_window.pixmap)
        self.second_window.show()


class SecondWidget(QMainWindow, Ui_SecondWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_back.clicked.connect(self.back)

    def back(self):
        self.hide()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyWidget()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())