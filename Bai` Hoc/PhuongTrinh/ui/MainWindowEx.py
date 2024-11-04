

from MainWindow import Ui_MainWindow
from factorial import factoria
class MainWindowEx(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
    def processSignalAndSlot(self):
        self.pushButtonExit.clicked.connect(self.processExit)
        self.pushButtonGiai.clicked.connect(self.processGiai)
    def processExit(self):
        self.MainWindow.close()
    def processGiai(self):
        try:
            n = int(self.lineEditNhapN.text())
            result = factoria(n)
            self.lineEditKetQua.setText(f"{n}! = {result}")
        except:
            self.lineEditKetQua.setText("May sai roi con cho")




