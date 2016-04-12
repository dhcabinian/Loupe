from PyQt4 import QtGui
from network import Network


class Window(QtGui.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 750, 750)
        self.setWindowTitle("Drawing Test")
        self.network = Network("Mesh", 9, 3, 8)
        self.show()

    def paintEvent(self, event):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.network.drawNetwork(qp)
        qp.end()
