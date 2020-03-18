from fbc.gui.MsgBoxUi import Ui

class MsgBox():

    def __init__(self, title, detail):
        self.ui = Ui()
        self.ui.lbl_title.setText(title)
        self.ui.lbl_detail.setText(detail)
        self.ui.exec_()
        self.ui.show()