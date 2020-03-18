from PyQt5 import uic, QtWidgets

class Ui(QtWidgets.QDialog):

    def __init__(self):
        super().__init__()
        uic.loadUi("qtui/msgbox.ui", self)
        self.lbl_title = self.findChild(QtWidgets.QLabel, "lbl_title")
        self.lbl_detail = self.findChild(QtWidgets.QLabel, "lbl_detail")