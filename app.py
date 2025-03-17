import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(0,0,1200,800)
    win.setWindowTitle("Pilgrims Broadway Complex")
    win.setWindowIcon(QIcon("Chicken.png"))
    win.show()
    sys.exit(app.exec_())

window()