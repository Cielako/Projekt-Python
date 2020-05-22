#from Modules.iplook import iplook
#from Modules.geolocation import geolocation

#for x,y in geolocation("wp.pl").items():# test geolokalizacji
    #print(f"{x} : {y}")
    
#try:
    #import subprocess
    #subprocess.Popen(['temp.pdf'],shell=True)

import webbrowser
import os
import sys
from PyQt5.QtWidgets import QFileDialog
webbrowser.open('file://' + os.path.realpath('temp.pdf'))
def file_save(self):
        name = QtWidgets.QFileDialog.getSaveFileName(MainWindow, "Save File", '/', '.txt')
        file = open(name,'w')
        text = self.textEdit.toPlainText()
        file.write(text)
        file.close()