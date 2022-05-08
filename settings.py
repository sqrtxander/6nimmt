import random
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtGui import QPixmap, QIcon
import sys
from functools import partial

from PyQt6.QtWidgets import QDialog, QApplication

from settingsWin import Ui_Dialog


class Settings:
    def __init__(self, game):
        self.window = QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window)
        
        self.game = game

    

