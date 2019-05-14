#This file will run the application
from DokkanGUI import Window
import sys
from PyQt5 import QtWidgets,QtGui

app = QtWidgets.QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())
