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
        finish_icon = QtGui.QIcon("Gui/icons/finished.png")
        Finished_Form.setWindowIcon(finish_icon)
        Finished_Form.setStyleSheet("background-image: url(Gui/icons/transparent.png)")
      
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Finished_Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        
        self.finishedLabel = QtWidgets.QLabel(Finished_Form)
        self.finishedLabel.setObjectName("finishedLabel")
        self.finishedLabel.setStyleSheet("background-image: url(Gui/icons/transparent1.png); background: qradialgradient(cx: 0.2, cy: -0.8,fx: 0.1, fy: -0.3, radius: 1.35, stop: 0 #fff, stop: 1 #eee); border-radius: 10px;")
        self.verticalLayout_2.addWidget(self.finishedLabel)
        
        self.viewButton = QtWidgets.QPushButton(Finished_Form)
        self.viewButton.setObjectName("viewButton")
        self.viewButton.setStyleSheet("QPushButton {\n"
        "color: black;\n"
        "border: 2px solid black;\n"
        "border-radius: 11px;\n"
        "padding: 5px;\n"
        "background: qradialgradient(cx: 0.3, cy: -0.4,fx: 0.3, fy: -0.4, radius: 1.35, stop: 0 #fff, stop: 1 #888);\n"
        " }"
        "QPushButton:hover {"
            "background: qradialgradient(cx: 0.3, cy: -0.4,fx: 0.3, fy: -0.4,radius: 1.35, stop: 0 #fff, stop: 1 #bbb);}")
        self.viewButton.clicked.connect(self.viewReport)
        self.horizontalLayout_2.addWidget(self.viewButton)
        
        self.saveButton = QtWidgets.QPushButton(Finished_Form)
        self.saveButton.setObjectName("saveButton")
        self.saveButton.setStyleSheet("QPushButton {\n"
        "color: black;\n"
        "border: 2px solid black;\n"
        "border-radius: 11px;\n"
        "padding: 5px;\n"
        "background: qradialgradient(cx: 0.3, cy: -0.4,fx: 0.3, fy: -0.4, radius: 1.35, stop: 0 #fff, stop: 1 #888);\n"
        " }"
        "QPushButton:hover {"
            "background: qradialgradient(cx: 0.3, cy: -0.4,fx: 0.3, fy: -0.4,radius: 1.35, stop: 0 #fff, stop: 1 #bbb);}")
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
        self.finishedLabel.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Twój raport został wygenerowany </span></p></body></html>"))
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
