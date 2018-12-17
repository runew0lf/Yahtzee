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
        self.hold_list = [self.ui.chk1, self.ui.chk2,
                          self.ui.chk3, self.ui.chk4, self.ui.chk5]
        self.lower_list = [self.ui.txtAces, self.ui.txtTwos, self.ui.txtThrees,
                           self.ui.txtFours, self.ui.txtFives, self.ui.txtSixes]

        # Add Click Even for Buttons
        self.ui.btnRoll.clicked.connect(self.on_btnRoll)
        self.ui.btnAces.clicked.connect(self.on_btnAces)
        self.ui.btnTwos.clicked.connect(self.on_btnTwos)
        self.ui.btnThrees.clicked.connect(self.on_btnThrees)
        self.ui.btnFours.clicked.connect(self.on_btnFours)
        self.ui.btnFives.clicked.connect(self.on_btnFives)
        self.ui.btnSixes.clicked.connect(self.on_btnSixes)

        # Initial Roll of dice
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
        self.set_upper_labels(1)

    @pyqtSlot()
    def on_btnTwos(self):
        self.set_upper_labels(2)

    @pyqtSlot()
    def on_btnThrees(self):
        self.set_upper_labels(3)

    @pyqtSlot()
    def on_btnFours(self):
        self.set_upper_labels(4)

    @pyqtSlot()
    def on_btnFives(self):
        self.set_upper_labels(5)

    @pyqtSlot()
    def on_btnSixes(self):
        self.set_upper_labels(6)

    def set_upper_labels(self, label):
        if self.lower_list[label - 1].text() is "":
            score = self.dice.count(label) * label
            self.lower_list[label - 1].setText(f"{score}")
            self.calc_upper_totals(score)
            self.clear_checks()

    def calc_upper_totals(self, value):
        total = self.ui.txtTotalScore.text()
        if total is "":
            self.ui.txtTotalScore.setText(f"{value}")
        else:
            self.ui.txtTotalScore.setText(f"{int(total) + int(value)}")

    def clear_checks(self):
        for hold in self.hold_list:
            hold.setChecked(False)


app = QtWidgets.QApplication([])
application = mywindow()
application.show()
app.exec()
