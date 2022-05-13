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

        self.page = 0
        self.page_count = 2
        page_0 = [self.ui.pg0_heading1, self.ui.pg0_rules1, self.ui.pg0_heading2, self.ui.pg0_rules2]
        page_1 = [self.ui.pg1_heading1, self.ui.pg1_rules1, self.ui.pg1_heading2, self.ui.pg1_rules2]

        self.pages = [page_0, page_1]

        self.ui.right_btn.clicked.connect(lambda: self.change_page(1))
        self.ui.left_btn.clicked.connect(lambda:self.change_page(-1))

        for page in self.pages[1:]:
            self.hide_widgets(page)

    def hide_widgets(self, widgets):
        for widget in widgets:
            widget.hide()

    def show_widgets(self, widgets):
        for widget in widgets:
            widget.show()

    def change_page(self, direction):
        self.hide_widgets(self.pages[self.page])
        
        self.page = (self.page + direction) % self.page_count

        self.show_widgets(self.pages[self.page])