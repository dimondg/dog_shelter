import sqlite3

from PyQt5.QtWidgets import QMainWindow
from designers.admin_add_breed_window_designer import Ui_AdminAddBreedWindow


class AddBreedWidget(QMainWindow, Ui_AdminAddBreedWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("add")
        self.btn_add.clicked.connect(self.add)

    def add(self):
        try:
            con = sqlite3.connect("dog_shelter_db")
            cur = con.cursor()
            breed = self.breed_edit.text()

            cur.execute("""INSERT INTO
                breeds(breed)
                VALUES(:breed)
                """, {'breed': breed})

            con.commit()
            con.close()
            self.hide()
        except sqlite3.IntegrityError:
            self.breed_edit.setText("Такая порода уже есть")
