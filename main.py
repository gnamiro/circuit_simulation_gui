import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import tkinter
# import tkFileDialog

import elements



class Dialog(QDialog):
    def __init__(self):
        super().__init__()
        pass

class OptionsDialog(Dialog):
    def __init__(self, parent=None):
        super().__init__()
        self.setWindowTitle('Options')

        dlgLayout = QVBoxLayout()

        formLayout = QFormLayout()
        formLayout.addRow('Main Time Step(dt):', self.createLineCombox())
        formLayout.addRow('Simulation Time:', self.createLineCombox())
        dlgLayout.addLayout(formLayout)

        btns = QDialogButtonBox()
        btns.setStandardButtons(
            QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        btns.clicked.connect(self.close)
        dlgLayout.addWidget(btns)

        self.setLayout(dlgLayout)

    
    def createTimeBox(self):
        comboBox = QComboBox()
            # self.comboBox.setGeometry(QRect(40, 40, 491, 31))
        comboBox.setObjectName(("Time Dimensions"))
        comboBox.addItem("ms")
        comboBox.addItem("s")
        comboBox.addItem("m")
        comboBox.addItem("h")

        return comboBox

    def createLineCombox(self):
        lineCombo = QHBoxLayout()
        lineCombo.addWidget(QLineEdit())
        lineCombo.addWidget(self.createTimeBox())

        return lineCombo


class PushButton:
    def __init__(self, message, max_width, min_width=None):
        self.button = QPushButton(message)
        self.button.setMaximumWidth(max_width)
        self.button.setMinimumWidth(len(message)* 10 +7)       
        
    def getButton(self):
        return self.button

    def getIcon(self, path):
        self.button.setText('')
        self.button.setIcon(QIcon(path))
        self.button.setIconSize(QSize(20, 17))
        self.button.setFixedWidth(23)

        return self.button


class SimWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()

        self.setWindowTitle('Simulator')

        self.generalLayout = QVBoxLayout()
        
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)

        self._centralWidget.setLayout(self.generalLayout)

        self._createToolBars()
        self._createDisplay()

    def _createToolBars(self):
        self.optionButton = PushButton('Options', 100).getButton()
        self.modelButton = PushButton('Model', 100, 50).getButton()

        self.toolbars = QHBoxLayout()
        self.toolbars.addWidget(self.modelButton)
        self.toolbars.addWidget(self.optionButton)
        self.toolbars.addWidget(PushButton('Simulate', 100).getIcon('./images/play_icon.png'))

        self.options = OptionsDialog()
        self.optionButton.clicked.connect(self.toggleOptionWindow)
        self.modelButton.clicked.connect(self.getFileDialogWindow)

        self.generalLayout.addLayout(self.toolbars)
        self.generalLayout.setAlignment(self.toolbars, Qt.AlignTop)
     
    def _createDisplay(self):
        pass


    def toggleOptionWindow(self, checked):
        if(self.options.isVisible()):
            self.options.hide()
        else:
            self.options.show()

    def getFileDialogWindow(self, checked):
        root = tkinter.Tk()
        root.withdraw()
        self.filename = tkinter.filedialog.askopenfilename(initialdir="/", title='Choose Generator.csv')


styleSheet = """
    SimWindow {
        background-image: url(./images/background_black.jpg);
        background_repeat: repeat;
        background-position: top; 
    },
    SimWindow toolbars {
        width: 100px
    }
"""

def findScreenWidth():
    screen = app.primaryScreen()
    size = screen.size()
    return size.width(), size.height()


if __name__ == '__main__':
        
    app = QApplication(sys.argv)
    app.setStyleSheet(styleSheet)


    window = SimWindow()
    window.resize(640, 640)
    # helloMsg = QLabel('<h1>Hello from outside</h1>', parent=window)
    # helloMsg.move(60, 15)

    window.show()

    sys.exit(app.exec_())