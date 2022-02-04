import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Diolog:
    def __init__(self):
        pass
    
    def connect(self):
        pass

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
        self.toolbars = QHBoxLayout()
        self.toolbars.addWidget(PushButton('Model', 100, 50).getButton())
        self.toolbars.addWidget(PushButton('Options', 100).getButton())
        self.toolbars.addWidget(PushButton('Simulate', 100).getIcon('./images/play_icon.png'))

        self.generalLayout.addLayout(self.toolbars)
        self.generalLayout.setAlignment(self.toolbars, Qt.AlignTop)
    
    def _createDisplay(self):
        pass

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