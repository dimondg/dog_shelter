from PyQt5.QtWidgets import QMainWindow
from designers.admin_password_window_designer import Ui_AdminWindow
from windows.admin_change_window import AdminChangeWidget
from functions.authorization import *


class AdminPasswordWidget(QMainWindow, Ui_AdminWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("password")
        self.btn_next.clicked.connect(self.next)
        self.btn_back.clicked.connect(self.back)
        self.admin_change_window = AdminChangeWidget()

    def next(self):
        is_true = authorization(self.password_edit.text())
        if is_true:
            self.admin_change_window.show()
        else:
            self.password_edit.setText("Неверный пароль")

    def back(self):
        self.hide()
