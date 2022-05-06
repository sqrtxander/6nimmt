import random
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtGui import QPixmap, QIcon
import sys
from functools import partial

from PyQt6.QtWidgets import QDialog, QApplication

from outcomeWin import Ui_Dialog


class Outcome:
    def __init__(self, game):
        self.window = QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window)
        
        self.game = game

    def show_win(self, player):
        self.ui.outcome_lbl.setText(f'{player.name} {player.win}!')
        self.ui.play_again.clicked.connect(partial(self.play_again))
        self.ui.exit.clicked.connect(self.exit)

    def play_again(self):
        self.window.close()
        self.game.reset()

    def exit(self):
        self.window.close()
        self.game.main_window.close()
        self.game.app.quit()
