from PyQt5.QtWidgets import QMainWindow
from designers.dog_shelter_result_window import Ui_ResultWindow


class ResultWindow(QMainWindow, Ui_ResultWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("thank you")