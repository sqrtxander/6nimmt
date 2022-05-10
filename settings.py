from PyQt6 import QtCore, QtWidgets
from PyQt6.QtGui import QPixmap, QIcon
import sys

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

        self.defaults = {'delay': 2.0, 'points': 66}

        self.game = game
        
        self.ui.delay_inp.setMinimum(0)
        self.ui.delay_inp.setValue(self.settings_json["delay"])
        self.game.delay_time = int(self.settings_json["delay"] * 1000)

        self.ui.points_inp.setMinimum(1)
        self.ui.points_inp.setValue(self.settings_json["points"])
        self.game.points_required = int(self.settings_json["points"])

        self.ui.buttonBox.accepted.connect(self.ok)
        self.ui.buttonBox.rejected.connect(self.cancel)
        self.ui.reset_btn.clicked.connect(self.reset)
            
    def ok(self):
        self.game.delay_time = int(self.ui.delay_inp.value() * 1000)
        self.settings_json["delay"] = self.ui.delay_inp.value()

        self.game.points_required = int(self.ui.points_inp.value())
        self.settings_json["points"] = self.ui.points_inp.value()

        self.save_json()

    def cancel(self):
        self.ui.delay_inp.setValue(self.settings_json["delay"])
        self.ui.points_inp.setValue(self.settings_json["points"])

    def save_json(self):
        with open('settings.json', 'w') as f:
            json.dump(self.settings_json, f)

    def reset(self):
        self.ui.delay_inp.setValue(self.defaults["delay"])
        self.ui.points_inp.setValue(self.defaults["points"])