# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(524, 261)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonLogin = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonLogin.setObjectName("pushButtonLogin")
        self.horizontalLayout.addWidget(self.pushButtonLogin)
        self.pushButtonExit = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonExit.setObjectName("pushButtonExit")
        self.horizontalLayout.addWidget(self.pushButtonExit)
        self.gridLayout.addLayout(self.horizontalLayout, 4, 1, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(0, 48))
        self.label.setMaximumSize(QtCore.QSize(16777215, 50))
        self.label.setStyleSheet("color: rgb(255, 0, 0);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.lineEditPassword = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.gridLayout.addWidget(self.lineEditPassword, 2, 1, 1, 1)
        self.chkSaveInformation = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.chkSaveInformation.setObjectName("chkSaveInformation")
        self.gridLayout.addWidget(self.chkSaveInformation, 3, 1, 1, 1)
        self.lineEditUsername = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditUsername.setObjectName("lineEditUsername")
        self.gridLayout.addWidget(self.lineEditUsername, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 524, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow","Tran Duy Thanh"))
        self.pushButtonLogin.setText(_translate("MainWindow", "Login"))
        self.pushButtonExit.setText(_translate("MainWindow", "Exit"))
        self.label.setText(_translate("MainWindow", "Login Screen"))
        self.chkSaveInformation.setText(_translate("MainWindow", "Save login information"))
        self.label_3.setText(_translate("MainWindow", "Password:"))
        self.label_2.setText(_translate("MainWindow", "User Name:"))