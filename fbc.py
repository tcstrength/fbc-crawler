from PyQt5 import QtWidgets
from fbc.gui.MainWindow import MainWindow
from fbc.spider.Crawler import Crawler
from fbc import Driver
import sys

try:
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("fusion")
    win = MainWindow()
    win.ui.show()
    app.exec_()
    Driver.close()
except KeyboardInterrupt:
    pass

