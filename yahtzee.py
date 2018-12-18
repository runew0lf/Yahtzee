from PyQt5 import QtWidgets
from PyQt5 import QtGui
from yahtzee_ui import Ui_Dialog
from random import randint
from PyQt5.QtCore import pyqtSlot

import collections

MAX_ROLLS = 3


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.dice = [1, 2, 3, 4, 5]
        self.rolls = MAX_ROLLS
        self.hold_list = [self.ui.chk1, self.ui.chk2,
                          self.ui.chk3, self.ui.chk4, self.ui.chk5]
        self.upper_list = [self.ui.txtAces, self.ui.txtTwos, self.ui.txtThrees,
                           self.ui.txtFours, self.ui.txtFives, self.ui.txtSixes]

        self.lower_list = [self.ui.txt3OfAKind, self.ui.txt4OfAKind, self.ui.txtFullHouse, self.ui.txtSmStraight,
                           self.ui.txtLgStraight, self.ui.txtChance, self.ui.txtYahtzee, self.ui.txtYahtzeeBonus]

        # Add Click Even for Buttons
        self.ui.btnRoll.clicked.connect(self.on_btnRoll)
        self.ui.btnAces.clicked.connect(self.on_btnAces)
        self.ui.btnTwos.clicked.connect(self.on_btnTwos)
        self.ui.btnThrees.clicked.connect(self.on_btnThrees)
        self.ui.btnFours.clicked.connect(self.on_btnFours)
        self.ui.btnFives.clicked.connect(self.on_btnFives)
        self.ui.btnSixes.clicked.connect(self.on_btnSixes)
        self.ui.btn3OfAKind.clicked.connect(self.on_btn3OfAKind)
        self.ui.btn4OfAKind.clicked.connect(self.on_btn4OfAKind)
        self.ui.btnFullHouse.clicked.connect(self.on_btnFullhouse)
        self.ui.btnSmStraight.clicked.connect(self.on_btnSmStraight)
        self.ui.btnLgStraight.clicked.connect(self.on_btnLgStraight)
        self.ui.btnChance.clicked.connect(self.on_btnChance)
        self.ui.btnYahtzee.clicked.connect(self.on_btnYahtzee)

        # Initial Roll of dice
        self.RollDice()

    def RollDice(self):
        if self.rolls < 1:
            return
        for i in range(len(self.dice)):
            if not self.hold_list[i].isChecked():
                self.dice[i] = randint(1, 6)
        self.rolls -= 1
        self.showDice()

    def showDice(self):
        self.ui.lblD1.setPixmap(QtGui.QPixmap(f"D{self.dice[0]}.png"))
        self.ui.lblD2.setPixmap(QtGui.QPixmap(f"D{self.dice[1]}.png"))
        self.ui.lblD3.setPixmap(QtGui.QPixmap(f"D{self.dice[2]}.png"))
        self.ui.lblD4.setPixmap(QtGui.QPixmap(f"D{self.dice[3]}.png"))
        self.ui.lblD5.setPixmap(QtGui.QPixmap(f"D{self.dice[4]}.png"))
        self.ui.btnRoll.setText(f"Rolls ({self.rolls})")

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

    @pyqtSlot()
    def on_btn3OfAKind(self):
        if self.ui.txt3OfAKind.text() == "":
            self.check_Yahtzee()
            if list(set([x for x in self.dice if self.dice.count(x) > 2])):
                self.ui.txt3OfAKind.setText(f"{sum(self.dice)}")
            else:
                self.ui.txt3OfAKind.setText("0")
            self.set_lower_labels(0)

    @pyqtSlot()
    def on_btn4OfAKind(self):
        if self.ui.txt4OfAKind.text() == "":
            self.check_Yahtzee()
            if list(set([x for x in self.dice if self.dice.count(x) > 3])):
                self.ui.txt4OfAKind.setText(f"{sum(self.dice)}")
            else:
                self.ui.txt4OfAKind.setText("0")
            self.set_lower_labels(1)

    @pyqtSlot()
    def on_btnFullhouse(self):
        if self.ui.txtFullHouse.text() == "":
            self.check_Yahtzee()
            counter = collections.Counter(self.dice)
            if 3 in counter.values() and 2 in counter.values():
                self.ui.txtFullHouse.setText("25")
            else:
                self.ui.txtFullHouse.setText("0")
            self.set_lower_labels(2)

    @pyqtSlot()
    def on_btnSmStraight(self):
        if self.ui.txtSmStraight.text() == "":
            self.check_Yahtzee()
            if self.check_straight() >= 4:
                self.ui.txtSmStraight.setText("30")
            else:
                self.ui.txtSmStraight.setText("0")
            self.set_lower_labels(3)

    @pyqtSlot()
    def on_btnLgStraight(self):
        if self.ui.txtLgStraight.text() == "":
            self.check_Yahtzee()
            if self.check_straight() >= 5:
                self.ui.txtLgStraight.setText("40")
            else:
                self.ui.txtLgStraight.setText("0")
            self.set_lower_labels(4)

    @pyqtSlot()
    def on_btnChance(self):
        if self.ui.txtChance.text() == "":
            self.check_Yahtzee()
            self.ui.txtChance.setText(f"{sum(self.dice)}")
            self.set_lower_labels(5)

    @pyqtSlot()
    def on_btnYahtzee(self):
        if self.ui.txtYahtzee.text() == "":
            if list(set([x for x in self.dice if self.dice.count(x) == 5])):
                self.ui.txtYahtzee.setText("50")
            else:
                self.ui.txtYahtzee.setText("0")
            self.set_lower_labels(6)

    def check_Yahtzee(self):
        if self.ui.txtYahtzee.text() != "":
            if self.ui.txtYahtzee.text() != "0":
                if list(set([x for x in self.dice if self.dice.count(x) == 5])):
                    if self.ui.txtYahtzeeBonus.text() == "":
                        self.ui.txtYahtzeeBonus.setText("0")
                    bonusYahtzee = int(self.ui.txtYahtzeeBonus.text()) + 100
                    self.ui.txtYahtzeeBonus.setText(f"{bonusYahtzee}")

    def check_straight(self):
        self.dice.sort()
        newlist = list(set(self.dice))
        bestcount = 1
        count = 1
        for i in range(len(newlist) - 1):
            if newlist[i] + 1 == newlist[i + 1]:
                count += 1
                if bestcount < count:
                    bestcount = count
            else:
                if bestcount < count:
                    bestcount = count
                count = 1
        return bestcount

    def set_lower_labels(self, label):
        if self.ui.txtLowerTotal.text() == "":
            score = 0
        else:
            score = int(self.ui.txtLowerTotal.text())
        value = int(self.lower_list[label].text())
        score += value
        self.ui.txtLowerTotal.setText(f"{score}")
        self.clear_checks()
        self.rolls = MAX_ROLLS
        self.RollDice()
        self.calc_totals()

    def set_upper_labels(self, label):
        if self.upper_list[label - 1].text() == "":
            self.check_Yahtzee()
            score = self.dice.count(label) * label
            self.upper_list[label - 1].setText(f"{score}")
            self.calc_upper_totals(score)
            self.clear_checks()
            self.rolls = MAX_ROLLS
            self.RollDice()
            self.calc_totals()

    def calc_upper_totals(self, value):
        total = self.ui.txtTotalScore.text()
        bonus = 0
        if total == "":
            self.ui.txtTotalScore.setText(f"{value}")
        else:
            self.ui.txtTotalScore.setText(f"{int(total) + int(value)}")
        if int(self.ui.txtTotalScore.text()) < 64:
            bonus = 0
        else:
            bonus = 35
        self.ui.txtBonus.setText(f"{bonus}")
        uppertotal = int(self.ui.txtTotalScore.text()) + bonus
        self.ui.txtUpperTotal.setText(f"{uppertotal}")


    def calc_totals(self):
        total = 0
        if self.ui.txtUpperTotal.text() != "":
           total = int(self.ui.txtUpperTotal.text())
        if self.ui.txtLowerTotal.text() != "":
            total += int(self.ui.txtLowerTotal.text())
        self.ui.txtGrandTotal.setText(f"{total}")

    def clear_checks(self):
        for hold in self.hold_list:
            hold.setChecked(False)


app = QtWidgets.QApplication([])
application = mywindow()
application.show()
app.exec()
