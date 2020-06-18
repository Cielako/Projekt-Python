from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Blad(object):
    def setupUi(self, Blad):
        Blad.setObjectName("Blad")
        Blad.resize(320, 120)
        Blad.setMinimumSize(QtCore.QSize(320, 120))
        Blad.setMaximumSize(QtCore.QSize(320, 120))
        blad_icon = QtGui.QIcon("Gui/icons/warning.png")
        Blad.setWindowIcon(blad_icon)
        #self.pushButton = QtWidgets.QPushButton(Blad)
        #self.pushButton.setGeometry(QtCore.QRect(120, 60, 75, 25))
        #self.pushButton.setObjectName("pushButton")
        #self.pushButton.clicked.connect(self.zamknijOkno)
        #self.pushButton
        self.label = QtWidgets.QLabel(Blad)
        self.label.setGeometry(QtCore.QRect(20, 20, 286, 18))
        self.label.setObjectName("label")
        self.retranslateUi(Blad)
        QtCore.QMetaObject.connectSlotsByName(Blad)

    def retranslateUi(self, Blad):
        _translate = QtCore.QCoreApplication.translate
        Blad.setWindowTitle(_translate("Blad", "Uwaga !"))
        #self.pushButton.setText(_translate("Blad", "OK"))
        self.label.setText(_translate("Blad", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Wprowadzono niepoprawny adres !</span></p></body></html>"))
        
    def zamknijOkno(self):
        Blad.close()
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Blad = QtWidgets.QDialog()
    ui = Ui_Blad()
    ui.setupUi(Blad)
    Blad.show()
    sys.exit(app.exec_())
