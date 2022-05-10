from PyQt6 import QtCore, QtWidgets
from PyQt6.QtGui import QPixmap, QIcon
import sys

from PyQt6.QtWidgets import QDialog, QApplication

from rulesWin import Ui_Dialog


class Rules():
    def __init__(self):
        self.window = QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window) 
