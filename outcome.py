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
        
        self.window.setFixedSize(self.window.width(), self.window.height())
        
        self.game = game
        self.ui.play_again.clicked.connect(self.play_again)
        self.ui.exit.clicked.connect(self.exit)

    def show_win(self, winners):
        winner_names = ' & '.join(winner.name for winner in winners)
        if len(winners) > 1:
            self.ui.outcome_lbl.setText(f'{winner_names} draw!')
        else:
            self.ui.outcome_lbl.setText(f'{winner_names} {winners[0].win}!')

    def play_again(self):
        self.window.close()
        self.game.reset()

    def exit(self):
        self.window.close()
        self.game.main_window.close()
        self.game.app.quit()
