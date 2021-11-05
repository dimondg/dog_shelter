from PyQt5.QtWidgets import QMainWindow
from dog_shelter_admin_change_window import Ui_AdminChangeWindow


class AdminChangeWidget(QMainWindow, Ui_AdminChangeWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("change")

    def add_dog(self):
        pass

    def add_breed(self):
        pass
