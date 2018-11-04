import sys
from PyQt5 import QtWidgets, QtGui

import design

class ExapleApp (QtWidgets.QMainWindow, design.Ui_MainWindow):
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

    def AddNew(self):
        nf = QtWidgets.QFrame()
        nf.setStyleSheet(".QLabel { max-height: 170; max-width: 170; min-width: 170; min-height: 170; border: 1px solid white; }")
        nb = QtWidgets.QPushButton(nf)
        nb.setText("Информация")
        nb.move(35, 190)

        name = self.GetNameDialog()

        nl = QtWidgets.QLabel(nf)
        nl.move(4, 5)
        nl.setPixmap(QtGui.QPixmap(name + ".jpg"))
        nl.setScaledContents(True)

        self.gridLayout.addWidget(nf, self.NewPositionV, self.NewPositionH)
        self.NewPositionH += 1
        if self.NewPositionH == 4:
            self.NewPositionV += 1
            self.NewPositionH = 0

    def GetNameDialog(self):
        name, ok = QtWidgets.QInputDialog().getText(self, 'InputText', 'Адрес изображения:?')
        return name
def main():
    app = QtWidgets.QApplication(sys.argv)
    w = ExapleApp()
    w.show()
    app.exec_()

if __name__ == "__main__":
    main()