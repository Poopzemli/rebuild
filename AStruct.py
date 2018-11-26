import sys
from PyQt5 import QtWidgets, QtGui, QtCore
import pandas as pd
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction, qApp, QStyle

import design
from InfoMessage import Ui_InfoMessage

from abc import ABC, abstractmethod, abstractproperty

class Example (ABC, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

