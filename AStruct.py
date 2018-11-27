import sys
from PyQt5 import QtWidgets, QtGui, QtCore
import pandas as pd
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction, qApp, QStyle

import design
from InfoMessage import Ui_InfoMessage

from abc import ABCMeta, abstractmethod, abstractproperty, ABC

class Menu(object):
    def __init__(self, window):
        self.SetMenuFunc(window)
        self.CreateMenuBarFunc(window)

    def SetMenuFunc(self, window):
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

    def CreateMenuBarFunc(self, window):
        window.menubar = window.menuBar()
        window.fileMenu = window.menubar.addMenu('&File')
        window.Line = window.menubar.addMenu('&Line')
        window.Line.addAction(window.searchAction)
        window.Line.addAction(window.rebootAction)
        window.fileMenu.addAction(window.exitAction)
        window.fileMenu.addAction(window.DBrebuild)

class Example (object):

    def build(self):
        self.pushButton.clicked.connect(self.AddNew)
        self.label.setPixmap(QtGui.QPixmap('NewAdd.png'))
        self.label.setScaledContents(True)

    def CreateMenuFunc(self):
        Menu1 = Menu(self)