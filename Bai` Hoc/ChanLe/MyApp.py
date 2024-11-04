from PyQt6.QtWidgets import QApplication, QMainWindow

from MainWindowEx import MainWindowEx
#Create QApplication instance
app=QApplication([])
#Create QMainWindow instance
qMainWindow=QMainWindow()
#Create MyQMainWindowExt instance
myWindow=MainWindowEx()
#call setupUi method for MyQMainWindowExt
myWindow.setupUi(qMainWindow)
#call methods for Signal and slots processing
myWindow.setupSignalAndSlot()
#call show method to show Window
qMainWindow.show()
#start Event loop
app.exec()