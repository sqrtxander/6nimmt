import random
from unicodedata import name
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtGui import QPixmap, QIcon
import sys
from functools import partial

from PyQt6.QtWidgets import QDialog, QApplication

from settingsWin import Ui_Dialog

import json


class Settings:
    def __init__(self, game):
        self.window = QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window)

        with open('settings.json', 'r') as f:
            self.settings_json = json.load(f)

        self.delay = self.ui.delay_inp        
        self.game = game
        self.ui.delay_inp.setMinimum(0)
        self.ui.delay_inp.setValue(self.settings_json["delay"])
        self.game.delay_time = int(self.settings_json["delay"] * 1000)

        self.ui.buttonBox.accepted.connect(self.ok)
        self.ui.buttonBox.rejected.connect(self.cancel)

            
    def ok(self):
        self.game.delay_time = int(self.ui.delay_inp.value() * 1000)
        self.settings_json["delay"] = self.ui.delay_inp.value()
        self.save_json()

    def cancel(self):
        print('cancel')
        self.ui.delay_inp.setValue(self.settings_json["delay"])

    def save_json(self):
        with open('settings.json', 'w') as f:
            json.dump(self.settings_json, f)