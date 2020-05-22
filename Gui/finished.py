from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import webbrowser
import os
import shutil

class Ui_Finished_Form(object):
    def setupUi(self, Finished_Form):
        Finished_Form.setObjectName("Finished_Form")
        Finished_Form.resize(640, 308)
        Finished_Form.setMaximumSize(QtCore.QSize(686,308))
        Finished_Form.setMinimumSize(QtCore.QSize(686,308))
        
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Finished_Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        
        self.label = QtWidgets.QLabel(Finished_Form)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        
        self.viewButton = QtWidgets.QPushButton(Finished_Form)
        self.viewButton.setObjectName("viewButton")
        self.viewButton.clicked.connect(self.viewReport)
        self.horizontalLayout_2.addWidget(self.viewButton)
        
        self.saveButton = QtWidgets.QPushButton(Finished_Form)
        self.saveButton.setObjectName("saveButton")
        self.saveButton.clicked.connect(self.saveReport)
        self.horizontalLayout_2.addWidget(self.saveButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Finished_Form)
        QtCore.QMetaObject.connectSlotsByName(Finished_Form)
        
    def viewReport(self):
        webbrowser.open('file://' + os.path.realpath('temp.pdf'))
    
    def saveReport(self):
        option = QFileDialog.Options()
        Finished_Form = QtWidgets.QWidget()
        name = QtWidgets.QFileDialog.getSaveFileName(Finished_Form, "Save File", 'raport', 'Pliki PDF (*.pdf)',options=option)
        temp_report = os.path.realpath('temp.pdf')# ścieżka do pliku temp.pdf
        if len(name[0]) > 0:
            shutil.copy(temp_report,name[0])# przenoszenie, oraz zmiana nazwy pliku do wybranego miejsca na dysku
            
    def retranslateUi(self, Finished_Form):
        _translate = QtCore.QCoreApplication.translate
        Finished_Form.setWindowTitle(_translate("Form", "Zakończono"))
        Finished_Form.setStatusTip(_translate("Form", "Zapisz wygenerowany raport"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Twój raport został wygenerowany </span></p></body></html>"))
        self.viewButton.setToolTip(_translate("Form", "Obejrzyj raport"))
        self.viewButton.setText(_translate("Form", "Podejrzyj raport"))
        self.saveButton.setToolTip(_translate("Form", "Zapisz swój raport"))
        self.saveButton.setText(_translate("Form", "Zapisz raport"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Finished_Form = QtWidgets.QWidget()
    ui = Ui_Finished_Form()
    ui.setupUi(Finished_Form)
    Finished_Form.show()
    sys.exit(app.exec_())
