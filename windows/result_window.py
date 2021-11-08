from PyQt5.QtWidgets import QMainWindow
from designers.result_window_designer import Ui_ResultWindow


class ResultWindow(QMainWindow, Ui_ResultWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("thank you")