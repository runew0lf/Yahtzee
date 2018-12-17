from PyQt5 import QtWidgets
from PyQt5 import QtGui
from yahtzee_ui import Ui_Dialog
from random import randint
from PyQt5.QtCore import pyqtSlot


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.dice = [1, 2, 3, 4, 5]   
        self.hold_list = [self.ui.chk1, self.ui.chk2, self.ui.chk3, self.ui.chk4, self.ui.chk5]

        # Add Click Even for Buttons
        self.ui.btnRoll.clicked.connect(self.on_btnRoll)
        self.ui.btnAces.clicked.connect(self.on_btnAces)
        self.ui.btnTwos.clicked.connect(self.on_btnTwos)
        self.ui.btnThrees.clicked.connect(self.on_btnThrees)
        self.ui.btnFours.clicked.connect(self.on_btnFours)
        self.ui.btnFives.clicked.connect(self.on_btnFives)
        self.ui.btnSixes.clicked.connect(self.on_btnSixes)

        # Inital Roll of dice
        self.RollDice()

    def RollDice(self):
        for i in range(len(self.dice)):
            if not self.hold_list[i].isChecked():
                self.dice[i] = randint(1, 6)
        self.showDice()
            
    def showDice(self):
        self.ui.lblD1.setPixmap(QtGui.QPixmap(f"D{self.dice[0]}.png"))
        self.ui.lblD2.setPixmap(QtGui.QPixmap(f"D{self.dice[1]}.png"))
        self.ui.lblD3.setPixmap(QtGui.QPixmap(f"D{self.dice[2]}.png"))
        self.ui.lblD4.setPixmap(QtGui.QPixmap(f"D{self.dice[3]}.png"))
        self.ui.lblD5.setPixmap(QtGui.QPixmap(f"D{self.dice[4]}.png"))

    @pyqtSlot()
    def on_btnRoll(self):
        self.RollDice()

    @pyqtSlot()
    def on_btnAces(self):
        if self.ui.txtAces.text() is "":
            self.ui.txtAces.setText(f"{self.dice.count(1)}")

    @pyqtSlot()
    def on_btnTwos(self):
        if self.ui.txtTwos.text() is "":
            self.ui.txtTwos.setText(f"{self.dice.count(2)}")

    @pyqtSlot()
    def on_btnThrees(self):
        if self.ui.txtThrees.text() is "":
            self.ui.txtThrees.setText(f"{self.dice.count(3)}")

    @pyqtSlot()
    def on_btnFours(self):
        if self.ui.txtFours.text() is "":        
            self.ui.txtFours.setText(f"{self.dice.count(4)}")

    @pyqtSlot()
    def on_btnFives(self):
        if self.ui.txtFives.text() is "":        
            self.ui.txtFives.setText(f"{self.dice.count(5)}")

    @pyqtSlot()
    def on_btnSixes(self):
        if self.ui.txtSixes.text() is "":        
            self.ui.txtSixes.setText(f"{self.dice.count(6)}")


app = QtWidgets.QApplication([])
application = mywindow()
application.show()
app.exec()
