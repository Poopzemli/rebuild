import sys
from PyQt5 import QtWidgets, QtGui, QtCore
import pandas as pd
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction, qApp, QStyle

import design
from InfoMessage import Ui_InfoMessage

from abc import ABCMeta, abstractmethod, abstractproperty, ABC

class MenuFunctions(object):
    def __init__(self):
        pass

    def openDataFrameFile(self):
        self.df = pd.read_csv(self.DBase + self.DFile, header=0, sep=',')

    def dataBaseChooseFile(self):
        text, ok = QtWidgets.QInputDialog.getText(self, "Input dialog", "Data Base Name")
        if ok:
            self.DFile = text + ".csv"
        self.reboot()

    def lineSearch(self):
        for i in self.tileList:
            i.deleteLater()
        self.NewPositionH = 1
        self.NewPositionV = 0
        self.tileList = []
        text, ok = QtWidgets.QInputDialog.getText(self, "Input dialog", "Search Word's")
        if ok:
            self.openDataFrameFile()
            variously = df.loc[df.pic == "pic/"+text]
            for item in variously.pic:
                self.nf = QtWidgets.QFrame()
                #self.n += 1
                self.nf.setStyleSheet(".QLabel { max-height: 170; max-width: 170; min-width: 170; min-height: 170; border: 1px solid white; }" + "QPushButton#CloseButton" + str(self.n) + " {background-color: red; max-width: 30px;}")
                print(item)
                k = df[df.pic == item]['ID']
                k.index = [1]
                print(k[1])
                self.nf.setObjectName("NF" + str(k[1]))
                nb = QtWidgets.QPushButton(self.nf)
                nb.setObjectName(str(k[1]))
                nb.clicked.connect(self.DFrameSendInfo)
                nb.setText("Информация")
                nb.move(35, 190)

                nl = QtWidgets.QLabel(self.nf)
                nl.move(4, 5)
                nl.setPixmap(QtGui.QPixmap(item))
                nl.setScaledContents(True)

                self.tileList.append(self.nf)

                self.gridLayout.addWidget(self.nf, self.NewPositionV, self.NewPositionH)
                self.NewPositionH += 1
                if self.NewPositionH == 4:
                    self.NewPositionV += 1
                    self.NewPositionH = 0

    def reboot(self):
        pass

class Menu(object):
    def __init__(self, window):
        self.setMenuFunc(window)
        self.createMenuBarFunc(window)

    def setMenuFunc(self, window):
        window.exitAction = QAction(QIcon('exit.png'), '&Exit', window)
        window.exitAction.setShortcut('Ctrl+Q')
        window.exitAction.triggered.connect(qApp.quit)

        window.DBrebuild = QAction(QIcon(), '&Choose DB', window)
        window.DBrebuild.triggered.connect(window.DataBaseChooseFile)

        window.searchAction = QAction(QIcon(), '&Search', window)
        window.searchAction.setShortcut('Shift+F')
        window.searchAction.triggered.connect(window.LineSearch)

        window.rebootAction = QAction(QIcon(), '&Reboot', window)
        window.rebootAction.setShortcut('Shift+R')
        window.rebootAction.triggered.connect(window.reboot)

    def createMenuBarFunc(self, window):
        window.menubar = window.menuBar()
        window.fileMenu = window.menubar.addMenu('&File')
        window.Line = window.menubar.addMenu('&Line')
        window.Line.addAction(window.searchAction)
        window.Line.addAction(window.rebootAction)
        window.fileMenu.addAction(window.exitAction)
        window.fileMenu.addAction(window.DBrebuild)

class Example (object):

    def DBase(self): self.DBase = 'DataBase/'
    def DFile(self): self.DFile = 'House.csv'
    def tileList(self): self.tileList = []

    def build(self):
        self.pushButton.clicked.connect(self.AddNew)
        self.label.setPixmap(QtGui.QPixmap('NewAdd.png'))
        self.label.setScaledContents(True)

    def createMenuFunc(self):
        Menu(self)