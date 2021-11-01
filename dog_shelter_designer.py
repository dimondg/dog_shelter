# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dog_shelter_designer.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(560, 222)
        MainWindow.setStyleSheet("background-color: rgb(232, 232, 174)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 10, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 60, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(50, 100, 401, 61))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.breed_edit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.breed_edit.setObjectName("breed_edit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.breed_edit)
        self.gender_edit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.gender_edit.setObjectName("gender_edit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.gender_edit)
        self.btn_search = QtWidgets.QPushButton(self.centralwidget)
        self.btn_search.setGeometry(QtCore.QRect(460, 100, 81, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btn_search.setFont(font)
        self.btn_search.setStyleSheet("background-color: rgb(214, 214, 160)")
        self.btn_search.setObjectName("btn_search")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 70, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(214, 214, 160)")
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 560, 26))
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
        self.label.setText(_translate("MainWindow", "ПРИЮТ ДЛЯ СОБАК"))
        self.label_2.setText(_translate("MainWindow", "Искать питомца"))
        self.label_3.setText(_translate("MainWindow", "Порода:"))
        self.label_4.setText(_translate("MainWindow", "Пол:"))
        self.btn_search.setText(_translate("MainWindow", "Искать"))
        self.pushButton_2.setText(_translate("MainWindow", "Администратор"))
