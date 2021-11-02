import sqlite3

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPixmap
from dog_shelter_designer import Ui_MainWindow
from choose_window import SecondWidget


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("dog shelter")
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

        print(file_name)
        self.second_window.pixmap = QPixmap(f"images\{file_name[0][0]}.png")
        self.second_window.image_lbl.setPixmap(self.second_window.pixmap)
        self.second_window.show()

