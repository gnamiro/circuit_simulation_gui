import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QHBoxLayout, QWidget
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Node:
    def __init__(self):
        pass

    def __init__(self, parent, x, y, connectionList, NodeImPath):
        self.x = x
        self.y = y
        self.connectionList = connectionList

        self.im = QPixmap(NodeImPath)
        # self.im = self.im.scaled(100, 50, Qt.KeepAspectRatio)
        self.label = QLabel(parent=parent)
        self.label.setPixmap(self.im)
        # self.label.move(x, y)
        self.label.setGeometry(self.x, self.y, self.im.width(), self.im.height())
        self.label.setScaledContents(True)

    def draw(self):
        return self.label

    def connection(self):
        print('connections')
        pass


class Transfer_line(Node):
    def __init__(self, parent, x, y, connectionList, NodeImPath=None):
        Node.__init__(self, parent, x, y, connectionList, "./images/transfer_line.png")

class CT(Node):
    def __init__(self, parent, x, y, connectionList, NodeImPath=None):
        Node.__init__(self, parent, x, y, connectionList, "./images/CT.png")

class Bus(Node):
    def __init__(self, parent, x, y, connectionList, NodeImPath=None):
        Node.__init__(self, parent, x, y, connectionList, "./images/bus.png")

class Ground(Node):
    def __init__(self, parent, x, y, connectionList, NodeImPath=None):
        Node.__init__(self, parent, x, y, connectionList, "./images/ground.png")

class Transformer2Coil(Node):
    def __init__(self, parent, x, y, connectionList, NodeImPath=None):
        Node.__init__(self, parent, x, y, connectionList, "./images/transformer_2_coil.png")

class Transformer3Coil(Node):
    def __init__(self, parent, x, y, connectionList, NodeImPath=None):
        Node.__init__(self, parent, x, y, connectionList, "./images/transformer_3_coil.png")

class VSource(Node):
    def __init__(self, parent, x, y, connectionList, NodeImPath=None):
        Node.__init__(self, parent, x, y, connectionList, "./images/VSource.png")

class VT(Node):
    def __init__(self, parent, x, y, connectionList, NodeImPath=None):
        Node.__init__(self, parent, x, y, connectionList, "./images/VT.png")


if __name__ == '__main__':
        
    app = QApplication(sys.argv)


    window = QMainWindow()
    window.setWindowTitle('Elements Test Window')
    window.setGeometry(100, 100, 640, 640)
    window.move(60, 15)
    layout = QHBoxLayout()

    label = Transfer_line(window, 500, 700 , []).draw()
    label1 = CT(window, 100, 300 , []).draw()
    label2 = Bus(window, 150, 550 , []).draw()
    label3 = Ground(window, 100, 350 , []).draw()
    label4 = Transformer2Coil(window, 200, 500 , []).draw()
    label5 = Transformer3Coil(window, 350, 600 , []).draw()
    label6 = VSource(window, 450, 550 , []).draw()
    label7 = VT(window, 50, 200 , []).draw()
    layout.addWidget(label)
    layout.addWidget(label1)
    layout.addWidget(label2)
    layout.addWidget(label3)
    layout.addWidget(label4)
    layout.addWidget(label5)
    layout.addWidget(label6)
    # qp = QPainter()
    # qp.begin(window)
    # qp.setRenderHint(QPainter.Antialiasing)
    # path = QPainterPath()
    # path.moveTo(30, 30)
    # path.cubicTo(30, 30, 200, 350, 350, 30)

    # qp.drawPath(path)
    window.setLayout(layout)

    
    

    # helloMsg = QLabel('<h1>Hello from outside</h1>', parent=window)
    # helloMsg.move(60, 15)

    window.show()

    sys.exit(app.exec_())