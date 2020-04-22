# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Modules.iplook import iplook

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(875, 388)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.labelAddress = QtWidgets.QLabel(self.centralwidget)
        self.labelAddress.setGeometry(QtCore.QRect(240, 80, 331, 31))
        self.labelAddress.setObjectName("labelAddress")
        
        self.inputAddress = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.inputAddress.setGeometry(QtCore.QRect(240, 120, 321, 31))
        self.inputAddress.setObjectName("inputAddress")
        
        self.generateButton = QtWidgets.QPushButton(self.centralwidget)
        self.generateButton.setGeometry(QtCore.QRect(340, 170, 121, 31))
        self.generateButton.setObjectName("generateButton")
        
        self.test = QtWidgets.QLabel(self.centralwidget)
        self.test.setGeometry(QtCore.QRect(70, 260, 251, 51))
        self.test.setObjectName("test")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 875, 21))
        self.menubar.setObjectName("menubar")
        
        self.menuO_programie = QtWidgets.QMenu(self.menubar)
        self.menuO_programie.setObjectName("menuO_programie")
        
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuO_programie.menuAction())

        self.generateButton.clicked.connect(self.clicked)# zmiana nazwy etykiety na inną
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        MainWindow.setStatusTip(_translate("MainWindow", "Informacje o programie"))
        self.labelAddress.setStatusTip(_translate("MainWindow", "label_address"))
        self.labelAddress.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Podaj adres witryny internetowej:</span></p></body></html>"))
        self.inputAddress.setStatusTip(_translate("MainWindow", "input_address"))
        self.generateButton.setStatusTip(_translate("MainWindow", "Generuj_raport"))
        self.generateButton.setText(_translate("MainWindow", "Generuj raport"))
        self.test.setText(_translate("MainWindow", "TEST"))
        self.menuO_programie.setTitle(_translate("MainWindow", "O programie"))

    def clicked(self):
        inputValue = self.inputAddress.toPlainText() # pobieranie wartości z input address
        iplook(inputValue)
        self.test.setText(iplook(inputValue)) # wczytanie wartości z inputa do etykiety

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
