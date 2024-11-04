from MainWindowThay import Ui_MainWindow


class MainWindowExThay(Ui_MainWindow):
    def __init__(self):
        pass
    def setupUi(self, MainWindowThay):
        super().setupUi(MainWindowThay)
        self.MainWindowThay=MainWindowThay
    def show(self):
        self.MainWindowThay.show()