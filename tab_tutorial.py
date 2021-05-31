from PyQt5.QtWidgets import QApplication, QDialog, QTabWidget, QDialogButtonBox, QWidget, QVBoxLayout
import sys

class TabWidget(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tab Widget Application")
        #self.setWindowIcon(QIcon("myicon.png"))

        tabwidget = QTabWidget()
        tabwidget.addTab(FirstTab(), "First Tab")
        tabwidget.addTab(SecondTab(), "Second Tab")
        tabwidget.addTab(ThirdTab(), "Third Tab")

        buttonbox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        buttonbox.accepted.connect(self.accept)
        buttonbox.rejected.connect(self.reject)

        vbox = QVBoxLayout()
        vbox.addWidget(tabwidget)
        vbox.addWidget(buttonbox)



class FirstTab(QWidget):
    def __init__(self):
        super().__init__()



class SecondTab(QWidget):
    def __init__(self):
        super().__init__()



class ThirdTab(QWidget):
    def __init__(self):
        super().__init__()



def window():
    app = QApplication(sys.argv)
    screen = TabWidget()
    screen.show()
    sys.exit(app.exec_())

window()
