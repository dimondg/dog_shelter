# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin_add_dog_window_designer.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AdminAddDogWindow(object):
    def setupUi(self, AdminAddDogWindow):
        AdminAddDogWindow.setObjectName("AdminAddDogWindow")
        AdminAddDogWindow.resize(571, 248)
        AdminAddDogWindow.setStyleSheet("background-color: rgb(232, 232, 174)")
        self.centralwidget = QtWidgets.QWidget(AdminAddDogWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_breed = QtWidgets.QLabel(self.centralwidget)
        self.lbl_breed.setGeometry(QtCore.QRect(20, 20, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_breed.setFont(font)
        self.lbl_breed.setFrameShape(QtWidgets.QFrame.Panel)
        self.lbl_breed.setObjectName("lbl_breed")
        self.lbl_gender = QtWidgets.QLabel(self.centralwidget)
        self.lbl_gender.setGeometry(QtCore.QRect(150, 20, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_gender.setFont(font)
        self.lbl_gender.setFrameShape(QtWidgets.QFrame.Panel)
        self.lbl_gender.setObjectName("lbl_gender")
        self.lbl_filename = QtWidgets.QLabel(self.centralwidget)
        self.lbl_filename.setGeometry(QtCore.QRect(250, 20, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_filename.setFont(font)
        self.lbl_filename.setFrameShape(QtWidgets.QFrame.Panel)
        self.lbl_filename.setObjectName("lbl_filename")
        self.breed_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.breed_edit.setGeometry(QtCore.QRect(20, 70, 91, 31))
        self.breed_edit.setObjectName("breed_edit")
        self.gender_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.gender_edit.setGeometry(QtCore.QRect(150, 70, 61, 31))
        self.gender_edit.setObjectName("gender_edit")
        self.filename_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.filename_edit.setGeometry(QtCore.QRect(250, 70, 311, 31))
        self.filename_edit.setObjectName("filename_edit")
        self.v_line_right = QtWidgets.QFrame(self.centralwidget)
        self.v_line_right.setGeometry(QtCore.QRect(220, 10, 20, 101))
        self.v_line_right.setFrameShadow(QtWidgets.QFrame.Raised)
        self.v_line_right.setFrameShape(QtWidgets.QFrame.VLine)
        self.v_line_right.setObjectName("v_line_right")
        self.v_line_left = QtWidgets.QFrame(self.centralwidget)
        self.v_line_left.setGeometry(QtCore.QRect(120, 10, 20, 101))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.v_line_left.setFont(font)
        self.v_line_left.setFrameShadow(QtWidgets.QFrame.Raised)
        self.v_line_left.setFrameShape(QtWidgets.QFrame.VLine)
        self.v_line_left.setObjectName("v_line_left")
        self.h_line_top = QtWidgets.QFrame(self.centralwidget)
        self.h_line_top.setGeometry(QtCore.QRect(0, 0, 581, 20))
        self.h_line_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.h_line_top.setFrameShape(QtWidgets.QFrame.HLine)
        self.h_line_top.setObjectName("h_line_top")
        self.h_line_bottom = QtWidgets.QFrame(self.centralwidget)
        self.h_line_bottom.setGeometry(QtCore.QRect(0, 110, 581, 20))
        self.h_line_bottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.h_line_bottom.setFrameShape(QtWidgets.QFrame.HLine)
        self.h_line_bottom.setObjectName("h_line_bottom")
        self.btn_add = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add.setGeometry(QtCore.QRect(390, 170, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_add.setFont(font)
        self.btn_add.setStyleSheet("background-color: rgb(220, 220, 160)")
        self.btn_add.setObjectName("btn_add")
        self.btn_file = QtWidgets.QPushButton(self.centralwidget)
        self.btn_file.setGeometry(QtCore.QRect(20, 170, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.btn_file.setFont(font)
        self.btn_file.setStyleSheet("background-color: rgb(220, 220, 160)")
        self.btn_file.setObjectName("btn_file")
        self.lbl_error = QtWidgets.QLabel(self.centralwidget)
        self.lbl_error.setGeometry(QtCore.QRect(30, 129, 511, 31))
        self.lbl_error.setText("")
        self.lbl_error.setObjectName("lbl_error")
        AdminAddDogWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AdminAddDogWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 571, 26))
        self.menubar.setObjectName("menubar")
        AdminAddDogWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AdminAddDogWindow)
        self.statusbar.setObjectName("statusbar")
        AdminAddDogWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AdminAddDogWindow)
        QtCore.QMetaObject.connectSlotsByName(AdminAddDogWindow)

    def retranslateUi(self, AdminAddDogWindow):
        _translate = QtCore.QCoreApplication.translate
        AdminAddDogWindow.setWindowTitle(_translate("AdminAddDogWindow", "MainWindow"))
        self.lbl_breed.setText(_translate("AdminAddDogWindow", "????????????:"))
        self.lbl_gender.setText(_translate("AdminAddDogWindow", "??????:"))
        self.lbl_filename.setText(_translate("AdminAddDogWindow", "?????? ?????????? ?? ?????????????????? ????????????:"))
        self.btn_add.setText(_translate("AdminAddDogWindow", "????????????????"))
        self.btn_file.setText(_translate("AdminAddDogWindow", "???????????????? ???????? ?? ??????????????????"))
