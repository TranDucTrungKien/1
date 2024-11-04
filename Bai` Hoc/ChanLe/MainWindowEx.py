from MainWindow import Ui_MainWindow
from Function import list_prime_numbers, list_even_numbers, list_odd_numbers


class MainWindowEx(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi((MainWindow))
        self.MainWindow=MainWindow
    def showWindow(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.pushButtonOk.clicked.connect(self.slotOK)

    def slotExit(self):
        self.MainWindow.close()
    def slotOK(self):
        try:
            n = int(self.lineEditN.text())
            kq1 = list_odd_numbers(n)
            kq2 = list_even_numbers(n)
            kq3 = list_prime_numbers(n)
            self.lineEditOddNumber.setText(f"{kq1}")
            self.lineEditEvenNumber.setText(f"{kq2}")
            self.lineEditPrimeNumber.setText(f"{kq3}")

        except:
            self.lineEditN.setText("May sai cmnr")

