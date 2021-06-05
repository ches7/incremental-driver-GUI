#!/usr/bin/env python3
from PyQt5.QtCore import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import sys

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setGeometry(500, 500, 700, 700)
        layout = QGridLayout()
        self.setLayout(layout)

        tabwidget = QTabWidget()
        tabwidget.addTab(FirstTab(), "General Information")
        tabwidget.addTab(SecondTab(), "Material Constants")
        tabwidget.addTab(ThirdTab(), "Water Retention Model")
        tabwidget.addTab(FourthTab(), "Initial Conditions")
        tabwidget.addTab(FifthTab(), "Export")
        layout.addWidget(tabwidget, 0, 0)

    #def update(self):
     #   self.label.adjustSize()

class FirstTab(QWidget):
    def __init__(self):
        super().__init__()

        name = QLabel("Name of the Analysis/User")

        layout = QGridLayout()
        layout.addWidget(name, 0, 0)
        self.setLayout(layout)

class SecondTab(QWidget):
    def __init__(self):
        super().__init__()

#example of how to set up labels and LineEdit boxes
        self.nameExample = QLabel("Name: ")
        self.nameEditExample = QLineEdit()
        self.nameEditExample.editingFinished.connect(self.updatevariable)


#IMODE1 Label and LineEdit boxes
        self.nameIMODE1 = QLabel("IMODE(1): ")
        self.nameEditIMODE1 = QLineEdit()
        self.nameEditIMODE1.editingFinished.connect(self.updatevariable)

#IMODE2 Label and LineEdit boxes
        self.nameIMODE2 = QLabel("IMODE(2): ")
        self.nameEditIMODE2 = QLineEdit()
        self.nameEditIMODE2.editingFinished.connect(self.updatevariable)

#IMODE3 Label and LineEdit boxes
        self.nameIMODE3 = QLabel("IMODE(3): ")
        self.nameEditIMODE3 = QLineEdit()
        self.nameEditIMODE3.editingFinished.connect(self.updatevariable)

#IMODE4 Label and LineEdit boxes
        self.nameIMODE4 = QLabel("IMODE(4): ")
        self.nameEditIMODE4 = QLineEdit()
        self.nameEditIMODE4.editingFinished.connect(self.updatevariable)

#DDE Label and LineEdit boxes
        self.nameDDE = QLabel("DDE: ")
        self.nameEditDDE = QLineEdit()
        self.nameEditDDE.editingFinished.connect(self.updatevariable)

#RATIO Label and LineEdit boxes
        self.nameRATIO = QLabel("RATIO: ")
        self.nameEditRATIO = QLineEdit()
        self.nameEditRATIO.editingFinished.connect(self.updatevariable)

#IDIR Label and LineEdit boxes
        self.nameIDIR = QLabel("IDIR: ")
        self.nameEditIDIR = QLineEdit()
        self.nameEditIDIR.editingFinished.connect(self.updatevariable)

#IREV Label and LineEdit boxes
        self.nameIREV = QLabel("IREV: ")
        self.nameEditIREV = QLineEdit()
        self.nameEditIREV.editingFinished.connect(self.updatevariable)

#PEAK Label and LineEdit boxes
        self.namePEAK = QLabel("PEAK: ")
        self.nameEditPEAK = QLineEdit()
        self.nameEditPEAK.editingFinished.connect(self.updatevariable)

#NPRINT Label and LineEdit boxes
        self.nameNPRINT = QLabel("NPRINT: ")
        self.nameEditNPRINT = QLineEdit()
        self.nameEditNPRINT.editingFinished.connect(self.updatevariable)

#MAXLOOP Label and LineEdit boxes
        self.nameMAXLOOP = QLabel("MAXLOOP: ")
        self.nameEditMAXLOOP = QLineEdit()
        self.nameEditMAXLOOP.editingFinished.connect(self.updatevariable)

#NCYCL Label and LineEdit boxes
        self.nameNCYCL = QLabel("NCYCL: ")
        self.nameEditNCYCL = QLineEdit()
        self.nameEditNCYCL.editingFinished.connect(self.updatevariable)

#add objects to layout
        layout = QGridLayout()

        layout.addWidget(self.nameIMODE1, 1, 1)
        layout.addWidget(self.nameEditIMODE1, 1, 2)
        layout.addWidget(self.nameIMODE2, 2, 1)
        layout.addWidget(self.nameEditIMODE2, 2, 2)
        layout.addWidget(self.nameIMODE3, 3, 1)
        layout.addWidget(self.nameEditIMODE3, 3, 2)
        layout.addWidget(self.nameIMODE4, 4, 1)
        layout.addWidget(self.nameEditIMODE4, 4, 2)
        layout.addWidget(self.nameDDE, 5, 1)
        layout.addWidget(self.nameEditDDE, 5, 2)
        layout.addWidget(self.nameRATIO, 6, 1)
        layout.addWidget(self.nameEditRATIO, 6, 2)
        layout.addWidget(self.nameIDIR, 7, 1)
        layout.addWidget(self.nameEditIDIR, 7, 2)
        layout.addWidget(self.nameIREV, 8, 1)
        layout.addWidget(self.nameEditIREV, 8, 2)
        layout.addWidget(self.namePEAK, 9, 1)
        layout.addWidget(self.nameEditPEAK, 9, 2)
        layout.addWidget(self.nameNPRINT, 10, 1)
        layout.addWidget(self.nameEditNPRINT, 10, 2)
        layout.addWidget(self.nameMAXLOOP, 11, 1)
        layout.addWidget(self.nameEditMAXLOOP, 11, 2)
        layout.addWidget(self.nameNCYCL, 12, 1)
        layout.addWidget(self.nameEditNCYCL, 12, 2)

        self.setLayout(layout)

#set up updates to global variables    
    def updatevariable(self):
        global IMODE1, IMODE2, IMODE3, IMODE4, DDE, RATIO, IDIR, IREV, PEAK, NPRINT, MAXLOOP, NCYCL
        
        IMODE1 = self.nameEditIMODE1.text()
        IMODE2 = self.nameEditIMODE2.text()
        IMODE3 = self.nameEditIMODE3.text()
        IMODE4 = self.nameEditIMODE4.text()
        DDE = self.nameEditDDE.text()
        RATIO = self.nameEditRATIO.text()
        IDIR = self.nameEditIDIR.text()
        IREV = self.nameEditIREV.text()
        PEAK = self.nameEditPEAK.text()
        NPRINT = self.nameEditNPRINT.text()
        MAXLOOP = self.nameEditMAXLOOP.text()
        NCYCL = self.nameEditNCYCL.text()


class ThirdTab(QWidget):
    def __init__(self):
        super().__init__()

        name = QLabel("Name: ")
        nameEdit = QLineEdit()

        layout = QGridLayout()
        layout.addWidget(name, 1, 1)
        layout.addWidget(nameEdit, 2, 1)
        self.setLayout(layout)


class FourthTab(QWidget):
    def __init__(self):
        super().__init__()

        self.button1 = QtWidgets.QPushButton(self)
        self.button1.setText("click me")
        self.button1.clicked.connect(self.updatevariable2)

        layout = QGridLayout()
        layout.addWidget(self.button1, 1, 1)
        self.setLayout(layout)
    
    
    def updatevariable2(self):
        print("clicked")

class FifthTab(QWidget):
    def __init__(self):
        super().__init__()

        self.button3 = QtWidgets.QPushButton(self)
        self.button3.setText("export as txt")
        self.button3.clicked.connect(self.updatevariable2)

        layout = QGridLayout()
        layout.addWidget(self.button3, 1, 1)
        self.setLayout(layout)
    
    
    def updatevariable2(self):
        with open('export.txt', 'w') as f:
            f.writelines(repr(soil) + "\n")
            f.writelines(repr(IMODE1) + "\n")
            f.writelines(repr(IMODE2) + "\n")
            f.writelines(repr(IMODE3) + "\n")
            f.writelines(repr(IMODE4) + "\n")
            f.writelines(repr(DDE) + "\n")
            f.writelines(repr(RATIO) + "\n")
            f.writelines(repr(IDIR) + "\n")
            f.writelines(repr(IREV) + "\n")
            f.writelines(repr(PEAK) + "\n")
            f.writelines(repr(NPRINT) + "\n")
            f.writelines(repr(MAXLOOP) + "\n")
            f.writelines(repr(NCYCL) + "\n")

            f.writelines(repr(PAR1) + "\n")
            f.writelines(repr(PAR2) + "\n")
            f.writelines(repr(PAR3) + "\n")
            f.writelines(repr(PAR4) + "\n")
            f.writelines(repr(PAR5) + "\n")
            f.writelines(repr(PAR6) + "\n")
            f.writelines(repr(PAR7) + "\n")
            f.writelines(repr(PAR8) + "\n")
            f.writelines(repr(PAR9) + "\n")
            f.writelines(repr(PAR10) + "\n")
            f.writelines(repr(PAR11) + "\n")
            f.writelines(repr(PAR12) + "\n")
            f.writelines(repr(PAR13) + "\n")
            f.writelines(repr(PAR14) + "\n")
            f.writelines(repr(PAR15) + "\n")
            f.writelines(repr(PAR16) + "\n")
            f.writelines(repr(PAR17) + "\n")
            f.writelines(repr(PAR21) + "\n")
            f.writelines(repr(PAR22) + "\n")
            f.writelines(repr(PAR23) + "\n")
            f.writelines(repr(PAR24) + "\n")
            f.writelines(repr(PAR25) + "\n")
            f.writelines(repr(PAR26) + "\n")

            f.writelines(repr(SWCCPAR1) + "\n")
            f.writelines(repr(SWCCPAR2) + "\n")
            f.writelines(repr(SWCCPAR3) + "\n")
            f.writelines(repr(SWCCPAR4) + "\n")
            f.writelines(repr(SWCCPAR5) + "\n")

            f.writelines(repr(QH1) + "\n")
            f.writelines(repr(QH2) + "\n")
            f.writelines(repr(QH3) + "\n")
            f.writelines(repr(QH4) + "\n")
            f.writelines(repr(QH5) + "\n")
            f.writelines(repr(QH6) + "\n")

            f.writelines(repr(S) + "\n")
            f.writelines(repr(S1) + "\n")
            f.writelines(repr(S2) + "\n")
            f.writelines(repr(S3) + "\n")
            f.writelines(repr(SUC) + "\n")

            

#class variables:
#    def __init__(self, soil):
#        self.soil = soil

#elements = variables()
#elements.soil = 0

#VARIABLES
soil = 0
NT = 0

IMODE1 = 0
IMODE2 = 0 
IMODE3 = 0
IMODE4 = 0
DDE = 0 
RATIO = 0 
IDIR = 0
IREV = 0
PEAK = 0
NPRINT = 0
MAXLOOP = 0
NCYCL = 0

PAR1 = 0
PAR2 = 0
PAR3 = 0
PAR4 = 0
PAR5 = 0
PAR6 = 0
PAR7 = 0
PAR8 = 0
PAR9 = 0
PAR10 = 0
PAR11 = 0
PAR12 = 0
PAR13 = 0
PAR14 = 0
PAR15 = 0
PAR16 = 0
PAR17 = 0
PAR21 = 0
PAR22 = 0
PAR23 = 0
PAR24 = 0
PAR25 = 0
PAR26 = 0

SWCCPAR1 = 0
SWCCPAR2 = 0
SWCCPAR3 = 0
SWCCPAR4 = 0
SWCCPAR5 = 0

QH1 = 0
QH2 = 0
QH3 = 0
QH4 = 0
QH5 = 0
QH6 = 0

S = 0
S1 = 0
S2 = 0
S3 = 0
SUC = 0


def window():
    app = QApplication(sys.argv)
    screen = Window()
    screen.show()
    sys.exit(app.exec_())

window()
