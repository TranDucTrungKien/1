
from PyQt6.QtGui import QMovie

from MainWindow import Ui_MainWindow

class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        self.movie = None


    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
    def show(self):
        self.MainWindow.show()

    def process(self):
        #create QMovie instance
        self.movie=QMovie("siu.gif")
        #set movie object for label
        self.label_3.setMovie(self.movie)
        #call start method
        self.movie.start()

    price_laptop = 25
    price_robot = 100
    num_fake_laptop = 0
    num_fake_robot = 0
    num_real_laptop = 0
    num_real_robot = 0

    money_fake_laptop = 0
    money_fake_robot = 0
    money_real_laptop = 0
    money_real_robot = 0

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()

    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButtonBuy.clicked.connect(self.process_purchase)

    def process_purchase(self):
        n_laptop = 0
        n_robot = 0
        try:
            n_laptop = int(self.lineEditSoMacbook.text())
        except ValueError:
            n_laptop = 0
        try:
            n_robot = int(self.lineEditSoGOAT.text())
        except ValueError:
            n_robot = 0

        if self.radioButtonFake.isChecked():
            money_laptop = n_laptop * self.price_laptop * 0.9
            money_robot = n_robot * self.price_robot * 0.9
            self.num_fake_laptop += n_laptop
            self.num_fake_robot += n_robot
            self.money_fake_laptop += money_laptop
            self.money_fake_robot += money_robot
        else:
            money_laptop = n_laptop * self.price_laptop
            money_robot = n_robot * self.price_robot
            self.num_real_laptop += n_laptop
            self.num_real_robot += n_robot
            self.money_real_laptop += money_laptop
            self.money_real_robot += money_robot

        # Update the statistics section
        self.lineEditSoMacbookfake.setText(str(self.num_fake_laptop))
        self.lineEditGOATfake.setText(str(self.num_fake_robot))
        self.lineEditSoMacbookreal.setText(str(self.num_real_laptop))
        self.lineEditSoGOATreal.setText(str(self.num_real_robot))
        self.lineEditTienMacbookfake.setText(str(self.money_fake_laptop))
        self.lineEditTienGOATfake.setText(str(self.money_fake_robot))
        self.lineEditTienMacbookreal.setText(str(self.money_real_laptop))
        self.lineEditTienGOATreal.setText(str(self.money_real_robot))

