from PyQt5 import QtWidgets
from PyQt5 import QtGui
from yahtzee_ui import Ui_Dialog
from random import randint
from PyQt5.QtCore import pyqtSlot

dice = [1, 2, 3, 4, 5]
held_dice = [0, 0, 0, 0, 0]


def RollDice():
    for i in range(len(dice)):
        if held_dice[i] == 0:
            dice[i] = randint(1, 6)


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Add Images to Labels
        self.ui.lblD1.setScaledContents(True)
        self.ui.lblD2.setScaledContents(True)
        self.ui.lblD3.setScaledContents(True)
        self.ui.lblD4.setScaledContents(True)
        self.ui.lblD5.setScaledContents(True)

        # Add Click Even for Buttons
        self.ui.btnRoll.clicked.connect(self.on_btnRoll)

        # Inital Roll of dice
        self.checkHeld()
        RollDice()
        self.showDice()

    def checkHeld(self):
        if self.ui.chk1.isChecked():
            held_dice[0] = 1
        else:
            held_dice[0] = 0
        if self.ui.chk2.isChecked():
            held_dice[1] = 1
        else:
            held_dice[1] = 0
        if self.ui.chk3.isChecked():
            held_dice[2] = 1
        else:
            held_dice[2] = 0
        if self.ui.chk4.isChecked():
            held_dice[3] = 1
        else:
            held_dice[3] = 0
        if self.ui.chk5.isChecked():
            held_dice[4] = 1
        else:
            held_dice[4] = 0

    def showDice(self):
        self.ui.lblD1.setPixmap(QtGui.QPixmap(f"D{dice[0]}.png"))
        self.ui.lblD2.setPixmap(QtGui.QPixmap(f"D{dice[1]}.png"))
        self.ui.lblD3.setPixmap(QtGui.QPixmap(f"D{dice[2]}.png"))
        self.ui.lblD4.setPixmap(QtGui.QPixmap(f"D{dice[3]}.png"))
        self.ui.lblD5.setPixmap(QtGui.QPixmap(f"D{dice[4]}.png"))

    @pyqtSlot()
    def on_btnRoll(self):
        self.checkHeld()
        RollDice()
        self.showDice()


app = QtWidgets.QApplication([])
application = mywindow()
application.show()
app.exec()
