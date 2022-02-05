import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import tkinter
from tkinter.filedialog import askopenfilename

from elements import *

import csv
import ast


def read_csv_file(filename):
    with open(filename, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)

    for i in range(len(data)):
        data[i][-1] = ast.literal_eval(data[i][-1])
        data[i][1], data[i][2] = int(data[i][1]), int(data[i][2])

    return data

def write_config_file(filePath):
    f = open("configFile.txt", "w")
    f.write(filePath)
    f.close()

def read_config_file():
    f = open('configFile.txt', "r")
    # print(f.read())
    return f.read()

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
        
        self.fileName = read_config_file()

        self.generalLayout = QVBoxLayout()
        self._centralWidget = QWidget(self)
        self.setCentralWidget(self._centralWidget)

        self._centralWidget.setLayout(self.generalLayout)

        self._createToolBars()

        self.elementFactory = {
            'VS': VS,
            'Ground': Ground,
            'T2C': Transformer2Coil,
            'T3C': Transformer3Coil,
            'VT': VT,
            'CT': CT,
            'transferLine': TransferLine,
            'Bus': Bus
        }
        print(self.fileName)
        self._createDisplay(self.fileName)

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
     
    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawLines(qp)
        qp.end()

    def drawLines(self, qp):
        
        pen = QPen(Qt.blue, 3, Qt.SolidLine)
        qp.setPen(pen)

        for element in self.elementsList:
            elementConnectionList = element.getConnections()
            for connection in elementConnectionList:
                if(isinstance(connection, tuple)):
                    otherElement1 = self.elementsList[connection[0]]
                    otherElement2 = self.elementsList[connection[1]]
                    avgCenterX = (otherElement1.center[0] + otherElement2.center[0])/2
                    avgCenterY = (otherElement2.center[1] + otherElement2.center[1])/2
                    qp.drawLine(element.center[0], element.center[1], avgCenterX, avgCenterY)
                else:
                    otherElement = self.elementsList[connection]
                    qp.drawLine(element.center[0], element.center[1],
                     otherElement.center[0], otherElement.center[1])

    def _createDisplay(self, fileName):
        elementData = read_csv_file(fileName)
        print(self)
        self.elementsList = []

        for element in elementData:
            _element = self.elementFactory[element[0]](self, element[1], element[2], element[3])
            self.elementsList.append(_element)





    def toggleOptionWindow(self, checked):
        if(self.options.isVisible()):
            self.options.hide()
        else:
            self.options.show()

    def getFileDialogWindow(self, checked):
        root = tkinter.Tk()
        root.withdraw()
        self.fileName = askopenfilename(initialdir="./", title='Choose Generator.csv')
        write_config_file(self.fileName)
        # self._createDisplay(self.fileName)


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

flag_draw = False
if __name__ == '__main__':
        
    app = QApplication(sys.argv)
    app.setStyleSheet(styleSheet)

    window = SimWindow()
    window.resize(1024, 1024)

    # helloMsg = QLabel('<h1>Hello from outside</h1>', parent=window)
    # helloMsg.move(60, 15)

    window.show()

    sys.exit(app.exec_())