<<<<<<< HEAD
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin_change_window_designer.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ChangeWindow(object):
    def setupUi(self, ChangeWindow):
        ChangeWindow.setObjectName("ChangeWindow")
        ChangeWindow.resize(453, 158)
        ChangeWindow.setStyleSheet("background-color: rgb(232, 232, 174)")
        self.centralwidget = QtWidgets.QWidget(ChangeWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.cb_change = QtWidgets.QComboBox(self.centralwidget)
        self.cb_change.setGeometry(QtCore.QRect(30, 20, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cb_change.setFont(font)
        self.cb_change.setObjectName("cb_change")
        self.cb_change.addItem("")
        self.cb_change.addItem("")
        self.cb_change.addItem("")
        self.btn_next = QtWidgets.QPushButton(self.centralwidget)
        self.btn_next.setGeometry(QtCore.QRect(270, 80, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_next.setFont(font)
        self.btn_next.setStyleSheet("background-color: rgb(220, 220, 160)")
        self.btn_next.setObjectName("btn_next")
        self.btn_back = QtWidgets.QPushButton(self.centralwidget)
        self.btn_back.setGeometry(QtCore.QRect(40, 80, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_back.setFont(font)
        self.btn_back.setStyleSheet("background-color: rgb(220, 220, 160)")
        self.btn_back.setObjectName("btn_back")
        ChangeWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ChangeWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 453, 26))
        self.menubar.setObjectName("menubar")
        ChangeWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ChangeWindow)
        self.statusbar.setObjectName("statusbar")
        ChangeWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ChangeWindow)
        QtCore.QMetaObject.connectSlotsByName(ChangeWindow)

    def retranslateUi(self, ChangeWindow):
        _translate = QtCore.QCoreApplication.translate
        ChangeWindow.setWindowTitle(_translate("ChangeWindow", "MainWindow"))
        self.cb_change.setCurrentText(_translate("ChangeWindow", "Выбрать"))
        self.cb_change.setItemText(0, _translate("ChangeWindow", "Выбрать"))
        self.cb_change.setItemText(1, _translate("ChangeWindow", "Добавить собаку"))
        self.cb_change.setItemText(2, _translate("ChangeWindow", "Добавить новую породу"))
        self.btn_next.setText(_translate("ChangeWindow", "Далее"))
        self.btn_back.setText(_translate("ChangeWindow", "Назад"))
=======
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin_change_window_designer.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ChangeWindow(object):
    def setupUi(self, ChangeWindow):
        ChangeWindow.setObjectName("ChangeWindow")
        ChangeWindow.resize(453, 158)
        ChangeWindow.setStyleSheet("background-color: rgb(232, 232, 174)")
        self.centralwidget = QtWidgets.QWidget(ChangeWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.cb_change = QtWidgets.QComboBox(self.centralwidget)
        self.cb_change.setGeometry(QtCore.QRect(30, 20, 391, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cb_change.setFont(font)
        self.cb_change.setObjectName("cb_change")
        self.cb_change.addItem("")
        self.cb_change.addItem("")
        self.cb_change.addItem("")
        self.btn_next = QtWidgets.QPushButton(self.centralwidget)
        self.btn_next.setGeometry(QtCore.QRect(270, 80, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_next.setFont(font)
        self.btn_next.setStyleSheet("background-color: rgb(220, 220, 160)")
        self.btn_next.setObjectName("btn_next")
        self.btn_back = QtWidgets.QPushButton(self.centralwidget)
        self.btn_back.setGeometry(QtCore.QRect(40, 80, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.btn_back.setFont(font)
        self.btn_back.setStyleSheet("background-color: rgb(220, 220, 160)")
        self.btn_back.setObjectName("btn_back")
        ChangeWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ChangeWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 453, 26))
        self.menubar.setObjectName("menubar")
        ChangeWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ChangeWindow)
        self.statusbar.setObjectName("statusbar")
        ChangeWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ChangeWindow)
        QtCore.QMetaObject.connectSlotsByName(ChangeWindow)

    def retranslateUi(self, ChangeWindow):
        _translate = QtCore.QCoreApplication.translate
        ChangeWindow.setWindowTitle(_translate("ChangeWindow", "MainWindow"))
        self.cb_change.setCurrentText(_translate("ChangeWindow", "Выбрать"))
        self.cb_change.setItemText(0, _translate("ChangeWindow", "Выбрать"))
        self.cb_change.setItemText(1, _translate("ChangeWindow", "Добавить собаку"))
        self.cb_change.setItemText(2, _translate("ChangeWindow", "Добавить новую породу"))
        self.btn_next.setText(_translate("ChangeWindow", "Далее"))
        self.btn_back.setText(_translate("ChangeWindow", "Назад"))
>>>>>>> origin/master
