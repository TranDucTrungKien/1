from PyQt6.QtWidgets import QApplication, QMainWindow

from MainWindowExThay import MainWindowExThay

app=QApplication([])
myWindowThay= MainWindowExThay()
myWindowThay.setupUi(QMainWindow())
myWindowThay.show()
app.exec()