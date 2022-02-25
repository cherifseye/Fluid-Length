from email import message
from PyQt5.QtWidgets import (QWidget, QMainWindow, QVBoxLayout, QFrame, QLabel, QHBoxLayout, 
                            QLineEdit, QSpinBox, QComboBox, QPushButton, QMessageBox, QAction, QMenuBar)
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtCore import Qt, QRect, QSize
from pyfirmata import Arduino, util
import UI

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
        self.createMenuBAr()
        '''
        1 Create a dictionary with the port name and the digital pin
        '''
        self.pinchoice = {
            '13': 'd:13:o',
            '12': 'd:12:o',
            '11': 'd:11:o',
            '10': 'd:10:o',
            '9': 'd:9:o',
            '8': 'd:8:o',
            '7': 'd:7:o',
            '6': 'd:6:o',
            '5': 'd:5:o',
            '4': 'd:4:o',
            '3': 'd:3:o',
            '2': 'd:2:o',
            '1': 'd:1:o'
        }
        
        '''
        2 create a dictionnary for analog pin choice
        '''
        self.apinchoice = {
            'A0': 'a:0:i',
            'A1': 'a:1:i',
            'A2': 'a:2:i',
            'A3': 'a:3:i',
            'A4': 'a:4:i',
            'A5': 'a:5:i'
        }

    def initUI(self):
        #The size and the title of the window
        self.resize(300, 300)
        self.setWindowTitle('CONFIGURATION')
        self.setMinimumSize(350, 350)

    
    def createMenuBAr(self):
        exit_act = QAction('Exit', self)
        exit_act.setShortcut('Ctrl+Q')
        exit_act.triggered.connect(self.close)

        self.helpcontent = QAction('Help', self)
        self.helpcontent.setShortcut('Ctrl+L')
        self.helpcontent.triggered.connect(self.help)

        menuBar = QMenuBar(self)
        menuBar.setNativeMenuBar(False)
        helpmenu = menuBar.addMenu('&Help')
        helpmenu.addAction(self.helpcontent)

        exitmenu = menuBar.addMenu('&Exit')
        exitmenu.addAction(exit_act)

    def help(self):
        message = """This page allow you to set your configuration for the Arduino
        These are the step to follow for seting your configuration
        1. Choose your port name
        2.Press on the SETUP button to make sure that you have the right port
        3.In thsi step we will test your setup by using the led that we provide you
        -Choose the digital pin you want to use
        -Press on the TEST button to test, if everything is ok, you will see the led turning on
        4 After the test work is done, press on the NEXT button to go to the next page and take your mesure of pressure
        """

        self.message = QMessageBox().information(self, "Help", message, QMessageBox.Ok)



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
        self.framelineeditport.setMaximumSize(QSize(148, 100))
        

        self.hlayoutport.addWidget(self.framelineeditport)
        self.hlayoutlineedit = QHBoxLayout(self.framelineeditport)

        

        self.lineedit = QLineEdit(self.framelineeditport)
        self.lineedit.setText("COM3")
        self.lineedit.setFont(QFont("Arial", 15))
        self.lineedit.setStyleSheet("color: #02659D")
        self.hlayoutlineedit.addWidget(self.lineedit)
        
        
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
        self.buttonTest.clicked.connect(self.testing)


        self.buttonSetup = QFrame(self.setButtonFrame)
        self.hlayoutbut.addWidget(self.buttonSetup)
        self.buttonsetuplayout = QHBoxLayout(self.buttonSetup)

        self.buttonSetup = QPushButton(self.buttonSetup)
        self.buttonSetup.setText("Setup")
        self.buttonSetup.setFont(QFont("Arial", 15))
        self.buttonSetup.setStyleSheet("color: #02659D")
        #self.buttonSetup.setAlignment(Qt.AlignCenter)
        self.buttonsetuplayout.addWidget(self.buttonSetup)
        self.buttonSetup.clicked.connect(self.setup)

        self.buttonnextr = QFrame(self.setButtonFrame)
        self.hlayoutbut.addWidget(self.buttonnextr)
        self.buttonnextlayout = QHBoxLayout(self.buttonnextr)

        self.buttonnext = QPushButton(self.buttonnextr)
        self.buttonnext.setText("Next")
        self.buttonnext.setFont(QFont("Arial", 15))
        self.buttonnext.setStyleSheet("color: #02659D")
        #self.buttonnext.setAlignment(Qt.AlignCenter)
        self.buttonnextlayout.addWidget(self.buttonnext)
        self.buttonnext.clicked.connect(self.next)


    def setup(self):
        try:
            port = self.lineedit.text()
            self.board = Arduino(port)
            it = util.Iterator(self.board)
            it.start()

        except:
            text ="Please check your setup or make sure that you chose the right port and serial"
            QMessageBox().about(self, "Error", text)

    
    def testing(self):
        try:
            pintext = self.spin.text()
            ledpin = self.board.get_pin(self.pinchoice[pintext])
            ledpin.write(1)

        except:
            text ="Please check your setup or make sure that you chose the right port and serial"
            QMessageBox().about(self, "Error", text)

    def next(self, checked):
        try:
            self.close()
            self.uiwindow = UI.FluidLenght()
            self.uiwindow.show()
        except:
            text ="Can't open the next window"
            QMessageBox().about(self, "Error", text)





