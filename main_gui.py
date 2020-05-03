from PyQt5 import QtCore, QtGui, QtWidgets
from Gui.info import Ui_Info

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(686, 382)
        MainWindow.setMaximumSize(QtCore.QSize(686, 16777215))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.generateButton = QtWidgets.QPushButton(self.centralwidget)
        self.generateButton.setGeometry(QtCore.QRect(290, 180, 101, 31))
        self.generateButton.setObjectName("generateButton")
        self.generateButton.clicked.connect(self.run)
        
        self.inputAddress = QtWidgets.QLineEdit(self.centralwidget)
        self.inputAddress.setGeometry(QtCore.QRect(220, 150, 251, 20))
        self.inputAddress.setObjectName("inputAddress")
        
        self.labelAddress = QtWidgets.QLabel(self.centralwidget)
        self.labelAddress.setGeometry(QtCore.QRect(120, 100, 481, 41))
        self.labelAddress.setObjectName("labelAddress")
        
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(217, 230, 291, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.hide()
        
        
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
        self.actionInformacje.triggered['bool'].connect(self.display) 
        
        self.actionZamknij = QtWidgets.QAction(MainWindow)
        self.actionZamknij.setObjectName("actionZamknij")
        self.menuProgram.addAction(self.actionZamknij)
        self.actionZamknij.triggered['bool'].connect(MainWindow.close)
        
        self.menubar.addAction(self.menuProgram.menuAction())
        self.retranslateUi(MainWindow)
        
       
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def display(self):
        Info = QtWidgets.QDialog()
        MainWindow.hide()
        ui = Ui_Info()
        ui.setupUi(Info)
        Info.show()
        Info.exec_()
        MainWindow.show()
          
    def run(self):
        inputValue = self.inputAddress.text() # pobieranie wartości z input address
        self.labelAddress.setText(inputValue)
        self.completed = 0
        self.progressBar.show()
        
        self.generateButton.setEnabled(False)
        while self.completed < 100:
            self.completed += 0.00001
            self.progressBar.setValue(self.completed)
        self.generateButton.setEnabled(True)
        self.progressBar.hide()
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.generateButton.setStatusTip(_translate("MainWindow", "Rozpocznij generowanie raportu"))
        self.generateButton.setText(_translate("MainWindow", "Generuj raport"))
        self.inputAddress.setStatusTip(_translate("MainWindow", "Wprowadź adres witryny internetowej, aby uzyskać informacje"))
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
