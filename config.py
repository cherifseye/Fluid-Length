from PyQt5.QtWidgets import QWidget, QMainWindow, QVBoxLayout, QFrame, QLabel, QHBoxLayout, QLineEdit, QSpinBox, QComboBox, QPushButton
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtCore import Qt, QRect

# This page allow us to set our configuration with our Setup Arduino
class configPage(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        self.cwidget()
        self.content()
        self.portContent()
        self.dpinContent()
        self.apinContent()
        self.setButtonContent()

    def initUI(self):
        #The size and the title of the window
        self.resize(300, 300)
        self.setWindowTitle('CONFIGURATION')
        self.setMinimumSize(350, 350)

    def cwidget(self):
        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)
        self.vlayout = QVBoxLayout(self.centralWidget)

    def content(self):
        #In this frame we will put the port content
        self.framePort = QFrame(self.centralWidget)
        self.vlayout.addWidget(self.framePort)
        
        #In this frame we will put the digital pin content
        self.framedPin = QFrame(self.centralWidget)
        self.framedPin.setObjectName("framePin")
        self.vlayout.addWidget(self.framedPin)
        
        #In this frame we will put the analog pin content
        self.frameaPin = QFrame(self.centralWidget)
        self.vlayout.addWidget(self.frameaPin)
         
        #In this frame we will put the set button(test and setup) content
        self.setButtonFrame = QFrame(self.centralWidget)
        self.vlayout.addWidget(self.setButtonFrame)

    def portContent(self):
        self.hlayoutport = QHBoxLayout(self.framePort)
        self.framelabelport = QFrame(self.framePort)
        self.hlayoutport.addWidget(self.framelabelport)
        self.hlayoutlabel = QVBoxLayout(self.framelabelport)

        self.labelport = QLabel(self.framelabelport)
        self.labelport.setText("Port Name")
        self.labelport.setFont(QFont("Arial", 15))
        self.labelport.setStyleSheet("color: #02659D")

        self.hlayoutlabel.addWidget(self.labelport, 0, Qt.AlignHCenter)

        self.framelineeditport = QFrame(self.framePort)
        self.hlayoutport.addWidget(self.framelineeditport)
        self.hlayoutlineedit = QHBoxLayout(self.framelineeditport)

        self.lineeditport = QSpinBox(self.framelineeditport)
        self.lineeditport.setMinimum(0)
        self.lineeditport.setMaximum(13)
        self.lineeditport.setValue(0)
    
        self.lineeditport.setFont(QFont("Arial", 15))
        self.lineeditport.setStyleSheet("color: #02659D")
        self.lineeditport.setAlignment(Qt.AlignCenter)
        self.hlayoutlineedit.addWidget(self.lineeditport)
        
        
    def dpinContent(self):
        
        self.hlayoutpin = QHBoxLayout(self.framedPin)
        self.framelabelpin = QFrame(self.framedPin)
        self.hlayoutpin.addWidget(self.framelabelpin)
        self.hlayoutlabelpin = QHBoxLayout(self.framelabelpin)
    
        self.labeldpin = QLabel(self.framelabelpin)
        self.labeldpin.setText("Digital Pin")
        self.labeldpin.setFont(QFont("Arial", 15))
        self.labeldpin.setStyleSheet("color: #02659D")
        self.labeldpin.setAlignment(Qt.AlignCenter)
        self.hlayoutlabelpin.addWidget(self.labeldpin)

        self.framespin = QFrame(self.framedPin)
        self.hlayoutpin.addWidget(self.framespin)
        self.hlayoutspin = QHBoxLayout(self.framespin)

        self.spin = QSpinBox(self.framespin)
        self.spin.setMinimum(0)
        self.spin.setMaximum(13)
        self.spin.setValue(13)
        self.spin.setFont(QFont("Arial", 15))
        self.spin.setStyleSheet("color: #02659D")
        self.spin.setAlignment(Qt.AlignCenter)
        self.hlayoutspin.addWidget(self.spin)
        

    def apinContent(self):

        self.hlayoutapin = QHBoxLayout(self.frameaPin)
        self.framelabelapin = QFrame(self.frameaPin)
        self.hlayoutapin.addWidget(self.framelabelapin)
        self.hlayoutlabelapin = QHBoxLayout(self.framelabelapin)

        self.labelapin = QLabel(self.framelabelapin)
        self.labelapin.setText("Analog Pin")
        self.labelapin.setFont(QFont("Arial", 15))
        self.labelapin.setStyleSheet("color: #02659D")
        self.labelapin.setAlignment(Qt.AlignCenter)
        self.hlayoutlabelapin.addWidget(self.labelapin)

        self.combopin = QFrame(self.frameaPin)
        self.hlayoutapin.addWidget(self.combopin)
        self.hlayoutcombopin = QHBoxLayout(self.combopin)
        self.analoglist = ['A0', 'A1', 'A2', 'A3', 'A4', 'A5']
        self.combo = QComboBox(self.combopin)
        self.combo.addItems(self.analoglist)
        self.combo.setFont(QFont("Arial", 15))
        self.combo.setStyleSheet("color: #02659D")
        #self.combo.setAlignment(Qt.AlignCenter)
        self.hlayoutcombopin.addWidget(self.combo)

     

    def setButtonContent(self):
        self.hlayoutbut = QHBoxLayout(self.setButtonFrame)
        self.buttonTest = QFrame(self.setButtonFrame)
        self.hlayoutbut.addWidget(self.buttonTest)
        self.buttonteslayout = QHBoxLayout(self.buttonTest)

        self.buttonTest = QPushButton(self.buttonTest)
        self.buttonTest.setText("Test")
        self.buttonTest.setFont(QFont("Arial", 15))
        self.buttonTest.setStyleSheet("color: #02659D")
        #self.buttonTest.setAlignment(Qt.AlignCenter)
        self.buttonteslayout.addWidget(self.buttonTest)

        self.buttonSetup = QFrame(self.setButtonFrame)
        self.hlayoutbut.addWidget(self.buttonSetup)
        self.buttonsetuplayout = QHBoxLayout(self.buttonSetup)

        self.buttonSetup = QPushButton(self.buttonSetup)
        self.buttonSetup.setText("Setup")
        self.buttonSetup.setFont(QFont("Arial", 15))
        self.buttonSetup.setStyleSheet("color: #02659D")
        #self.buttonSetup.setAlignment(Qt.AlignCenter)
        self.buttonsetuplayout.addWidget(self.buttonSetup)

        

