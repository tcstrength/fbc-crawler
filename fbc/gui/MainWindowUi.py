from PyQt5 import uic, QtWidgets

class Ui(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("qtui/mainwindow.ui", self)
        self.tblw_posts = self.findChild(QtWidgets.QTableWidget, "tblw_posts")
        header = self.tblw_posts.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.btn_delete = self.findChild(QtWidgets.QPushButton, "btn_delete")
        self.btn_start = self.findChild(QtWidgets.QPushButton, "btn_start")
        self.btn_add = self.findChild(QtWidgets.QPushButton, "btn_add")
        self.lbl_status = self.findChild(QtWidgets.QLabel, "lbl_status")
        self.lbl_wcount = self.findChild(QtWidgets.QLabel, "lbl_wcount")
        self.cb_hide_browser = self.findChild(QtWidgets.QCheckBox, "cb_hide_browser")

    def enable(self, flag):
        self.btn_add.setEnabled(flag)
        self.btn_delete.setEnabled(flag)
        self.tblw_posts.setEnabled(flag)
        self.cb_hide_browser.setEnabled(flag)

    def remove_contain_str(self, str):
        row_count = self.tblw_posts.rowCount()
        for row in range(row_count):
            post = self.tblw_posts.item(row, 0).text()
            if (str in post):
                self.tblw_posts.removeRow(row)
                return