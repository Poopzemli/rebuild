import sys
from PyQt5 import QtWidgets, QtGui
import pandas as pd

import design

class ExapleApp (QtWidgets.QMainWindow, design.Ui_MainWindow):

    DBase = 'DataBase/'
    DFile = 'House.csv'

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

    def ReadDF(self, file):
        df = pd.read_csv(self.DBase + file, header=0, sep=',')
        for item in df.pic:
            nf = QtWidgets.QFrame()
            nf.setStyleSheet(".QLabel { max-height: 170; max-width: 170; min-width: 170; min-height: 170; border: 1px solid white; }")
            nb = QtWidgets.QPushButton(nf)
            nb.clicked.connect(lambda: self.DFrameSendInfo(df.ID))
            nb.setText("Информация")
            nb.move(35, 190)

            nl = QtWidgets.QLabel(nf)
            nl.move(4, 5)
            nl.setPixmap(QtGui.QPixmap(item))
            nl.setScaledContents(True)

            self.gridLayout.addWidget(nf, self.NewPositionV, self.NewPositionH)
            self.NewPositionH += 1
            if self.NewPositionH == 4:
                self.NewPositionV += 1
                self.NewPositionH = 0

    def AddNew(self):
        nf = QtWidgets.QFrame()
        nf.setStyleSheet(".QLabel { max-height: 170; max-width: 170; min-width: 170; min-height: 170; border: 1px solid white; }")
        nb = QtWidgets.QPushButton(nf)
        nb.setText("Информация")
        nb.move(35, 190)

        pic, addr, plosh, kom, tip, price, index, ok = self.GetAddInformation()

        if ok:
            nl = QtWidgets.QLabel(nf)
            nl.move(4, 5)
            nl.setPixmap(QtGui.QPixmap(pic + ".jpg"))
            nl.setScaledContents(True)

            self.gridLayout.addWidget(nf, self.NewPositionV, self.NewPositionH)
            self.NewPositionH += 1
            if self.NewPositionH == 4:
                self.NewPositionV += 1
                self.NewPositionH = 0
        df = pd.read_csv(self.DBase + self.DFile, sep=',', header=0, encoding='utf-8', index_col=False)
        new_line = pd.DataFrame({'ID':len(df.index)+1, 'Адрес':addr, 'Площадь':plosh, 'Комнаты':kom, 'Тип сделки':tip, 'Цена':price, 'Индекс':index, 'pic':pic}, index=range(1))
        print(new_line)
        nb.clicked.connect(lambda : self.DFrameSendInfo(df.ID))
        df = df.append(new_line)
        print(df)
        df.to_csv(self.DBase + self.DFile, sep=',', encoding='utf-8', line_terminator='\n', index=False)

    def DFrameSendInfo(self, ID):
        print('CLICKED!')
    def GetAddInformation(self):
        pic, ok = QtWidgets.QInputDialog().getText(self, 'InputText', 'Адрес изображения:?')
        if ok:
            addr, ok = QtWidgets.QInputDialog().getText(self, 'InputText', 'Адрес квартиры:?')
            if ok:
                plosh, ok = QtWidgets.QInputDialog().getText(self, 'InputText', 'Площадь квартиры:?')
                if ok:
                    kom, ok = QtWidgets.QInputDialog().getText(self, 'InputText', 'Кол-во квартир:?')
                    if ok:
                        type, ok = QtWidgets.QInputDialog().getText(self, 'InputText', 'Тип сделки:?')
                        if ok:
                            price, ok = QtWidgets.QInputDialog().getText(self, 'InputText', 'Цена квартиры:?')
                            if ok:
                                index, ok = QtWidgets.QInputDialog().getText(self, 'InputText', 'Почтовый индекс:?')
                                if ok: return pic, addr, plosh, kom, type, price, index, ok

def main():
    app = QtWidgets.QApplication(sys.argv)
    w = ExapleApp()
    w.show()
    app.exec_()

if __name__ == "__main__":
    main()