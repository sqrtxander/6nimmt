# Form implementation generated from reading ui file 'mainWin.ui'
#
# Created by: PyQt6 UI code generator 6.2.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(730, 562)
        font = QtGui.QFont()
        font.setPointSize(8)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("background/icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        MainWindow.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.hand00 = QtWidgets.QPushButton(self.centralwidget)
        self.hand00.setGeometry(QtCore.QRect(20, 40, 62, 82))
        self.hand00.setText("")
        self.hand00.setFlat(True)
        self.hand00.setObjectName("hand00")
        self.hand_lbl = QtWidgets.QLabel(self.centralwidget)
        self.hand_lbl.setGeometry(QtCore.QRect(20, 0, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.hand_lbl.setFont(font)
        self.hand_lbl.setStyleSheet("color: white;")
        self.hand_lbl.setScaledContents(False)
        self.hand_lbl.setObjectName("hand_lbl")
        self.table_lbl = QtWidgets.QLabel(self.centralwidget)
        self.table_lbl.setGeometry(QtCore.QRect(20, 120, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.table_lbl.setFont(font)
        self.table_lbl.setStyleSheet("color: white;")
        self.table_lbl.setScaledContents(False)
        self.table_lbl.setObjectName("table_lbl")
        self.hand01 = QtWidgets.QPushButton(self.centralwidget)
        self.hand01.setGeometry(QtCore.QRect(90, 40, 62, 82))
        self.hand01.setText("")
        self.hand01.setFlat(True)
        self.hand01.setObjectName("hand01")
        self.hand02 = QtWidgets.QPushButton(self.centralwidget)
        self.hand02.setGeometry(QtCore.QRect(160, 40, 62, 82))
        self.hand02.setText("")
        self.hand02.setFlat(True)
        self.hand02.setObjectName("hand02")
        self.hand03 = QtWidgets.QPushButton(self.centralwidget)
        self.hand03.setGeometry(QtCore.QRect(230, 40, 62, 82))
        self.hand03.setText("")
        self.hand03.setFlat(True)
        self.hand03.setObjectName("hand03")
        self.hand04 = QtWidgets.QPushButton(self.centralwidget)
        self.hand04.setGeometry(QtCore.QRect(300, 40, 62, 82))
        self.hand04.setText("")
        self.hand04.setFlat(True)
        self.hand04.setObjectName("hand04")
        self.hand08 = QtWidgets.QPushButton(self.centralwidget)
        self.hand08.setGeometry(QtCore.QRect(580, 40, 62, 82))
        self.hand08.setText("")
        self.hand08.setFlat(True)
        self.hand08.setObjectName("hand08")
        self.hand07 = QtWidgets.QPushButton(self.centralwidget)
        self.hand07.setGeometry(QtCore.QRect(510, 40, 62, 82))
        self.hand07.setText("")
        self.hand07.setFlat(True)
        self.hand07.setObjectName("hand07")
        self.hand05 = QtWidgets.QPushButton(self.centralwidget)
        self.hand05.setGeometry(QtCore.QRect(370, 40, 62, 82))
        self.hand05.setText("")
        self.hand05.setFlat(True)
        self.hand05.setObjectName("hand05")
        self.hand06 = QtWidgets.QPushButton(self.centralwidget)
        self.hand06.setGeometry(QtCore.QRect(440, 40, 62, 82))
        self.hand06.setText("")
        self.hand06.setFlat(True)
        self.hand06.setObjectName("hand06")
        self.hand09 = QtWidgets.QPushButton(self.centralwidget)
        self.hand09.setGeometry(QtCore.QRect(650, 40, 62, 82))
        self.hand09.setText("")
        self.hand09.setFlat(True)
        self.hand09.setObjectName("hand09")
        self.table03 = QtWidgets.QPushButton(self.centralwidget)
        self.table03.setGeometry(QtCore.QRect(230, 160, 62, 82))
        self.table03.setText("")
        self.table03.setFlat(True)
        self.table03.setObjectName("table03")
        self.table05 = QtWidgets.QPushButton(self.centralwidget)
        self.table05.setGeometry(QtCore.QRect(370, 160, 62, 82))
        self.table05.setText("")
        self.table05.setFlat(True)
        self.table05.setObjectName("table05")
        self.table02 = QtWidgets.QPushButton(self.centralwidget)
        self.table02.setGeometry(QtCore.QRect(160, 160, 62, 82))
        self.table02.setText("")
        self.table02.setFlat(True)
        self.table02.setObjectName("table02")
        self.table00 = QtWidgets.QPushButton(self.centralwidget)
        self.table00.setGeometry(QtCore.QRect(20, 160, 62, 82))
        self.table00.setText("")
        self.table00.setFlat(True)
        self.table00.setObjectName("table00")
        self.table01 = QtWidgets.QPushButton(self.centralwidget)
        self.table01.setGeometry(QtCore.QRect(90, 160, 62, 82))
        self.table01.setText("")
        self.table01.setFlat(True)
        self.table01.setObjectName("table01")
        self.table04 = QtWidgets.QPushButton(self.centralwidget)
        self.table04.setGeometry(QtCore.QRect(300, 160, 62, 82))
        self.table04.setText("")
        self.table04.setFlat(True)
        self.table04.setObjectName("table04")
        self.table13 = QtWidgets.QPushButton(self.centralwidget)
        self.table13.setGeometry(QtCore.QRect(230, 250, 62, 82))
        self.table13.setText("")
        self.table13.setFlat(True)
        self.table13.setObjectName("table13")
        self.table15 = QtWidgets.QPushButton(self.centralwidget)
        self.table15.setGeometry(QtCore.QRect(370, 250, 62, 82))
        self.table15.setText("")
        self.table15.setFlat(True)
        self.table15.setObjectName("table15")
        self.table12 = QtWidgets.QPushButton(self.centralwidget)
        self.table12.setGeometry(QtCore.QRect(160, 250, 62, 82))
        self.table12.setText("")
        self.table12.setFlat(True)
        self.table12.setObjectName("table12")
        self.table10 = QtWidgets.QPushButton(self.centralwidget)
        self.table10.setGeometry(QtCore.QRect(20, 250, 62, 82))
        self.table10.setText("")
        self.table10.setFlat(True)
        self.table10.setObjectName("table10")
        self.table11 = QtWidgets.QPushButton(self.centralwidget)
        self.table11.setGeometry(QtCore.QRect(90, 250, 62, 82))
        self.table11.setText("")
        self.table11.setFlat(True)
        self.table11.setObjectName("table11")
        self.table14 = QtWidgets.QPushButton(self.centralwidget)
        self.table14.setGeometry(QtCore.QRect(300, 250, 62, 82))
        self.table14.setText("")
        self.table14.setFlat(True)
        self.table14.setObjectName("table14")
        self.table20 = QtWidgets.QPushButton(self.centralwidget)
        self.table20.setGeometry(QtCore.QRect(20, 340, 62, 82))
        self.table20.setText("")
        self.table20.setFlat(True)
        self.table20.setObjectName("table20")
        self.table23 = QtWidgets.QPushButton(self.centralwidget)
        self.table23.setGeometry(QtCore.QRect(230, 340, 62, 82))
        self.table23.setText("")
        self.table23.setFlat(True)
        self.table23.setObjectName("table23")
        self.table21 = QtWidgets.QPushButton(self.centralwidget)
        self.table21.setGeometry(QtCore.QRect(90, 340, 62, 82))
        self.table21.setText("")
        self.table21.setFlat(True)
        self.table21.setObjectName("table21")
        self.table31 = QtWidgets.QPushButton(self.centralwidget)
        self.table31.setGeometry(QtCore.QRect(90, 430, 62, 82))
        self.table31.setText("")
        self.table31.setFlat(True)
        self.table31.setObjectName("table31")
        self.table32 = QtWidgets.QPushButton(self.centralwidget)
        self.table32.setGeometry(QtCore.QRect(160, 430, 62, 82))
        self.table32.setText("")
        self.table32.setFlat(True)
        self.table32.setObjectName("table32")
        self.table25 = QtWidgets.QPushButton(self.centralwidget)
        self.table25.setGeometry(QtCore.QRect(370, 340, 62, 82))
        self.table25.setText("")
        self.table25.setFlat(True)
        self.table25.setObjectName("table25")
        self.table35 = QtWidgets.QPushButton(self.centralwidget)
        self.table35.setGeometry(QtCore.QRect(370, 430, 62, 82))
        self.table35.setText("")
        self.table35.setFlat(True)
        self.table35.setObjectName("table35")
        self.table22 = QtWidgets.QPushButton(self.centralwidget)
        self.table22.setGeometry(QtCore.QRect(160, 340, 62, 82))
        self.table22.setText("")
        self.table22.setFlat(True)
        self.table22.setObjectName("table22")
        self.table24 = QtWidgets.QPushButton(self.centralwidget)
        self.table24.setGeometry(QtCore.QRect(300, 340, 62, 82))
        self.table24.setText("")
        self.table24.setFlat(True)
        self.table24.setObjectName("table24")
        self.table34 = QtWidgets.QPushButton(self.centralwidget)
        self.table34.setGeometry(QtCore.QRect(300, 430, 62, 82))
        self.table34.setText("")
        self.table34.setFlat(True)
        self.table34.setObjectName("table34")
        self.table30 = QtWidgets.QPushButton(self.centralwidget)
        self.table30.setGeometry(QtCore.QRect(20, 430, 62, 82))
        self.table30.setText("")
        self.table30.setFlat(True)
        self.table30.setObjectName("table30")
        self.table33 = QtWidgets.QPushButton(self.centralwidget)
        self.table33.setGeometry(QtCore.QRect(230, 430, 62, 82))
        self.table33.setText("")
        self.table33.setFlat(True)
        self.table33.setObjectName("table33")
        self.player1 = QtWidgets.QFrame(self.centralwidget)
        self.player1.setGeometry(QtCore.QRect(440, 155, 271, 90))
        self.player1.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.player1.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.player1.setObjectName("player1")
        self.p1_lbl = QtWidgets.QLabel(self.player1)
        self.p1_lbl.setGeometry(QtCore.QRect(0, 0, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.p1_lbl.setFont(font)
        self.p1_lbl.setStyleSheet("color: white;")
        self.p1_lbl.setObjectName("p1_lbl")
        self.p1_played = QtWidgets.QLabel(self.player1)
        self.p1_played.setGeometry(QtCore.QRect(70, 5, 60, 80))
        self.p1_played.setText("")
        self.p1_played.setObjectName("p1_played")
        self.p1_pickup = QtWidgets.QLabel(self.player1)
        self.p1_pickup.setGeometry(QtCore.QRect(140, 5, 60, 80))
        self.p1_pickup.setText("")
        self.p1_pickup.setObjectName("p1_pickup")
        self.p1_score = QtWidgets.QLabel(self.player1)
        self.p1_score.setGeometry(QtCore.QRect(220, 30, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.p1_score.setFont(font)
        self.p1_score.setStyleSheet("color: white;")
        self.p1_score.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.p1_score.setObjectName("p1_score")
        self.played_lbl = QtWidgets.QLabel(self.centralwidget)
        self.played_lbl.setGeometry(QtCore.QRect(510, 120, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.played_lbl.setFont(font)
        self.played_lbl.setStyleSheet("color: white;")
        self.played_lbl.setScaledContents(False)
        self.played_lbl.setObjectName("played_lbl")
        self.pick_up_lbl = QtWidgets.QLabel(self.centralwidget)
        self.pick_up_lbl.setGeometry(QtCore.QRect(580, 120, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pick_up_lbl.setFont(font)
        self.pick_up_lbl.setStyleSheet("color: white;")
        self.pick_up_lbl.setScaledContents(False)
        self.pick_up_lbl.setObjectName("pick_up_lbl")
        self.score_lbl = QtWidgets.QLabel(self.centralwidget)
        self.score_lbl.setGeometry(QtCore.QRect(650, 120, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.score_lbl.setFont(font)
        self.score_lbl.setStyleSheet("color: white;")
        self.score_lbl.setScaledContents(False)
        self.score_lbl.setObjectName("score_lbl")
        self.player_2 = QtWidgets.QFrame(self.centralwidget)
        self.player_2.setGeometry(QtCore.QRect(440, 244, 271, 91))
        self.player_2.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.player_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.player_2.setObjectName("player_2")
        self.p2_lbl = QtWidgets.QLabel(self.player_2)
        self.p2_lbl.setGeometry(QtCore.QRect(0, 0, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.p2_lbl.setFont(font)
        self.p2_lbl.setStyleSheet("color: white;")
        self.p2_lbl.setObjectName("p2_lbl")
        self.p2_played = QtWidgets.QLabel(self.player_2)
        self.p2_played.setGeometry(QtCore.QRect(70, 5, 60, 80))
        self.p2_played.setText("")
        self.p2_played.setObjectName("p2_played")
        self.p2_pickup = QtWidgets.QLabel(self.player_2)
        self.p2_pickup.setGeometry(QtCore.QRect(140, 5, 60, 80))
        self.p2_pickup.setText("")
        self.p2_pickup.setObjectName("p2_pickup")
        self.p2_score = QtWidgets.QLabel(self.player_2)
        self.p2_score.setGeometry(QtCore.QRect(220, 30, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.p2_score.setFont(font)
        self.p2_score.setStyleSheet("color: white;")
        self.p2_score.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.p2_score.setObjectName("p2_score")
        self.player_3 = QtWidgets.QFrame(self.centralwidget)
        self.player_3.setGeometry(QtCore.QRect(440, 334, 271, 91))
        self.player_3.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.player_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.player_3.setObjectName("player_3")
        self.p3_lbl = QtWidgets.QLabel(self.player_3)
        self.p3_lbl.setGeometry(QtCore.QRect(0, 0, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.p3_lbl.setFont(font)
        self.p3_lbl.setStyleSheet("color: white;")
        self.p3_lbl.setObjectName("p3_lbl")
        self.p3_played = QtWidgets.QLabel(self.player_3)
        self.p3_played.setGeometry(QtCore.QRect(70, 5, 60, 80))
        self.p3_played.setText("")
        self.p3_played.setObjectName("p3_played")
        self.p3_pickup = QtWidgets.QLabel(self.player_3)
        self.p3_pickup.setGeometry(QtCore.QRect(140, 5, 60, 80))
        self.p3_pickup.setText("")
        self.p3_pickup.setObjectName("p3_pickup")
        self.p3_score = QtWidgets.QLabel(self.player_3)
        self.p3_score.setGeometry(QtCore.QRect(220, 30, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.p3_score.setFont(font)
        self.p3_score.setStyleSheet("color: white;")
        self.p3_score.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.p3_score.setObjectName("p3_score")
        self.player_4 = QtWidgets.QFrame(self.centralwidget)
        self.player_4.setGeometry(QtCore.QRect(440, 424, 271, 90))
        self.player_4.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.player_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.player_4.setObjectName("player_4")
        self.p4_lbl = QtWidgets.QLabel(self.player_4)
        self.p4_lbl.setGeometry(QtCore.QRect(0, 0, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.p4_lbl.setFont(font)
        self.p4_lbl.setStyleSheet("color: white;")
        self.p4_lbl.setObjectName("p4_lbl")
        self.p4_played = QtWidgets.QLabel(self.player_4)
        self.p4_played.setGeometry(QtCore.QRect(70, 5, 60, 80))
        self.p4_played.setText("")
        self.p4_played.setObjectName("p4_played")
        self.pr_pickup = QtWidgets.QLabel(self.player_4)
        self.pr_pickup.setGeometry(QtCore.QRect(140, 5, 60, 80))
        self.pr_pickup.setText("")
        self.pr_pickup.setObjectName("pr_pickup")
        self.p4_score = QtWidgets.QLabel(self.player_4)
        self.p4_score.setGeometry(QtCore.QRect(220, 30, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.p4_score.setFont(font)
        self.p4_score.setStyleSheet("color: white;")
        self.p4_score.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.p4_score.setObjectName("p4_score")
        self.current_lbl = QtWidgets.QLabel(self.centralwidget)
        self.current_lbl.setGeometry(QtCore.QRect(183, 5, 365, 32))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.current_lbl.setFont(font)
        self.current_lbl.setAutoFillBackground(False)
        self.current_lbl.setStyleSheet("color: white;")
        self.current_lbl.setText("")
        self.current_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.current_lbl.setObjectName("current_lbl")
        self.rules_button = QtWidgets.QPushButton(self.centralwidget)
        self.rules_button.setGeometry(QtCore.QRect(650, 5, 60, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rules_button.setFont(font)
        self.rules_button.setObjectName("rules_button")
        self.menu_cover = QtWidgets.QLabel(self.centralwidget)
        self.menu_cover.setGeometry(QtCore.QRect(0, 1, 731, 581))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.menu_cover.setFont(font)
        self.menu_cover.setAutoFillBackground(True)
        self.menu_cover.setText("")
        self.menu_cover.setObjectName("menu_cover")
        self.menu_text = QtWidgets.QLabel(self.centralwidget)
        self.menu_text.setGeometry(QtCore.QRect(190, 130, 350, 91))
        font = QtGui.QFont()
        font.setPointSize(56)
        font.setBold(False)
        font.setWeight(50)
        self.menu_text.setFont(font)
        self.menu_text.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.menu_text.setObjectName("menu_text")
        self.play_btn = QtWidgets.QPushButton(self.centralwidget)
        self.play_btn.setGeometry(QtCore.QRect(260, 250, 210, 100))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.play_btn.setFont(font)
        self.play_btn.setObjectName("play_btn")
        self.exit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.exit_btn.setGeometry(QtCore.QRect(260, 380, 210, 100))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.exit_btn.setFont(font)
        self.exit_btn.setObjectName("exit_btn")
        self.menu_image = QtWidgets.QLabel(self.centralwidget)
        self.menu_image.setGeometry(QtCore.QRect(560, 120, 128, 128))
        self.menu_image.setText("")
        self.menu_image.setObjectName("menu_image")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(426, 126, 20, 401))
        self.line.setStyleSheet("color: white;")
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.line.setLineWidth(3)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(436, 119, 311, 16))
        self.line_2.setStyleSheet("color: white;\n"
"\n"
"")
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.line_2.setLineWidth(3)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setObjectName("line_2")
        self.settings_button = QtWidgets.QPushButton(self.centralwidget)
        self.settings_button.setGeometry(QtCore.QRect(580, 5, 60, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.settings_button.setFont(font)
        self.settings_button.setObjectName("settings_button")
        self.hand00.raise_()
        self.hand_lbl.raise_()
        self.table_lbl.raise_()
        self.hand01.raise_()
        self.hand02.raise_()
        self.hand03.raise_()
        self.hand04.raise_()
        self.hand08.raise_()
        self.hand07.raise_()
        self.hand05.raise_()
        self.hand06.raise_()
        self.hand09.raise_()
        self.table03.raise_()
        self.table05.raise_()
        self.table02.raise_()
        self.table00.raise_()
        self.table01.raise_()
        self.table04.raise_()
        self.table13.raise_()
        self.table15.raise_()
        self.table12.raise_()
        self.table10.raise_()
        self.table11.raise_()
        self.table14.raise_()
        self.table20.raise_()
        self.table23.raise_()
        self.table21.raise_()
        self.table31.raise_()
        self.table32.raise_()
        self.table25.raise_()
        self.table35.raise_()
        self.table22.raise_()
        self.table24.raise_()
        self.table34.raise_()
        self.table30.raise_()
        self.table33.raise_()
        self.player1.raise_()
        self.played_lbl.raise_()
        self.pick_up_lbl.raise_()
        self.score_lbl.raise_()
        self.player_2.raise_()
        self.player_3.raise_()
        self.player_4.raise_()
        self.current_lbl.raise_()
        self.rules_button.raise_()
        self.line.raise_()
        self.line_2.raise_()
        self.settings_button.raise_()
        self.menu_cover.raise_()
        self.menu_image.raise_()
        self.menu_text.raise_()
        self.exit_btn.raise_()
        self.play_btn.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 730, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "6 Nimmt!"))
        self.hand_lbl.setText(_translate("MainWindow", "Your Hand:"))
        self.table_lbl.setText(_translate("MainWindow", "Table:"))
        self.p1_lbl.setText(_translate("MainWindow", "You"))
        self.p1_score.setText(_translate("MainWindow", "00"))
        self.played_lbl.setText(_translate("MainWindow", "Played"))
        self.pick_up_lbl.setText(_translate("MainWindow", "Pick Up"))
        self.score_lbl.setText(_translate("MainWindow", "Score"))
        self.p2_lbl.setText(_translate("MainWindow", "P2"))
        self.p2_score.setText(_translate("MainWindow", "00"))
        self.p3_lbl.setText(_translate("MainWindow", "P3"))
        self.p3_score.setText(_translate("MainWindow", "00"))
        self.p4_lbl.setText(_translate("MainWindow", "P4"))
        self.p4_score.setText(_translate("MainWindow", "00"))
        self.rules_button.setText(_translate("MainWindow", "Rules"))
        self.menu_text.setText(_translate("MainWindow", "6 Nimmt!"))
        self.play_btn.setText(_translate("MainWindow", "Play"))
        self.exit_btn.setText(_translate("MainWindow", "Exit"))
        self.settings_button.setText(_translate("MainWindow", "Settings"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
