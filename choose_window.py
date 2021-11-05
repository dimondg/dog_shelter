from PyQt5.QtWidgets import QMainWindow
from dog_shelter_designer import Ui_MainWindow
from dog_shelter_choose_form_designer import Ui_SecondWindow
from PyQt5.QtGui import QPixmap


class SecondWidget(QMainWindow, Ui_SecondWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("choose")
        self.btn_back_to_main_menu.clicked.connect(self.back_to_main_menu)
        self.btn_next.clicked.connect(self.next)
        self.dog_number = 1

    def back_to_main_menu(self):
        self.hide()

    def next(self):
        if self.dog_number > len(self.selected_dogs_file_names) - 1:
            self.dog_number = 0
        self.pixmap = QPixmap(f"images\{self.selected_dogs_file_names[self.dog_number]}.png")
        self.image_lbl.setPixmap(self.pixmap)
        self.dog_number += 1
