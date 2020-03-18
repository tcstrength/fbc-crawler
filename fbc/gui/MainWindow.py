from fbc.gui.MainWindowUi import Ui
from fbc.gui.MsgBox import MsgBox
from fbc.gui.threads.TrackLogin import TrackLoginThread
from fbc.gui.threads.Crawl import CrawlThread
from fbc import Driver
from PyQt5 import QtWidgets, QtCore 

class MainWindow():
    def __init__(self):
        self.crawl_thread = CrawlThread()
        self.crawl_thread.one_crawled.connect(self.crawl_thread_one_crawled)
        self.crawl_thread.finished.connect(self.crawl_thread_finished)
        self.crawl_thread.error.connect(self.crawl_thread_error)
        self.ui = Ui()
        self.ui.btn_add.clicked.connect(self.ui_btn_add_clicked)
        self.ui.btn_delete.clicked.connect(self.ui_btn_delete_clicked)
        self.ui.btn_start.clicked.connect(self.ui_btn_start_clicked)
        self.ui.cb_hide_browser.stateChanged.connect(self.ui_cb_hide_browser_state_changed)

    def start_crawl(self):
        row_count = self.ui.tblw_posts.rowCount()
        posts = list()
        for row in range(row_count):
            post = self.ui.tblw_posts.item(row, 0).text()
            if (post != ""):
                posts.append(post)

        self.error_found = False
        self.crawl_thread.set_posts(posts)
        self.crawl_thread.start()

    def stop_crawl(self):
        self.crawl_thread.terminate()
        Driver.close()

    def crawl_thread_error(self, msg, post):
        self.error_found = True
        MsgBox("May be wrong post id: " + post, str(msg))

    def crawl_thread_finished(self):
        self.ui.enable(True)
        self.ui.btn_start.setText("Start")

        if (not self.error_found):
            detail = ""
            detail += "Total posts: %d\n" % (self.ui.tblw_posts.rowCount())
            detail += "Total words: %d\n" % (self.crawl_thread.count)
            detail += "Finished!"
            MsgBox("Crawl finished", detail)

    def crawl_thread_one_crawled(self, txt):
        self.ui.lbl_wcount.setText("Count: " + str(self.crawl_thread.count))
        self.ui.remove_contain_str(txt)

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
        if (self.ui.btn_start.text() == "Stop"):
            self.stop_crawl()
            return

        self.ui.enable(False)
        self.ui.btn_start.setText("Stop")
        self.start_crawl()
        
    def ui_cb_hide_browser_state_changed(self, state):
        if (state == QtCore.Qt.Checked):
            Driver.hide(True)
        else:
            Driver.hide(False)