from fbc.gui.MainWindowUi import Ui
from fbc.gui.threads.TrackLogin import TrackLoginThread
from fbc.gui.threads.Crawl import CrawlThread
from fbc import Driver
from PyQt5 import QtWidgets, QtCore 

class MainWindow():
    def __init__(self):
        self.crawl_thread = CrawlThread()
        self.crawl_thread.one_crawled.connect(self.one_crawled)
        self.crawl_thread.finished.connect(self.crawl_finished)
        self.ui = Ui()
        self.ui.btn_add.clicked.connect(self.ui_btn_add_clicked)
        self.ui.btn_delete.clicked.connect(self.ui_btn_delete_clicked)
        self.ui.btn_start.clicked.connect(self.ui_btn_start_clicked)
        self.ui.cb_hide_browser.stateChanged.connect(self.ui_cb_hide_browser_state_changed)

    def crawl_finished(self):
        self.ui.enable(True)

    def one_crawled(self):
        print(self.crawl_thread.count)
        self.ui.lbl_wcount.setText("Count: " + str(self.crawl_thread.count))

    def ui_btn_add_clicked(self):
        row = self.ui.tblw_posts.rowCount()
        self.ui.tblw_posts.insertRow(row)
        self.ui.tblw_posts.setItem(row, 0, QtWidgets.QTableWidgetItem(""))

    def ui_btn_delete_clicked(self):
        idx = self.ui.tblw_posts.selectedIndexes()
        rows = list(item.row() for item in idx)
        for selected_row in reversed(rows):
            self.ui.tblw_posts.removeRow(selected_row)

    def ui_btn_start_clicked(self):
        row_count = self.ui.tblw_posts.rowCount()
        posts = list()
        for row in range(row_count):
            post = self.ui.tblw_posts.item(row, 0).text()
            if (post != ""):
                posts.append(post)
        self.ui.enable(False)
        self.crawl_thread.set_posts(posts)
        self.crawl_thread.start()
        
    def ui_cb_hide_browser_state_changed(self, state):
        if (state == QtCore.Qt.Checked):
            Driver.hide(True)
        else:
            Driver.hide(False)

        print(Driver.hide_browser)