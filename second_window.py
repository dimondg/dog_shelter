import sqlite3

from PyQt5.QtWidgets import QMainWindow
from dog_shelter_designer import Ui_MainWindow
from dog_shelter_second_form_designer import Ui_SecondWindow


class SecondWidget(QMainWindow, Ui_SecondWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_back.clicked.connect(self.back)

    def back(self):
        self.hide()
