from PyQt5.QtWidgets import QWidget, QMainWindow, QVBoxLayout, QFrame

class configPage(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        self.cwidget()
        self.content()

    def initUI(self):
        self.resize(400, 400)
        self.setWindowTitle('CONFIGURATION')
        self.setMinimumSize(400, 400)

    def cwidget(self):
        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)
        self.vlayout = QVBoxLayout(self.centralWidget)

    def content(self):
        self.framePort = QFrame(self.centralWidget)
        self.framePort.setFrameShape(QFrame.StyledPanel)
        self.framePort.setFrameShadow(QFrame.Raised)
        self.framePort.setObjectName("framePort")
        self.vlayout.addWidget(self.framePort)

        self.framedPin = QFrame(self.centralWidget)
        self.framedPin.setFrameShape(QFrame.StyledPanel)
        self.framedPin.setFrameShadow(QFrame.Raised)
        self.framedPin.setObjectName("framePin")
        self.vlayout.addWidget(self.framedPin)

        self.frameaPin = QFrame(self.centralWidget)
        self.frameaPin.setFrameShape(QFrame.StyledPanel)
        self.frameaPin.setFrameShadow(QFrame.Raised)
        self.frameaPin.setObjectName("frameaPin")
        self.vlayout.addWidget(self.frameaPin)

        self.setButtonFrame = QFrame(self.centralWidget)
        self.setButtonFrame.setFrameShape(QFrame.StyledPanel)
        self.setButtonFrame.setFrameShadow(QFrame.Raised)
        self.setButtonFrame.setObjectName("setButtonFrame")
        self.vlayout.addWidget(self.setButtonFrame)



