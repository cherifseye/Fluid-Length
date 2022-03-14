from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QFrame, QApplication,
                            QHBoxLayout, QLabel, QPushButton, QLineEdit,
                            QMessageBox, QSpinBox, QComboBox, QAction, QMenuBar)
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtCore import Qt, QRect, QSize, QTimer, QThread, pyqtSignal
import pyqtgraph as pg
import config
import sys
from time import sleep
import math
import random
from pyfirmata import Arduino, util



class Thread(QThread):
    _signal = pyqtSignal(int)

    def __init__(self):
        super(Thread, self).__init__()
        self.exiting = False

    def __del__(self):
        self.exiting = True
        self.wait()

    def run(self):
        i = 1
        while i < 100:
            if self.exiting:
                break
            self._signal.emit(i)
            sleep(0.1)
            i += 1

class FluidLenght(QMainWindow):

    def __init__(self):
        super().__init__()
        self.unitUI()
        self.cwidget()
        self.general()
        self.content()
        self.contentconfig()
        self.portContent()
        self.dpinContent()
        self.apinContent()
        self.setButtonContent()
        self.framenumUI()
        self.liquidframecontent()
        self.measurecontent()
        self.frameplotting()
        self.graphics()
        self.configgraphics()
        self.intensityval = []
        self.pressureval = []
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

    def unitUI(self):
        self.resize(850, 800)
        self.setWindowTitle('Fluid Lenght')
    
    def cwidget(self):
        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)
        self.vlayout = QVBoxLayout(self.centralWidget)

    def general(self):
        self.configurationframe = QFrame(self.centralWidget)
        self.configurationframe.setFrameShape(QFrame.StyledPanel)
        self.configurationframe.setFrameShadow(QFrame.Raised)
        self.configurationframe.setMaximumHeight(100)
        self.configlayout = QHBoxLayout(self.configurationframe)
        self.vlayout.addWidget(self.configurationframe)

        self.body = QFrame(self.centralWidget)
        self.body.setFrameShape(QFrame.StyledPanel)
        self.body.setFrameShadow(QFrame.Raised)
        self.bodylayout = QHBoxLayout(self.body)
    
        self.vlayout.addWidget(self.configurationframe)
        self.vlayout.addWidget(self.body)

    def content(self):
        self.framenum = QFrame(self.body)
        self.bodylayout.addWidget(self.framenum)
        self.framenum.setMaximumSize(QSize(220, 16777215))

        self.frameplot = QFrame(self.centralWidget)
        self.bodylayout.addWidget(self.frameplot)


    def framenumUI(self):
        self.vlayoutnum = QVBoxLayout(self.framenum)
        self.liquipropframe = QFrame(self.framenum)
        self.liquipropframe.setFrameShape(QFrame.StyledPanel)
        self.liquipropframe.setFrameShadow(QFrame.Raised)
        self.vlayoutnum.addWidget(self.liquipropframe)
        self.liquipropframe.setMinimumSize(QSize(16777215, 150))
        self.liquipropframe.setMaximumSize(QSize(16777215, 200))

        self.measureframe = QFrame(self.framenum)
        self.measureframe.setFrameShape(QFrame.StyledPanel)
        self.measureframe.setFrameShadow(QFrame.Raised)
        self.vlayoutnum.addWidget(self.measureframe)


    def liquidframecontent(self):
        self.vlayoutliquid = QVBoxLayout(self.liquipropframe)

        self.framelabel = QFrame(self.liquipropframe)
        self.framelabel.setFrameShape(QFrame.StyledPanel)
        self.framelabel.setFrameShadow(QFrame.Raised)
        self.vlayoutlabel = QVBoxLayout(self.framelabel)
        self.vlayoutliquid.addWidget(self.framelabel)
        self.framelabel.setStyleSheet('color: #800000')

        self.label = QLabel(self.framelabel)
        self.label.setText('Liquid Properties')
        self.label.setFont(QFont('Arial', 16))
        self.vlayoutlabel.addWidget(self.label, 0, Qt.AlignCenter)
        
        self.densityframe = QFrame(self.liquipropframe)
        self.densityframe.setFrameShape(QFrame.StyledPanel)
        self.densityframe.setFrameShadow(QFrame.Raised)
        self.hlayoutdensity = QHBoxLayout(self.densityframe)
        self.vlayoutliquid.addWidget(self.densityframe)

        self.densitylabel = QLabel(self.densityframe)
        self.densitylabel.setText('Density')
        self.densitylabel.setFont(QFont('Arial', 12))
        self.hlayoutdensity.addWidget(self.densitylabel, 0, Qt.AlignLeft)

        self.density = QLineEdit(self.densityframe)
        self.density.setPlaceholderText('Density')
        self.density.setFont(QFont('Arial', 12))
        self.hlayoutdensity.addWidget(self.density, 0, Qt.AlignRight)


        self.gravityframe = QFrame(self.liquipropframe)
        self.gravityframe.setFrameShape(QFrame.StyledPanel)
        self.gravityframe.setFrameShadow(QFrame.Raised)
        self.hlayoutgravity = QHBoxLayout(self.gravityframe)
        self.vlayoutliquid.addWidget(self.gravityframe)
        
        self.gravitylabel = QLabel(self.gravityframe)
        self.gravitylabel.setText('Gravity')
        self.gravitylabel.setFont(QFont('Arial', 12))
        self.hlayoutgravity.addWidget(self.gravitylabel, 0, Qt.AlignLeft)
        
        self.gravity = QLineEdit(self.gravityframe)
        self.gravity.setPlaceholderText('Gravity')
        self.gravity.setFont(QFont('Arial', 12))
        self.hlayoutgravity.addWidget(self.gravity, 0, Qt.AlignRight)

        self.specificweightframe = QFrame(self.liquipropframe)
        self.specificweightframe.setFrameShape(QFrame.StyledPanel)
        self.specificweightframe.setFrameShadow(QFrame.Raised)
        self.hlayoutspecificweight = QHBoxLayout(self.specificweightframe)
        self.vlayoutliquid.addWidget(self.specificweightframe)

        self.specificweightbutt = QPushButton(self.specificweightframe)
        self.specificweightbutt.setText('Specific Weight')
        self.specificweightbutt.setFont(QFont('Arial', 12))
        self.hlayoutspecificweight.addWidget(self.specificweightbutt, 0, Qt.AlignLeft)
        self.specificweightbutt.clicked.connect(self.gamma)

        self.specificweight = QLineEdit(self.specificweightframe)
        self.specificweight.setReadOnly(True)
        self.specificweight.setPlaceholderText('Specific Weight')
        self.specificweight.setFont(QFont('Arial', 12))
        self.hlayoutspecificweight.addWidget(self.specificweight, 0, Qt.AlignRight)


    def gamma(self):
        try:
            gravity = float(self.gravity.text())
            density = float(self.density.text())
            specificweight = round(density * gravity, 2)
            self.specificweight.setText(str(specificweight))

        except:
            text = 'Please enter a valid number'
            QMessageBox.warning(self, 'Error', text)

    def measurecontent(self):
        self.vlayoutmeasure = QVBoxLayout(self.measureframe)

        self.framelabel = QFrame(self.measureframe)
        self.framelabel.setFrameShape(QFrame.StyledPanel)
        self.framelabel.setFrameShadow(QFrame.Raised)
        self.vlayoutlabel = QVBoxLayout(self.framelabel)
        self.vlayoutmeasure.addWidget(self.framelabel)
        self.framelabel.setStyleSheet('color: #FF0000')
        
        self.labelmesure = QLabel(self.framelabel)
        self.labelmesure.setText('Measure')
        self.labelmesure.setFont(QFont('Arial', 16))
        self.vlayoutlabel.addWidget(self.labelmesure, 0, Qt.AlignCenter)
        

        self.intenstyframe = QFrame(self.measureframe)
        self.intenstyframe.setFrameShape(QFrame.StyledPanel)
        self.intenstyframe.setFrameShadow(QFrame.Raised)
        self.hlayoutintensty = QHBoxLayout(self.intenstyframe)
        self.vlayoutmeasure.addWidget(self.intenstyframe)

        self.intenstylabel = QPushButton(self.intenstyframe)
        self.intenstylabel.setText('Intensity')
        self.intenstylabel.setFont(QFont('Arial', 12))
        self.intenstylabel.clicked.connect(self.get_intensity)
        self.hlayoutintensty.addWidget(self.intenstylabel, 0, Qt.AlignLeft)

        self.intensty = QLineEdit(self.intenstyframe)
        self.intensty.setPlaceholderText('Intensity')
        self.intensty.setReadOnly(True)
        self.intensty.setFont(QFont('Arial', 12))
        self.hlayoutintensty.addWidget(self.intensty, 0, Qt.AlignRight)


        self.atmpressureframe = QFrame(self.measureframe)
        self.atmpressureframe.setFrameShape(QFrame.StyledPanel)
        self.atmpressureframe.setFrameShadow(QFrame.Raised)
        self.hlayoutatmpressure = QHBoxLayout(self.atmpressureframe)
        self.vlayoutmeasure.addWidget(self.atmpressureframe)
        
        self.atmpressurelabel = QLabel(self.atmpressureframe)
        self.atmpressurelabel.setText('Pressure 0')
        self.atmpressurelabel.setFont(QFont('Arial', 12))
        self.hlayoutatmpressure.addWidget(self.atmpressurelabel, 0, Qt.AlignLeft)

        self.atmpressure = QLineEdit(self.atmpressureframe)
        self.atmpressure.setPlaceholderText('Pressure (atm)')
        self.atmpressure.setFont(QFont('Arial', 12))
        self.hlayoutatmpressure.addWidget(self.atmpressure, 0, Qt.AlignRight)


        self.jaugeframe = QFrame(self.measureframe)
        self.jaugeframe.setFrameShape(QFrame.StyledPanel)
        self.jaugeframe.setFrameShadow(QFrame.Raised)
        self.hlayoutjauge = QHBoxLayout(self.jaugeframe)
        self.vlayoutmeasure.addWidget(self.jaugeframe)

        self.jaugelabel = QPushButton(self.jaugeframe)
        self.jaugelabel.setText('Jauge')
        self.jaugelabel.setFont(QFont('Arial', 12))
        self.hlayoutjauge.addWidget(self.jaugelabel, 0, Qt.AlignLeft)

        self.jauge = QLineEdit(self.jaugeframe)
        self.jauge.setPlaceholderText('Jauge')
        self.jauge.setFont(QFont('Arial', 12))
        self.hlayoutjauge.addWidget(self.jauge, 0, Qt.AlignRight)


        self.abspressureframe = QFrame(self.measureframe)
        self.abspressureframe.setFrameShape(QFrame.StyledPanel)
        self.abspressureframe.setFrameShadow(QFrame.Raised)
        self.hlayoutabspressure = QHBoxLayout(self.abspressureframe)
        self.vlayoutmeasure.addWidget(self.abspressureframe)


        self.abspressurebutt = QPushButton(self.abspressureframe)
        self.abspressurebutt.setText('Pressure abs')
        self.abspressurebutt.setFont(QFont('Arial', 12))
        self.abspressurebutt.clicked.connect(self.abspressurecalc)
        self.hlayoutabspressure.addWidget(self.abspressurebutt, 0, Qt.AlignLeft)

        self.abspressure = QLineEdit(self.abspressureframe)
        self.abspressure.setPlaceholderText('Pressure (atm)')
        self.abspressure.setFont(QFont('Arial', 12))
        self.hlayoutabspressure.addWidget(self.abspressure, 0, Qt.AlignRight)
        self.abspressure.setReadOnly(True)
    

        self.heightframe = QFrame(self.measureframe)
        self.heightframe.setFrameShape(QFrame.StyledPanel)
        self.heightframe.setFrameShadow(QFrame.Raised)
        self.hlayoutheight = QHBoxLayout(self.heightframe)
        self.vlayoutmeasure.addWidget(self.heightframe)

        self.heightbutt = QPushButton(self.heightframe)
        self.heightbutt.setText('Height')
        self.heightbutt.setFont(QFont('Arial', 12))
        self.hlayoutheight.addWidget(self.heightbutt, 0, Qt.AlignLeft)
        self.heightbutt.clicked.connect(self.get_height)

        self.height = QLineEdit(self.heightframe)
        self.height.setPlaceholderText('Height')
        self.height.setFont(QFont('Arial', 12))
        self.hlayoutheight.addWidget(self.height, 0, Qt.AlignRight)

        self.realheight = QFrame(self.measureframe)
        self.realheight.setFrameShape(QFrame.StyledPanel)
        self.realheight.setFrameShadow(QFrame.Raised)
        self.hlayoutrealheight = QHBoxLayout(self.realheight)
        self.vlayoutmeasure.addWidget(self.realheight)

        self.realheightlabel = QLabel(self.realheight)
        self.realheightlabel.setText('Real height')
        self.realheightlabel.setFont(QFont('Arial', 12))
        self.hlayoutrealheight.addWidget(self.realheightlabel, 0, Qt.AlignLeft)

        self.realheightvalue = QLineEdit(self.realheight)
        self.realheightvalue.setPlaceholderText('Real height')
        self.realheightvalue.setFont(QFont('Arial', 12))
        self.hlayoutrealheight.addWidget(self.realheightvalue, 0, Qt.AlignRight)

        self.precisionframe = QFrame(self.measureframe)
        self.precisionframe.setFrameShape(QFrame.StyledPanel)
        self.precisionframe.setFrameShadow(QFrame.Raised)
        self.hlayoutprecision = QHBoxLayout(self.precisionframe)
        self.vlayoutmeasure.addWidget(self.precisionframe)

        self.precisionbutt = QPushButton(self.precisionframe)
        self.precisionbutt.setText('Precision')
        self.precisionbutt.setFont(QFont('Arial', 12))
        self.precisionbutt.clicked.connect(self.precisioncompute)
        self.hlayoutprecision.addWidget(self.precisionbutt, 0, Qt.AlignLeft)

        self.precision = QLineEdit(self.precisionframe)
        self.precision.setPlaceholderText('Precision')
        self.precision.setFont(QFont('Arial', 12))
        self.hlayoutprecision.addWidget(self.precision, 0, Qt.AlignRight)

    def get_intensity(self):
        try:
            self.intensty.clear()
            potval = self.potpin.read()
            jaugeval = math.exp(int(potval)) + random.uniform(-0.1, 0.1)
            self.intensty.setText(str(potval))
            self.jauge.setText(str(round(jaugeval, 2)))

        except:
            text = "Please check if the device is connected"
            QMessageBox.warning(self, "Error", text)

            
    def abspressurecalc(self):
        try:
            press0 = float(self.atmpressure.text())
            press1 = float(self.jauge.text())
            abspress = press0 + press1
            self.abspressure.setText(str(abspress))

        except:
            text = 'Please enter a number'
            QMessageBox.warning(self, 'Error', text)

    def get_height(self):
        try:
            self.height.clear()
            pressure = float(self.abspressure.text())
            speciifc_w  = float(self.specificweight.text())
            self.height.setText(str(round(pressure / speciifc_w, 2)))

        except:
            text = "Please check if the device is connected"
            QMessageBox.warning(self, "Error", text)

    def precisioncompute(self):
        try:
            real = float(self.realheightvalue.text())
            mesheight = float(self.height.text())
            precision = round((real - mesheight) / real * 100, 2)
            self.precision.setText(str(precision) + '%')

        except:
            text = 'Please enter a number'
            QMessageBox.warning(self, 'Error', text)

    
    def frameplotting(self):
        self.vlayoutplot = QVBoxLayout(self.frameplot)
        self.framegraph = QFrame(self.frameplot)
        self.vlayoutplot.addWidget(self.framegraph)
        self.framegraphvlayout = QVBoxLayout(self.framegraph)

        self.configplotframe = QFrame(self.frameplot) 
        self.configplotframe.setMaximumHeight(200)
        self.configplotvlayout = QVBoxLayout(self.configplotframe)
        self.vlayoutplot.addWidget(self.configplotframe)


    def graphics(self):
        self.graph = pg.PlotWidget(self.framegraph)
        self.graph.setBackground('w')
        self.graph.setLabel('bottom', 'Time', units='s')
        self.graph.setLabel('left', 'Intensity', units='A')
        self.framegraphvlayout.addWidget(self.graph)
        self.graph.setGeometry(QRect(0, 0, 400, 400))
        self.graph.showGrid(x=True, y=True)


    def configgraphics(self):
        self.framebutton = QFrame(self.configplotframe)
        self.framebutton.setFrameShape(QFrame.StyledPanel)
        self.framebutton.setFrameShadow(QFrame.Raised)
        self.framebuttonhlayout = QHBoxLayout(self.framebutton)
        self.configplotvlayout.addWidget(self.framebutton)

        self.buttonplot = QPushButton(self.framebutton)
        self.buttonplot.setText('Plot')
        self.buttonplot.setFont(QFont('Arial', 12))
        self.buttonplot.clicked.connect(self.sendthread)
        self.framebuttonhlayout.addWidget(self.buttonplot)
        #self.buttonplot.clicked.connect(self.plottingaction)

        self.buttonclear = QPushButton(self.framebutton)
        self.buttonclear.setText('Clear')
        self.buttonclear.setFont(QFont('Arial', 12))
        self.buttonclear.clicked.connect(self.clear)
        self.framebuttonhlayout.addWidget(self.buttonclear)
     


    def contentconfig (self):
        #In this frame we will put the port content
        self.framePort = QFrame(self.configurationframe)
        self.framePort.setFrameShape(QFrame.StyledPanel)
        self.framePort.setFrameShadow(QFrame.Raised)
        self.configlayout.addWidget(self.framePort)
        
        #In this frame we will put the digital pin content
        self.framedPin = QFrame(self.configurationframe)
        self.framedPin.setFrameShape(QFrame.StyledPanel)
        self.framedPin.setFrameShadow(QFrame.Raised)
        self.configlayout.addWidget(self.framedPin)
        self.framedPin.setObjectName("framePin")
        self.configlayout.addWidget(self.framedPin)
        
        #In this frame we will put the analog pin content
        self.frameaPin = QFrame(self.configurationframe)
        self.frameaPin.setFrameShape(QFrame.StyledPanel)
        self.frameaPin.setFrameShadow(QFrame.Raised)
        self.configlayout.addWidget(self.frameaPin)
         
        #In this frame we will put the set button(test and setup) content
        self.setButtonFrame = QFrame(self.configurationframe)
        self.setButtonFrame.setFrameShape(QFrame.StyledPanel)
        self.setButtonFrame.setFrameShadow(QFrame.Raised)
        self.setButtonFrame.setMaximumWidth(190)
        self.configlayout.addWidget(self.setButtonFrame)

    def portContent(self): #This function will create the port content
        self.hlayoutport = QHBoxLayout(self.framePort)
        self.framelabelport = QFrame(self.framePort)
        self.hlayoutport.addWidget(self.framelabelport)
        self.hlayoutlabel = QVBoxLayout(self.framelabelport)

        self.labelport = QLabel(self.framelabelport) 
        self.labelport.setText("Port Name")
        self.labelport.setFont(QFont("Arial", 15))
        self.labelport.setStyleSheet("color: #02659D")

        self.hlayoutlabel.addWidget(self.labelport, 0, Qt.AlignHCenter)

        self.framelineeditport = QFrame(self.framePort) #This frame will contain the line of the port name
        self.framelineeditport.setMaximumSize(QSize(148, 100))
        

        self.hlayoutport.addWidget(self.framelineeditport)
        self.hlayoutlineedit = QHBoxLayout(self.framelineeditport)

        self.lineedit = QLineEdit(self.framelineeditport)
        self.lineedit.setText("/dev/cu.usbmodem141101")
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
    
    
    def setup(self):
        try:
            port = self.lineedit.text()
            self.board = Arduino(port)
            it = util.Iterator(self.board)
            it.start()
            pottext = self.combo.currentText()
            self.potpin = self.board.get_pin(self.apinchoice[pottext])

            
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

    def sendthread(self):
        self.thread = Thread()
        self.thread._signal.connect(self.signal_accept)
        self.thread.start()
        self.buttonplot.setEnabled(False)

    def signal_accept(self):
        try:
            potval = self.potpin.read()
            if potval is not None:
                self.intensityval.append(potval)
                self.graph.plot(self.intensityval)

        except:
            text ="Please check your setup or make sure that you chose the right port and serial"
            QMessageBox().about(self, "Error", text)
            
    
    def clear(self):
        self.graph.clear()
        self.intensityval = []
        self.buttonplot.setEnabled(True)