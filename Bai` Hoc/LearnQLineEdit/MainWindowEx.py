from PyQt6.QtWidgets import QCompleter
from PyQt6.QtCore import Qt
from MainWindow import Ui_MainWindow


class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        pass

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        cities = ["Biên Hòa", "Cà Mau", "Nha Trang", "Cali", "Hồ Chí Minh", "Cần Em"]

        completer = QCompleter(cities)
        completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)  # Bỏ phân biệt chữ hoa chữ thường

        self.lineEditCity.setCompleter(completer)

    def show(self):
        self.MainWindow.show()
