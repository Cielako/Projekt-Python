from PyQt5 import (QtCore, QtGui, QtWidgets)
from Gui.info import Ui_Info
from Gui.finished import Ui_Finished_Form
from Gui.komunikat import Ui_Blad
from Modules.is_online import is_online
from pdfcreate import pdfcreate
from PyQt5.QtWidgets import QFileDialog

import urllib.request

#Główny kod uruchamiający cały program 
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(686, 382)
        MainWindow.setMaximumSize(QtCore.QSize(686,382))
        MainWindow.setMinimumSize(QtCore.QSize(686,382))
        main_icon = QtGui.QIcon("Gui/icons/main.png")
        MainWindow.setWindowIcon(main_icon)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-image: url(Gui/icons/transparent.png)")
        
        self.generateButton = QtWidgets.QPushButton(self.centralwidget)
        self.generateButton.setGeometry(QtCore.QRect(290, 180, 101, 31))
        self.generateButton.setObjectName("generateButton")
        self.generateButton.setStyleSheet("QPushButton {\n"
        "color: black;\n"
        "border: 2px solid black;\n"
        "border-radius: 11px;\n"
        "padding: 5px;\n"
        "background: qradialgradient(cx: 0.3, cy: -0.4,fx: 0.3, fy: -0.4, radius: 1.35, stop: 0 #fff, stop: 1 #888);\n"
        " }"
        "QPushButton:hover {"
            "background: qradialgradient(cx: 0.3, cy: -0.4,fx: 0.3, fy: -0.4,radius: 1.35, stop: 0 #fff, stop: 1 #bbb);}")
        self.generateButton.clicked.connect(self.run)
        
        self.inputAddress = QtWidgets.QLineEdit(self.centralwidget)
        self.inputAddress.setGeometry(QtCore.QRect(220, 150, 251, 20))
        self.inputAddress.setObjectName("inputAddress")
        self.inputAddress.setStyleSheet("border-radius:10px; border: 2px solid black;background-image: url(Gui/icons/transparent1.png); font-weight: bold;")
        
        self.labelAddress = QtWidgets.QLabel(self.centralwidget)
        self.labelAddress.setGeometry(QtCore.QRect(105, 100, 481, 41))
        self.labelAddress.setObjectName("labelAddress")
        self.labelAddress.setStyleSheet("background-image: url(Gui/icons/transparent1.png); background: qradialgradient(cx: 0.2, cy: -0.8,fx: 0.1, fy: -0.3, radius: 1.35, stop: 0 #fff, stop: 1 #eee); border-radius: 10px;")
    
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(217, 230, 291, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.close()
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 686, 21))
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
        self.actionInformacje.triggered['bool'].connect(self.displayAbout) 
        
        self.actionZamknij = QtWidgets.QAction(MainWindow)
        self.actionZamknij.setObjectName("actionZamknij")
        self.menuProgram.addAction(self.actionZamknij)
        self.actionZamknij.triggered['bool'].connect(MainWindow.close)
        
        self.menubar.addAction(self.menuProgram.menuAction())
        self.retranslateUi(MainWindow)
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def displayAbout(self):# Okno Informacje o programie
        Info = QtWidgets.QDialog()
        MainWindow.hide()
        ui = Ui_Info()
        ui.setupUi(Info)
        Info.show()
        Info.exec_()
        MainWindow.show()

    def finishedReport(self):# Komunikat o zakończeniu generowania raportu
        Finish = QtWidgets.QDialog()
        MainWindow.hide()
        ui = Ui_Finished_Form()
        ui.setupUi(Finish)
        Finish.show()
        Finish.exec_()
        MainWindow.show()
        return Finish
    
    def komunikatBlad(self):
        Komunikat = QtWidgets.QDialog()
        MainWindow.hide()
        ui = Ui_Blad()
        ui.setupUi(Komunikat)
        Komunikat.show()
        Komunikat.exec_()
        MainWindow.show()
        return Komunikat
                    
    def run(self):# Uruchom główne funkcje programu
        inputValue = self.inputAddress.text() # pobieranie wartości z input address
        #self.labelAddress.setText(inputValue)
        if inputValue is not "":
            try:
                urllib.request.urlopen("http://" + inputValue)
            except:
                MainWindow.close()
                self.komunikatBlad()
                MainWindow.show()
            else:
                inputValue = self.inputAddress.text()
                self.completed = 0
                self.progressBar.show()
                self.generateButton.setEnabled(False)
                pdfcreate(inputValue)
                while self.completed < 100:
                    self.completed += 0.0001
                    self.progressBar.setValue(self.completed)
                self.generateButton.setEnabled(True)
                self.finishedReport()
                self.progressBar.close()
        else:
            self.komunikatBlad()
        #self.generateButton.clicked.connect(self.finishedReport)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "IPSI"))
        self.generateButton.setToolTip(_translate("MainWindow", "Rozpocznij generowanie raportu"))
        self.generateButton.setText(_translate("MainWindow", "Generuj raport"))
        self.inputAddress.setToolTip(_translate("MainWindow", "Wprowadź adres witryny internetowej, aby uzyskać informacje"))
        self.labelAddress.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; font-family:Comic Sans Ms; font-style:italic;\">Wprowadź adres witryny internetowej</span></p></body></html>"))
        self.menuProgram.setTitle(_translate("MainWindow", "Program"))
        self.actionInformacje.setText(_translate("MainWindow", "Informacje"))
        self.actionZamknij.setText(_translate("MainWindow", "Zamknij"))
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
