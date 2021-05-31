#!/usr/bin/env python3
from PyQt5.QtCore import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import sys

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setGeometry(200, 200, 300, 300)
        layout = QGridLayout()
        self.setLayout(layout)

        tabwidget = QTabWidget()
        tabwidget.addTab(FirstTab(), "Tab 1")
        tabwidget.addTab(SecondTab(), "Tab 2")
        tabwidget.addTab(ThirdTab(), "Tab 3")
        tabwidget.addTab(FourthTab(), "Tab 4")
        layout.addWidget(tabwidget, 0, 0)

class FirstTab(QWidget):
    def __init__(self):
        super().__init__()

        self.name = QLabel("Name: ")
        self.nameEdit = QLineEdit()
        self.nameEdit.editingFinished.connect(self.updatevariable)

        layout = QGridLayout()
        layout.addWidget(self.name, 1, 1)
        layout.addWidget(self.nameEdit, 2, 1)
        self.setLayout(layout)
    
    def updatevariable(self):
        global soil
        soil = self.nameEdit.text()
        print(soil)

class SecondTab(QWidget):
    def __init__(self):
        super().__init__()

        name = QLabel("Name: ")
        nameEdit = QLineEdit()

        layout = QGridLayout()
        layout.addWidget(name, 1, 1)
        layout.addWidget(nameEdit, 2, 1)
        self.setLayout(layout)


class ThirdTab(QWidget):
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
            f.writelines(repr(soil))


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

#class variables:
#    def __init__(self, soil):
#        self.soil = soil

#elements = variables()
#elements.soil = 0

soil = 0

def window():
    app = QApplication(sys.argv)
    screen = Window()
    screen.show()
    sys.exit(app.exec_())

window()
