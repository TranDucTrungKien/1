from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindowThay):
        MainWindowThay.setObjectName("MainWindow")
        MainWindowThay.resize(542, 450)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindowThay)
        self.centralwidget.setObjectName("centralwidget")
        self.titleLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(40, 10, 381, 41))
        self.titleLabel.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.titleLabel.setObjectName("titlelabel")
        self.showPNGpushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.showPNGpushButton.setGeometry(QtCore.QRect(140, 100, 121, 31))
        self.showPNGpushButton.setObjectName("ShowPNGpushButton")
        self.showGIFpushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.showGIFpushButton.setGeometry(QtCore.QRect(270, 100, 121, 31))
        self.showGIFpushButton.setObjectName("showGIFpushButton")
        self.imageLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.imageLabel.setGeometry(QtCore.QRect(120, 140, 271, 231))
        self.imageLabel.setText("")
        self.imageLabel.setPixmap(QtGui.QPixmap("images/ThatTinh1.jpg.PNG"))
        self.imageLabel.setScaledContents(True)
        self.imageLabel.setObjectName("imageLabel")
        self.changeTextpushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.changeTextpushButton.setGeometry(QtCore.QRect(30, 60, 75, 23))
        self.changeTextpushButton.setObjectName("changeTextpushButton")
        self.alignLeftpushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.alignLeftpushButton.setGeometry(QtCore.QRect(240, 60, 75, 23))
        self.alignLeftpushButton.setObjectName("alignLeftpushButton")
        self.alignCenterpushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.alignCenterpushButton.setGeometry(QtCore.QRect(330, 60, 75, 23))
        self.alignCenterpushButton.setObjectName("alignCenterpushButton")
        self.alignRightpushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.alignRightpushButton.setGeometry(QtCore.QRect(410, 60, 75, 23))
        self.alignRightpushButton.setObjectName("alignRightpushButton")
        self.fontSizepushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.fontSizepushButton.setGeometry(QtCore.QRect(120, 60, 75, 23))
        self.fontSizepushButton.setObjectName("fontSizepushButton")
        MainWindowThay.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindowThay)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 542, 22))
        self.menubar.setObjectName("menubar")
        MainWindowThay.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindowThay)
        self.statusbar.setObjectName("statusbar")
        MainWindowThay.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindowThay)
        QtCore.QMetaObject.connectSlotsByName(MainWindowThay)

    def retranslateUi(self, MainWindowThay):
        _translate = QtCore.QCoreApplication.translate
        MainWindowThay.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.titleLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ff0000;\">Tran Duc Trung Kien</span></p></body></html>"))