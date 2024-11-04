from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QMovie

from MainWindow import Ui_MainWindow


class MainWindowEx(Ui_MainWindow):
    def __init__(self):
        pass
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        #change text
        self.changeTextpushButton.clicked.connect(self.processChangeText)
        #change font
        self.fontSizepushButton.clicked.connect(self.processChangeFontSize)
        #set align text
        self.alignLeftpushButton.clicked.connect(self.processAlignLeft)
        self.alignCenterpushButton.clicked.connect(self.processAlignCenter)
        self.alignRightpushButton.clicked.connect(self.processAlignRight)
        #change image with PNG format
        self.showPNGpushButton.clicked.connect(self.processChangePNG)
        #change image with GIF format
        self.showGIFpushButton.clicked.connect(self.processChangeGIF)
    def show(self):
        self.MainWindow.show()
    def processChangeText(self):
        self.titleLabel.setText("https://www.facebook.com/Kjndapoet/")
    def processChangeFontSize(self):
        #get font object
        font=self.titleLabel.font()
        #change font size
        font.setPointSize(20)
        #set italic
        font.setItalic(True)
        #set bold
        font.setBold(True)
        #set font name
        font.setFamily("cambria")
        #re-assign font
        self.titleLabel.setFont(font)
    def processAlignLeft(self):
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignLeft)
    def processAlignCenter(self):
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
    def processAlignRight(self):
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignRight)
    def processChangePNG(self):
        #create QPixmap instance
        pixmap=QPixmap("images/ThatTinh1.jpg")
        #set pixmap for label
        self.imageLabel.setPixmap(pixmap)
    def processChangeGIF(self):
        #create QMovie instance
        movie=QMovie("images/siu.gif")
        #set movie object for label
        self.imageLabel.setMovie(movie)
        #call start method
        movie.start()