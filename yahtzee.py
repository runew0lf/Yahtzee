from PyQt5 import QtWidgets
from PyQt5 import QtGui
from yahtzee_ui import Ui_Dialog


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Add Images to Labels
        self.ui.lblD1.setScaledContents(True)
        self.ui.lblD1.setPixmap(QtGui.QPixmap("D1.png"))
        self.ui.lblD2.setScaledContents(True)
        self.ui.lblD2.setPixmap(QtGui.QPixmap("D2.png"))
        self.ui.lblD3.setScaledContents(True)
        self.ui.lblD3.setPixmap(QtGui.QPixmap("D3.png"))
        self.ui.lblD4.setScaledContents(True)
        self.ui.lblD4.setPixmap(QtGui.QPixmap("D4.png"))
        self.ui.lblD5.setScaledContents(True)
        self.ui.lblD5.setPixmap(QtGui.QPixmap("D5.png"))


app = QtWidgets.QApplication([])
application = mywindow()
application.show()
app.exec()
