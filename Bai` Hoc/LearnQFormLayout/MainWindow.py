# Form implementation generated from reading ui file 'D:\Python\pythonProject\Bai` Hoc\LearnQFormLayout\MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(537, 340)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.fullNameLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.fullNameLabel.setObjectName("fullNameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.fullNameLabel)
        self.fullNameLineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.fullNameLineEdit.setObjectName("fullNameLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.fullNameLineEdit)
        self.userNameLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.userNameLabel.setObjectName("userNameLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.userNameLabel)
        self.userNameLineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.userNameLineEdit.setObjectName("userNameLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.userNameLineEdit)
        self.passwordLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.passwordLabel.setObjectName("passwordLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.passwordLabel)
        self.passwordLineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.passwordLineEdit)
        self.confirmPasswordLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.confirmPasswordLabel.setObjectName("confirmPasswordLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.confirmPasswordLabel)
        self.confirmPasswordLineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.confirmPasswordLineEdit.setObjectName("confirmPasswordLineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.confirmPasswordLineEdit)
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setEnabled(True)
        self.pushButton.setMinimumSize(QtCore.QSize(100, 30))
        self.pushButton.setMaximumSize(QtCore.QSize(100, 30))
        self.pushButton.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setItalic(False)
        font.setStrikeOut(False)
        self.pushButton.setFont(font)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("background-color: rgb(218, 218, 218);")
        self.pushButton.setObjectName("pushButton")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.pushButton)
        self.verticalLayout.addLayout(self.formLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 537, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.fullNameLabel.setText(_translate("MainWindow", "Full Name:"))
        self.userNameLabel.setText(_translate("MainWindow", "User Name:"))
        self.passwordLabel.setText(_translate("MainWindow", "Password:"))
        self.confirmPasswordLabel.setText(_translate("MainWindow", "Confirm Password:"))
        self.pushButton.setText(_translate("MainWindow", "Sign Up"))
