from PyQt5 import QtCore
from fbc import Driver
import time

class TrackLoginThread(QtCore.QThread):
    signed_in = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()

    def run(self):
        print("Start")
        try:
            Driver.open().find_element_by_id("u_0_a")
        except:
            Driver.open().get("https://fb.com")

        while(1):
            time.sleep(1)
            try:
                Driver.open().find_element_by_id("logoutMenu")
                self.signed_in.emit()
                return
            except:
                pass
