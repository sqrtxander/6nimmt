# Form implementation generated from reading ui file 'outcomeWin.ui'
#
# Created by: PyQt6 UI code generator 6.2.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.outcome_lbl = QtWidgets.QLabel(Dialog)
        self.outcome_lbl.setGeometry(QtCore.QRect(30, 10, 341, 181))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.outcome_lbl.setFont(font)
        self.outcome_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.outcome_lbl.setWordWrap(True)
        self.outcome_lbl.setObjectName("outcome_lbl")
        self.play_again = QtWidgets.QPushButton(Dialog)
        self.play_again.setGeometry(QtCore.QRect(30, 200, 151, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.play_again.setFont(font)
        self.play_again.setObjectName("play_again")
        self.exit = QtWidgets.QPushButton(Dialog)
        self.exit.setGeometry(QtCore.QRect(220, 200, 151, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.exit.setFont(font)
        self.exit.setObjectName("exit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "6 Nimmt! Winner"))
        self.outcome_lbl.setText(_translate("Dialog", "This player wins"))
        self.play_again.setText(_translate("Dialog", "Play again"))
        self.exit.setText(_translate("Dialog", "Exit game"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
