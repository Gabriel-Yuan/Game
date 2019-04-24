# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MyWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from TankBattle import Game as TankBattleGame
from EatBeans import Game as EatBeansGame
from FlappyBird import Game as FlappyBirdGame
from Sokoban import Game as SokobanGame

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setFamily("arial")
        font.setPointSize(15)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.TankBattle = QtWidgets.QPushButton(self.centralwidget)
        self.TankBattle.setGeometry(QtCore.QRect(200, 120, 400, 50))
        self.TankBattle.setObjectName("TankBattle")
        self.EatBeans = QtWidgets.QPushButton(self.centralwidget)
        self.EatBeans.setGeometry(QtCore.QRect(200, 240, 400, 50))
        self.EatBeans.setObjectName("EatBeans")
        self.Sokoban = QtWidgets.QPushButton(self.centralwidget)
        self.Sokoban.setGeometry(QtCore.QRect(200, 180, 400, 50))
        self.Sokoban.setObjectName("Sokoban")
        self.FlappyBird = QtWidgets.QPushButton(self.centralwidget)
        self.FlappyBird.setGeometry(QtCore.QRect(200, 300, 400, 50))
        self.FlappyBird.setObjectName("FlappyBird")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 50, 241, 30))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 36))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PyGame小游戏合集"))
        self.TankBattle.setText(_translate("MainWindow", "坦克大战"))
        self.EatBeans.setText(_translate("MainWindow", "吃豆豆"))
        self.Sokoban.setText(_translate("MainWindow", "推箱子"))
        self.FlappyBird.setText(_translate("MainWindow", "FlappyBird"))
        self.label.setText(_translate("MainWindow", "PyGame小游戏合集"))
        self.TankBattle.clicked.connect(self.on_click1)
        self.Sokoban.clicked.connect(self.on_click2)
        self.EatBeans.clicked.connect(self.on_click3)
        self.FlappyBird.clicked.connect(self.on_click4)

    @pyqtSlot()
    def on_click1(self):
        TankBattleGame.main()

    @pyqtSlot()
    def on_click2(self):
        SokobanGame.main()

    @pyqtSlot()
    def on_click3(self):
        EatBeansGame.main(EatBeansGame.initialize())

    @pyqtSlot()
    def on_click4(self):
        FlappyBirdGame.main()