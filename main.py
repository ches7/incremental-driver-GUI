from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import sys

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("pyqt test 1")
        self.initUI()
    


    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("my first label")
        self.label.move(50,50)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("click me")
        self.b1.clicked.connect(self.clicked)

        #layout = QGridLayout()
        #self.setLayout(layout)

        #label1 = QLabel("Example content contained in a tab.")
        #label2 = QLabel("More example text in the second tab.")

       # tabwidget = QTabWidget()
        #tabwidget.addTab(self.label, "Tab 1")
       # tabwidget.addTab(label2, "Tab 2")
        #self.layout.addWidget(tabwidget, 0, 0)
    
    def clicked(self):
        self.label.setText("you pressed the button")
        self.update()

    def update(self):
        self.label.adjustSize()



def window():
    app = QApplication(sys.argv)
    screen = Window()
    screen.show()
    sys.exit(app.exec_())

window()
