from PyQt5.QtWidgets import QMainWindow
from designers.change_designer import Ui_ChangeWindow
from add_dog_window import AddDogWidget
from add_breed_window import AddBreedWidget


class AdminChangeWidget(QMainWindow, Ui_ChangeWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("change")
        self.btn_back.clicked.connect(self.back)
        self.btn_next.clicked.connect(self.next)

    def back(self):
        self.hide()

    def next(self):
        text = self.cb_change.currentText()
        if text == "Добавить собаку":
            self.add_dog()
        elif text == "Добавить новую породу":
            self.add_breed()

    def add_dog(self):
        self.add_dog_window = AddDogWidget()
        self.add_dog_window.show()
        self.hide()

    def add_breed(self):
        self.add_breed_window = AddBreedWidget()
        self.add_breed_window.show()
        self.hide()
