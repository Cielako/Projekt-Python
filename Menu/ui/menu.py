# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


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
        self.test.setGeometry(QtCore.QRect(30, 230, 251, 51))
        self.test.setObjectName("test")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 875, 21))
        self.menubar.setObjectName("menubar")
        
        self.menuProgram = QtWidgets.QMenu(self.menubar)
        self.menuProgram.setObjectName("menuProgram")
        MainWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.actionInformacje = QtWidgets.QAction(MainWindow)
        self.actionInformacje.setObjectName("actionInformacje")
        
        self.menuProgram.addAction(self.actionInformacje)
        self.menubar.addAction(self.menuProgram.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        MainWindow.setStatusTip(_translate("MainWindow", "Informacje o programie"))
        self.labelAddress.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Podaj adres witryny internetowej:</span></p></body></html>"))
        self.generateButton.setText(_translate("MainWindow", "Generuj raport"))
        self.test.setText(_translate("MainWindow", "TEST"))
        self.menuProgram.setTitle(_translate("MainWindow", "Program"))
        self.actionInformacje.setText(_translate("MainWindow", "Informacje"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
