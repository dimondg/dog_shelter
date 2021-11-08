from PyQt5.QtWidgets import QMainWindow

from designers.dog_shelter_choose_form_designer import Ui_SecondWindow
from result_window import ResultWindow
from PyQt5.QtGui import QPixmap


class SecondWidget(QMainWindow, Ui_SecondWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("choose")
        self.btn_back_to_main_menu.clicked.connect(self.back_to_main_menu)
        self.btn_choose.clicked.connect(self.choose)
        self.btn_next.clicked.connect(self.next)
        self.dog_number = 1  # изменение номера собаки на 1, то есть теперь
        # это номер второй собаки, тк первую мы вывели еще до перехода в это окно

    def back_to_main_menu(self):
        self.hide()

    def next(self):
        print(self.selected_dogs_file_names)
        if len(self.selected_dogs_file_names) == 1:  # Изменение значения номера собаки на 0
            self.dog_number = 0  # если есть всего одна подходящая собака
        self.pixmap = QPixmap(f"images\{self.selected_dogs_file_names[self.dog_number][0]}.png")
        # отображение следующей из подходящих собак, если есть всего одна такая собака,
        # то выводится та же картинка
        self.image_lbl.setPixmap(self.pixmap)
        self.dog_number += 1

        if self.dog_number > len(self.selected_dogs_file_names) - 1:  # перезапуск очереди
            self.dog_number = 0  # из подходящих собак

    def choose(self):
        self.res = ResultWindow()
        self.hide()
        self.res.show()
