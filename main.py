import sys
from PyQt5 import QtWidgets, QtGui, QtCore
import pandas as pd
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction, qApp, QStyle

import design
from InfoMessage import Ui_InfoMessage

class ExapleApp (QtWidgets.QMainWindow, design.Ui_MainWindow):

    DBase = 'DataBase/'
    DFile = 'House.csv'
    tileList = []

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.Build()

    def Build(self):
        self.NewPositionH = 1
        self.NewPositionV = 0
        self.pushButton.clicked.connect(self.AddNew)
        self.label.setPixmap(QtGui.QPixmap('NewAdd.png'))
        self.label.setScaledContents(True)
        self.ReadDF(self.DFile)
        self.CreateMenuFunc()

    def CreateMenuFunc(self):
        exitAction = QAction(QIcon('exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(qApp.quit)

        DBrebuild = QAction(QIcon(), '&Choose DB', self)
        DBrebuild.triggered.connect(self.DataBaseChooseFile)

        searchAction = QAction(QIcon(), '&Search', self)
        searchAction.setShortcut('Shift+F')
        searchAction.triggered.connect(self.LineSearch)

        rebootAction = QAction(QIcon(), '&Reboot', self)
        rebootAction.setShortcut('Shift+R')
        rebootAction.triggered.connect(self.reboot)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        Line = menubar.addMenu('&Line')
        Line.addAction(searchAction)
        Line.addAction(rebootAction)
        fileMenu.addAction(exitAction)
        fileMenu.addAction(DBrebuild)

    def DataBaseChooseFile(self):
        text, ok = QtWidgets.QInputDialog.getText(self, "Input dialog", "Data Base Name")
        if ok:
            self.DFile = text+".csv"
        self.reboot()

    def LineSearch(self):
        for i in self.tileList:
            i.deleteLater()
        #self.n = 0
        self.NewPositionH = 1
        self.NewPositionV = 0
        self.tileList = []
        text, ok = QtWidgets.QInputDialog.getText(self, "Input dialog", "Search Word's")
        if ok:
            df = pd.read_csv(self.DBase + self.DFile, header=0, sep=',')
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
        for i in self.tileList:
            try:
                i.deleteLater()
            except RuntimeError: pass
        self.tileList = []
        self.n = 0
        self.NewPositionH = 1
        self.NewPositionV = 0
        self.ReadDF(self.DFile)

    def ReadDF(self, file):
        df = pd.read_csv(self.DBase + file, header=0, sep=',')
        df.reset_index(drop=True)
        self.n = 0
        for item in df.pic:
            self.nf = QtWidgets.QFrame()
            #nf.setObjectName("UFrame_" + str(n))
            self.n += 1
            self.nf.setStyleSheet(".QLabel { max-height: 170; max-width: 170; min-width: 170; min-height: 170; border: 1px solid white; }" + "QPushButton#CloseButton" + str(self.n) + " {background-color: red; max-width: 30px;}")
            self.nf.setObjectName("NF" + str(self.n))
            cd = QtWidgets.QPushButton(self.nf)
            cd.setText('X')
            cd.setObjectName("CloseButton" + str(self.n))
            cd.move(130, 191)
            cd.clicked.connect(lambda : self.delete())
            nb = QtWidgets.QPushButton(self.nf)
            nb.setObjectName(str(self.n))
            k = df[df.pic == item]['Адрес']
            #print(k)
            nb.clicked.connect(self.DFrameSendInfo)
            nb.setText("Информация")
            nb.move(5, 190)
            k = df[df.pic == item]['buff']
            k.index = [1]
            #print(k)
            if k[1] == 1:
                self.nf.setStyleSheet(".QLabel { max-height: 170; max-width: 170; min-width: 170; min-height: 170; border: 1px solid white; }"
                + "QPushButton#CloseButton" + str(self.n) + " {background-color: red; max-width: 30px;}"
                + ".QFrame#NF"+str(self.n)+" {background-color: green}")

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

    def delete(self):
        try:
            df = pd.read_csv(self.DBase + self.DFile, header=0, sep=',')
            sender = self.sender()
            k = int(sender.objectName()[len(sender.objectName())-1])
            print(k)
            self.tileList[k-1].deleteLater()
            df.drop([k-1], axis=0, inplace=True)
            df.to_csv(self.DBase + self.DFile, sep=',', encoding='utf-8', line_terminator='\n', index=False)
        except: self.reboot()
    def AddNew(self):
        nf = QtWidgets.QFrame()
        nf.setStyleSheet(".QLabel { max-height: 170; max-width: 170; min-width: 170; min-height: 170; border: 1px solid white; }" + "QPushButton#CloseButton" + str(self.n +1) + " {background-color: red; max-width: 30px;}")
        nb = QtWidgets.QPushButton(nf)
        self.n += 1
        cd = QtWidgets.QPushButton(nf)
        cd.setText('X')
        cd.setObjectName("CloseButton" + str(self.n))
        cd.move(130, 191)
        cd.clicked.connect(lambda: self.delete())
        nb.setObjectName(str(self.n))
        nb.clicked.connect(self.DFrameSendInfo)
        nb.setText("Информация")
        nb.move(10, 190)
        try:
            pic, addr, plosh, kom, tip, price, index, ok = self.GetAddInformation()
        except TypeError:
            ok = False
        if ok:
            nl = QtWidgets.QLabel(nf)
            nl.move(4, 5)
            nl.setPixmap(QtGui.QPixmap(pic + ".jpg"))
            nl.setScaledContents(True)

            self.tileList.append(nf)

            self.gridLayout.addWidget(nf, self.NewPositionV, self.NewPositionH)
            self.NewPositionH += 1
            if self.NewPositionH == 4:
                self.NewPositionV += 1
                self.NewPositionH = 0
            df = pd.read_csv(self.DBase + self.DFile, sep=',', header=0, encoding='utf-8', index_col=False)
            new_line = pd.DataFrame({'ID':len(df.index)+1, 'Адрес':addr, 'Площадь':plosh, 'Комнаты':kom, 'Тип сделки':tip, 'Цена':price, 'Индекс':index, 'pic':pic}, index=range(1))
            IDS = len(df.index) + 1
            nb.clicked.connect(lambda : self.DFrameSendInfo(IDS))
            df = df.append(new_line)
            print(df)
            df.to_csv(self.DBase + self.DFile, sep=',', encoding='utf-8', line_terminator='\n', index=False)

    def DFrameSendInfo(self, base = '1'):
        sender = self.sender()
        df = pd.read_csv(self.DBase + self.DFile, sep=',', header=0, encoding='utf-8', index_col=False)
        self.window = QtWidgets.QMainWindow()
        ui = Ui_InfoMessage()
        ui.setupUi(self.window)
        #print(sender.objectName())
        ID = int(sender.objectName())
        print(ID)
        ui.label_13.setText(str(ID))
        ui.label_14.setText(df[df.ID == ID]['Адрес'][ID-1])
        #print(df[df.ID == ID]['Адрес'][ID-1])
        ui.label_15.setText(str(df[df.ID == ID]['Площадь'][ID-1]))
        ui.label_16.setText(str(df[df.ID == ID]['Комнаты'][ID-1]))
        ui.label_17.setText(df[df.ID == ID]['Тип сделки'][ID-1])
        ui.label_18.setText(str(df[df.ID == ID]['Цена'][ID-1]) + " руб")
        ui.label_19.setText(str(df[df.ID == ID]['Индекс'][ID-1]))
        try:
            df = pd.read_csv(self.DBase + 'Prod.csv', sep=',', header=0, encoding='utf-8', index_col=False)
            ui.label_20.setText(str(df[df.ID == ID]['Адрес'][ID-1]))
            ui.label_21.setText(str(df[df.ID == ID]['Фамилия'][ID-1]) + ' ' + str(df[df.ID == ID]['Имя'][ID-1]) + ' ' + str(df[df.ID == ID]['Отчество'][ID-1]))
            ui.label_22.setText(str(df[df.ID == ID]['Номер'][ID-1]))
        except IndexError:
            pass
        self.window.show()
    def GetAddInformation(self):
        pic, ok = QtWidgets.QInputDialog().getText(self, 'InputText', 'Адрес изображения:?')
        if ok:
            addr, ok = QtWidgets.QInputDialog().getText(self, 'InputText', 'Адрес квартиры:?')
            if ok:
                plosh, ok = QtWidgets.QInputDialog().getText(self, 'InputText', 'Площадь квартиры:?')
                if ok:
                    kom, ok = QtWidgets.QInputDialog().getText(self, 'InputText', 'Кол-во комнат:?')
                    if ok:
                        type, ok = QtWidgets.QInputDialog().getText(self, 'InputText', 'Тип сделки:?')
                        if ok:
                            price, ok = QtWidgets.QInputDialog().getText(self, 'InputText', 'Цена квартиры:?')
                            if ok:
                                index, ok = QtWidgets.QInputDialog().getText(self, 'InputText', 'Почтовый индекс:?')
                                if ok: return pic, addr, plosh, kom, type, price, index, ok

    def __del__(self):
        try:
            df = pd.read_csv(self.DBase + self.DFile, sep=',', header=0, encoding='utf-8', index_col=False)
            df.reset_index(drop=True)
            df.to_csv(self.DBase + self.DFile, sep=',', encoding='utf-8', line_terminator='\n', index=False)
        except: pass

def main():
    app = QtWidgets.QApplication(sys.argv)
    w = ExapleApp()
    w.setWindowTitle("АСУРА - Автоматизированная сист...")
    w.setWindowIcon(QIcon.fromTheme('emblem-system'))
    w.show()
    app.exec_()

if __name__ == "__main__":
    main()