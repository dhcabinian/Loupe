from PyQt4 import QtGui, QtCore
from drawAttr import drawAttr
from networkAttr import networkAttr
from buffer import Buffer


class CoreExploded(QtGui.QWidget):

    def __init__(self, parent, CoreIn):
        super(CoreExploded, self).__init__()
        self.setParent(parent)
        # Core Information
        self.core_id = None
        self.buffers = []
        # # Row and Column
        self.row = None
        self.col = None
        # Graphics Options
        self.size = QtCore.QSizeF(drawAttr.DRAW_CORE_SIZE_EXP, drawAttr.DRAW_CORE_SIZE_EXP)
        self.setMinimumSize(drawAttr.DRAW_CORE_SIZE_EXP, drawAttr.DRAW_CORE_SIZE_EXP)
        # Pixel positions
        self.topLeftCorner = QtCore.QPointF(20, 20)
        # Core Rectangle Object
        self.rect = QtCore.QRectF(self.topLeftCorner, self.size)
        self.textId = None
        self.textIdPos = QtCore.QPointF()
        self.updateCore(CoreIn)

    def updateCore(self, CoreIn):
                # Core Information
        self.core_id = CoreIn.core_id
        self.buffers = []
        # Row and Column
        self.row = CoreIn.row
        self.col = CoreIn.col
        # Graphics Options
        self.textId = str(self.core_id)
        self.createBuffers()
        self.createCoreIdText()

    def drawCore(self, painter):
        painter.drawRect(self.rect)
        painter.drawText(self.textIdPos, self.textId)
        for buf in self.buffers:
            buf.drawBuffer(painter)

    def createCoreIdText(self):
        pos = self.rect.center()
        pos.setY(pos.y() + 15)
        self.textIdPos = pos

    def createBuffers(self):
        # Create Buffers
        if self.col + 1 < networkAttr.ATTR_CORE_COLS:
            self.buffers.append(Buffer(self.core_id, self.topLeftCorner, "SOUTH", 1))
        if self.col - 1 >= 0:
            self.buffers.append(Buffer(self.core_id, self.topLeftCorner, "NORTH", 1))
        if self.row + 1 < networkAttr.ATTR_CORE_ROWS:
            self.buffers.append(Buffer(self.core_id, self.topLeftCorner, "EAST", 1))
        if self.row - 1 >= 0:
            self.buffers.append(Buffer(self.core_id, self.topLeftCorner, "WEST", 1))
        self.buffers.append(Buffer(self.core_id, self.topLeftCorner, "CORE", 1))

    def paintEvent(self, event):
        painter = QtGui.QPainter()
        painter.begin(self)
        #qp.setWindow(0, -21, 750, 750)
        #qp.translate(0, 21)
        self.drawCore(painter)
        painter.end()