# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin_add_breed_window_designer.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AdminAddBreedWindow(object):
    def setupUi(self, AdminAddBreedWindow):
        AdminAddBreedWindow.setObjectName("AdminAddBreedWindow")
        AdminAddBreedWindow.resize(534, 140)
        AdminAddBreedWindow.setStyleSheet("background-color: rgb(232, 232, 174)")
        self.centralwidget = QtWidgets.QWidget(AdminAddBreedWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.breed_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.breed_edit.setGeometry(QtCore.QRect(40, 40, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.breed_edit.setFont(font)
        self.breed_edit.setText("")
        self.breed_edit.setObjectName("breed_edit")
        self.btn_add = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add.setGeometry(QtCore.QRect(370, 30, 121, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_add.setFont(font)
        self.btn_add.setStyleSheet("background-color: rgb(220, 220, 160)")
        self.btn_add.setObjectName("btn_add")
        AdminAddBreedWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AdminAddBreedWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 534, 26))
        self.menubar.setObjectName("menubar")
        AdminAddBreedWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AdminAddBreedWindow)
        self.statusbar.setObjectName("statusbar")
        AdminAddBreedWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AdminAddBreedWindow)
        QtCore.QMetaObject.connectSlotsByName(AdminAddBreedWindow)

    def retranslateUi(self, AdminAddBreedWindow):
        _translate = QtCore.QCoreApplication.translate
        AdminAddBreedWindow.setWindowTitle(_translate("AdminAddBreedWindow", "MainWindow"))
        self.btn_add.setText(_translate("AdminAddBreedWindow", "Добавить"))
