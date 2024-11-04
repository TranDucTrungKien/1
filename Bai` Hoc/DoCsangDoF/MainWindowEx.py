from MainWindow import Ui_MainWindow

class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        pass
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.pushButtonConvert.clicked.connect(self.convertCtoF)

    def convertCtoF(self):
        try:
            # Get the Fahrenheit value from the input field
            fahrenheit = float(self.lineEditdoF.text())
            # Perform the conversion
            celsius = (fahrenheit - 32) / 1.8
            # Display the Celsius result
            self.lineEditdoC.setText(f"{celsius:.3f}")
        except ValueError:
            # Show error if input is invalid
            self.lineEditdoC.setText("Sai roi con cho")
    def show(self):
        self.MainWindow.show()