# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dog_shelter_choose_form_designer.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SecondWindow(object):
    def setupUi(self, SecondWindow):
        SecondWindow.setObjectName("SecondWindow")
        SecondWindow.resize(729, 545)
        SecondWindow.setStyleSheet("background-color: rgb(232, 232, 174)")
        self.centralwidget = QtWidgets.QWidget(SecondWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.image_lbl = QtWidgets.QLabel(self.centralwidget)
        self.image_lbl.setGeometry(QtCore.QRect(50, 20, 631, 411))
        self.image_lbl.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.image_lbl.setText("")
        self.image_lbl.setObjectName("image_lbl")
        self.btn_next = QtWidgets.QPushButton(self.centralwidget)
        self.btn_next.setGeometry(QtCore.QRect(500, 450, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_next.setFont(font)
        self.btn_next.setStyleSheet("background-color: rgb(214, 214, 160)")
        self.btn_next.setObjectName("btn_next")
        self.btn_choose = QtWidgets.QPushButton(self.centralwidget)
        self.btn_choose.setGeometry(QtCore.QRect(270, 450, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_choose.setFont(font)
        self.btn_choose.setStyleSheet("background-color: rgb(214, 214, 160)")
        self.btn_choose.setObjectName("btn_choose")
        self.btn_back_to_main_menu = QtWidgets.QPushButton(self.centralwidget)
        self.btn_back_to_main_menu.setGeometry(QtCore.QRect(50, 450, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_back_to_main_menu.setFont(font)
        self.btn_back_to_main_menu.setStyleSheet("background-color: rgb(214, 214, 160)")
        self.btn_back_to_main_menu.setObjectName("btn_back_to_main_menu")
        SecondWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SecondWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 729, 26))
        self.menubar.setObjectName("menubar")
        SecondWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SecondWindow)
        self.statusbar.setObjectName("statusbar")
        SecondWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SecondWindow)
        QtCore.QMetaObject.connectSlotsByName(SecondWindow)

    def retranslateUi(self, SecondWindow):
        _translate = QtCore.QCoreApplication.translate
        SecondWindow.setWindowTitle(_translate("SecondWindow", "MainWindow"))
        self.btn_next.setText(_translate("SecondWindow", "Далее"))
        self.btn_choose.setText(_translate("SecondWindow", "Выбрать"))
        self.btn_back_to_main_menu.setText(_translate("SecondWindow", "Главное меню"))
