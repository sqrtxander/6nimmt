import random
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtGui import QPixmap, QIcon
import sys
from functools import partial

from PyQt6.QtWidgets import QDialog, QApplication

from rulesWin import Ui_Dialog1


class Rules():
    def __init__(self):
        self.window = QDialog()
        self.ui = Ui_Dialog1()
        self.ui.setupUi(self.window) 
