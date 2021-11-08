import sqlite3
import shutil

from PyQt5.QtWidgets import QMainWindow
from designers.dog_shelter_add_dog_window_designer import Ui_AdminAddDogWindow
from PyQt5.QtWidgets import QFileDialog
from convert_to_png import *


class AddDogWidget(QMainWindow, Ui_AdminAddDogWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("add")
        self.btn_add.clicked.connect(self.add)
        self.btn_file.clicked.connect(self.file)

    def add(self):
        con = sqlite3.connect("dog_shelter_db")
        cur = con.cursor()
        breed = self.breed_edit.text()
        gender = self.gender_edit.text()
        filename = self.filename_edit.text()
        breed_id = cur.execute("""SELECT id FROM breeds 
            WHERE breed == :breed""", {'breed': breed}).fetchone()[0]

        cur.execute("""INSERT INTO
            dogs(id, dog_image_file_name, breed_id, gender, is_taken)
            VALUES(15, :filename, :breed_id, :gender, "no")
            """, {'filename': filename, 'gender': gender, 'breed_id': breed_id})
        con.commit()
        con.close()
        self.hide()

    def file(self):
        filename = self.filename_edit.text()
        open(f"images\{filename}.png", "x")  # создание нового файла в images
        inp_file_name = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0]
        shutil.copy(inp_file_name, f"images\{filename}.png")  # перенос файла в images
        convert_to_png(filename)  # конвертирование файла с картинкой в png
