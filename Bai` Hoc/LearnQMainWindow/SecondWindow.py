from PyQt6 import QtCore
from PyQt6.QtWidgets import QLabel, QLineEdit, QPushButton

class SecondWindow(object):
    def __init__(self,parent):
        self.parent=parent
    def setupUi(self, MainWindow):
        self.MainWindow=MainWindow
        self.MainWindow.setWindowTitle("Tran Duc Trung Kien - Second Window")
        self.MainWindow.resize(381, 110)

        self.label = QLabel(parent=MainWindow)
        self.label.setText("Change Name:")
        self.label.setGeometry(QtCore.QRect(20, 10, 91, 16))

        self.lineEditFullName = QLineEdit(parent=MainWindow)
        self.lineEditFullName.setGeometry(QtCore.QRect(20, 40, 351, 22))

        self.pushButtonPurple = QPushButton(parent=MainWindow)
        self.pushButtonPurple.setText("Purple")
        self.pushButtonPurple.setGeometry(QtCore.QRect(40, 70, 93, 28))

        self.pushButtonPink = QPushButton(parent=MainWindow)
        self.pushButtonPink.setText("Pink")
        self.pushButtonPink.setGeometry(QtCore.QRect(150, 70, 93, 28))

        self.pushButtonClose = QPushButton(parent=MainWindow)
        self.pushButtonClose.setGeometry(QtCore.QRect(250, 70, 93, 28))
        self.pushButtonClose.setText("Close")

        self.lineEditFullName.setText(self.parent.lineEditName.text())

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.lineEditFullName.textChanged.connect(self.parent.lineEditName.setText)
        self.pushButtonClose.clicked.connect(self.processClose)
        self.pushButtonPurple.clicked.connect(self.parent.changePurpleColor)
        self.pushButtonPink.clicked.connect(self.parent.changePinkColor)
    def processClose(self):
        self.MainWindow.close()
        self.parent.secondWindow=None