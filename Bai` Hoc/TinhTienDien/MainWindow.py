# Form implementation generated from reading ui file 'D:\Python\pythonProject\Bai` Hoc\TinhTienDien\MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(584, 475)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 10, 55, 16))
        self.label.setObjectName("label")
        self.formLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(29, 59, 521, 161))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_5)
        self.lineEditOld = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditOld.setFont(font)
        self.lineEditOld.setObjectName("lineEditOld")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEditOld)
        self.lineEditNew = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditNew.setFont(font)
        self.lineEditNew.setObjectName("lineEditNew")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEditNew)
        self.lineEditSoHo = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditSoHo.setFont(font)
        self.lineEditSoHo.setObjectName("lineEditSoHo")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEditSoHo)
        self.lineEditSokWh = QtWidgets.QLineEdit(parent=self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditSokWh.setFont(font)
        self.lineEditSokWh.setObjectName("lineEditSokWh")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEditSokWh)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.formLayout.setItem(5, QtWidgets.QFormLayout.ItemRole.FieldRole, spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.formLayout.setItem(3, QtWidgets.QFormLayout.ItemRole.FieldRole, spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.formLayout.setItem(1, QtWidgets.QFormLayout.ItemRole.FieldRole, spacerItem2)
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 240, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(150, 240, 401, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: rgb(255, 170, 255);")
        self.label_7.setText("")
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(149, 320, 401, 81))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButtonSHBT = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.pushButtonSHBT.setObjectName("pushButtonSHBT")
        self.gridLayout.addWidget(self.pushButtonSHBT, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        self.pushButtonKinhDoanh = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.pushButtonKinhDoanh.setObjectName("pushButtonKinhDoanh")
        self.gridLayout.addWidget(self.pushButtonKinhDoanh, 0, 1, 1, 1)
        self.pushButtonnSanXuat = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.pushButtonnSanXuat.setObjectName("pushButtonnSanXuat")
        self.gridLayout.addWidget(self.pushButtonnSanXuat, 0, 2, 1, 1)
        self.pushButtonHuongDan = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.pushButtonHuongDan.setObjectName("pushButtonHuongDan")
        self.gridLayout.addWidget(self.pushButtonHuongDan, 1, 1, 1, 1)
        self.pushButtonThoat = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.pushButtonThoat.setObjectName("pushButtonThoat")
        self.gridLayout.addWidget(self.pushButtonThoat, 1, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 584, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButtonThoat.clicked.connect(MainWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.label_2.setText(_translate("MainWindow", "Chỉ số cũ:"))
        self.label_3.setText(_translate("MainWindow", "Chỉ số mới:"))
        self.label_4.setText(_translate("MainWindow", "Số hộ (SHBT):"))
        self.label_5.setText(_translate("MainWindow", "Số kWh dùng:"))
        self.label_6.setText(_translate("MainWindow", "Số tiền sẽ thu:"))
        self.pushButtonSHBT.setText(_translate("MainWindow", "SHBT"))
        self.pushButton.setText(_translate("MainWindow", "Tính tiếp"))
        self.pushButtonKinhDoanh.setText(_translate("MainWindow", "Kinh doanh"))
        self.pushButtonnSanXuat.setText(_translate("MainWindow", "Sản xuất"))
        self.pushButtonHuongDan.setText(_translate("MainWindow", "Hướng dẫn"))
        self.pushButtonThoat.setText(_translate("MainWindow", "Thoát"))
