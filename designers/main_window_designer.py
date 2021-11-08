# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window_designer.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(658, 406)
        MainWindow.setStyleSheet("background-color: rgb(232, 232, 174)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_dog_shelter = QtWidgets.QLabel(self.centralwidget)
        self.lbl_dog_shelter.setGeometry(QtCore.QRect(170, 10, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.lbl_dog_shelter.setFont(font)
        self.lbl_dog_shelter.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbl_dog_shelter.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_dog_shelter.setObjectName("lbl_dog_shelter")
        self.lbl_search = QtWidgets.QLabel(self.centralwidget)
        self.lbl_search.setGeometry(QtCore.QRect(30, 70, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setUnderline(True)
        self.lbl_search.setFont(font)
        self.lbl_search.setObjectName("lbl_search")
        self.btn_search = QtWidgets.QPushButton(self.centralwidget)
        self.btn_search.setGeometry(QtCore.QRect(400, 270, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_search.setFont(font)
        self.btn_search.setStyleSheet("background-color: rgb(220, 220, 160)")
        self.btn_search.setObjectName("btn_search")
        self.btn_admin = QtWidgets.QPushButton(self.centralwidget)
        self.btn_admin.setGeometry(QtCore.QRect(470, 80, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.btn_admin.setFont(font)
        self.btn_admin.setStyleSheet("background-color: rgb(220, 220, 160)")
        self.btn_admin.setObjectName("btn_admin")
        self.lbl_gender = QtWidgets.QLabel(self.centralwidget)
        self.lbl_gender.setGeometry(QtCore.QRect(70, 190, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_gender.setFont(font)
        self.lbl_gender.setObjectName("lbl_gender")
        self.lbl_breed = QtWidgets.QLabel(self.centralwidget)
        self.lbl_breed.setGeometry(QtCore.QRect(30, 130, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_breed.setFont(font)
        self.lbl_breed.setObjectName("lbl_breed")
        self.breed_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.breed_edit.setGeometry(QtCore.QRect(130, 140, 442, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.breed_edit.setFont(font)
        self.breed_edit.setObjectName("breed_edit")
        self.gender_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.gender_edit.setGeometry(QtCore.QRect(130, 190, 442, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.gender_edit.setFont(font)
        self.gender_edit.setObjectName("gender_edit")
        self.lbl_error = QtWidgets.QLabel(self.centralwidget)
        self.lbl_error.setGeometry(QtCore.QRect(40, 270, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbl_error.setFont(font)
        self.lbl_error.setText("")
        self.lbl_error.setObjectName("lbl_error")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 658, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbl_dog_shelter.setText(_translate("MainWindow", "ПРИЮТ ДЛЯ СОБАК"))
        self.lbl_search.setText(_translate("MainWindow", "Искать питомца"))
        self.btn_search.setText(_translate("MainWindow", "Искать"))
        self.btn_admin.setText(_translate("MainWindow", "Администратор"))
        self.lbl_gender.setText(_translate("MainWindow", "Пол:"))
        self.lbl_breed.setText(_translate("MainWindow", "Порода:"))
