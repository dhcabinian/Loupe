from PyQt4 import QtGui, QtCore

class CoreInfo(QtGui.QWidget):
    def __init__(self, parent, CoreIn):
        super(CoreInfo, self).__init__()
        self.setParent(parent)
        # Core Information
        self.core_id = None
        self.buffers = []
        self.textInfo = []
        self.textInfoPos = []
        self.createTextInfoPositions()
        self.updateCoreInfo(CoreIn)

    def updateCoreInfo(self, CoreIn):
        self.buffers = CoreIn.getBuffers()
        self.core_id = CoreIn.core_id
        self.updateText(CoreIn)

    def updateText(self, CoreIn):
        self.textInfo = []
        for buf in self.buffers:
            self.textInfo.append(str(buf))

    def createTextInfoPositions(self):
        #Position for each buffer
        for ypos in range(100,200,20):
            self.textInfoPos.append(QtCore.QPointF(0,ypos))

    def paintEvent(self, event):
        painter = QtGui.QPainter()
        painter.begin(self)
        self.drawCoreInfo(painter)
        painter.end()

    def drawCoreInfo(self, painter):
        for index, text in enumerate(self.textInfo):
            painter.drawText(self.textInfoPos[index], self.textInfo[index])