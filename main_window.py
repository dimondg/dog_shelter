import sqlite3

from PyQt5.QtWidgets import QMainWindow
from dog_shelter_designer import Ui_MainWindow
from choose_window import SecondWidget
from admin_password_window import AdminPasswordWidget
from PyQt5.QtGui import QPixmap


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("dog shelter")
        self.btn_search.clicked.connect(self.search)
        self.btn_admin.clicked.connect(self.admin)
        self.choose_window = SecondWidget()

    def search(self):
        self.gender = self.gender_edit.text()
        self.breed = self.breed_edit.text()

        con = sqlite3.connect("dog_shelter_db")
        cur = con.cursor()
        file_names = cur.execute("""SELECT
            dog_image_file_name FROM dogs WHERE
            gender == :gender AND breed_id == (SELECT id FROM breeds WHERE
            breed == :breed)
        """, {'gender': self.gender, 'breed': self.breed}).fetchall()
        con.close()

        self.choose_window.dog_number = 1
        self.choose_window.selected_dogs_file_names = file_names
        first_picture_file_name = file_names[0][0]  # имя файла с картинкой перво из подходящих собак
        self.choose_window.pixmap = QPixmap(f"images\{first_picture_file_name}.png")
        self.choose_window.image_lbl.setPixmap(self.choose_window.pixmap)
        self.choose_window.show()

    def admin(self):
        self.admin_window = AdminPasswordWidget()
        self.admin_window.btn_back.clicked.connect(self.back)
        self.hide()
        self.admin_window.show()

    def back(self):
        self.admin_window.hide()
        self.show()
