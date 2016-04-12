import math
from PyQt4 import QtCore, QtGui
from buffer import Buffer
from networkAttr import networkAttr
from drawAttr import drawAttr


# Core Implementation
class Core(QtGui.QWidget):
    def __init__(self, core_id, vcs_per_vnet, num_cols):
        super(Core, self).__init__()
        # Core Information
        self.core_id = core_id
        self.buffers = []
        # Row and Column
        self.row = core_id % networkAttr.ATTR_CORE_COLS
        self.col = math.floor(core_id / networkAttr.ATTR_CORE_COLS)
        # Graphics Size in Pixels
        self.size = QtCore.QSizeF(drawAttr.DRAW_CORE_SIZE, drawAttr.DRAW_CORE_SIZE)
        # Pixel positions
        self.topLeftCorner = QtCore.QPointF(self.row * drawAttr.DRAW_CORE_SIZE + self.row * drawAttr.DRAW_LINK_LENGTH,
                                            self.col * drawAttr.DRAW_CORE_SIZE + self.col * drawAttr.DRAW_LINK_LENGTH)
        # Core Rectangle Object
        self.rect = QtCore.QRectF(self.topLeftCorner, self.size)
        self.textId =str(self.core_id)
        self.textIdPos = QtCore.QPointF()
        self.createBuffers()

    def createCoreIdText(self):
        pos = self.rect.center()
        pos.setY(pos.y() + 15)
        self.textIdPos = pos

    def createBuffers(self):
        # Create Buffers
        if self.col + 1 < networkAttr.ATTR_CORE_COLS:
            self.buffers.append(Buffer(self.core_id, self.topLeftCorner, "SOUTH"))
        if self.col - 1 >= 0:
            self.buffers.append(Buffer(self.core_id, self.topLeftCorner, "NORTH"))
        if self.row + 1 < networkAttr.ATTR_CORE_ROWS:
            self.buffers.append(Buffer(self.core_id, self.topLeftCorner, "EAST"))
        if self.row - 1 >= 0:
            self.buffers.append(Buffer(self.core_id, self.topLeftCorner, "WEST"))
        self.buffers.append(Buffer(self.core_id, self.topLeftCorner, "CORE"))

    def drawCore(self, painter):
        painter.drawRect(self.rect)
        painter.drawText(self.textIdPos, self.textId)
        for buf in self.buffers:
            buf.drawBuffer(painter)

