from PyQt4 import QtGui, QtCore
from drawAttr import drawAttr
from networkAttr import networkAttr
from buffer import Buffer


class CoreExploded(QtGui.QWidget):
    CORE_EXP_X_OFFSET = 20
    CORE_EXP_Y_OFFSET = 20
    CORE_ID_Y_OFFSET = 15

    def __init__(self, parent_widget, core_in):
        super(CoreExploded, self).__init__()
        self.setParent(parent_widget)
        # Core Information
        self.core_id = None
        self.buffers = []
        # # Row and Column
        self.row = None
        self.col = None
        # Graphics Options
        self.size = QtCore.QSizeF(drawAttr.CORE_SIZE_EXP, drawAttr.CORE_SIZE_EXP)
        self.setMinimumSize(drawAttr.CORE_SIZE_EXP, drawAttr.CORE_SIZE_EXP)
        # Pixel positions
        self.topLeftCorner = QtCore.QPointF(CoreExploded.CORE_EXP_X_OFFSET, CoreExploded.CORE_EXP_Y_OFFSET)
        # Core Rectangle Object
        self.rect = QtCore.QRectF(self.topLeftCorner, self.size)
        self.text_id = None
        self.text_id_pos = QtCore.QPointF()
        self.update_core(core_in)

    def update_core(self, core_in):
        # Core Information
        self.core_id = core_in.core_id
        self.buffers = []
        # Row and Column
        self.row = core_in.row
        self.col = core_in.col
        # Graphics Options
        self.text_id = str(self.core_id)
        self.create_buffers()
        self.create_core_id_text()

    def draw_core(self, painter):
        painter.drawRect(self.rect)
        painter.drawText(self.text_id_pos, self.text_id)
        for buf in self.buffers:
            buf.draw_buffer(painter)

    def create_core_id_text(self):
        pos = self.rect.center()
        pos.setY(pos.y() + CoreExploded.CORE_ID_Y_OFFSET)
        self.text_id_pos = pos

    def create_buffers(self):
        # Create Buffers
        if self.col + 1 < networkAttr.CORE_COLS:
            self.buffers.append(Buffer(self.core_id, self.topLeftCorner, "SOUTH", 1))
        if self.col - 1 >= 0:
            self.buffers.append(Buffer(self.core_id, self.topLeftCorner, "NORTH", 1))
        if self.row + 1 < networkAttr.CORE_ROWS:
            self.buffers.append(Buffer(self.core_id, self.topLeftCorner, "EAST", 1))
        if self.row - 1 >= 0:
            self.buffers.append(Buffer(self.core_id, self.topLeftCorner, "WEST", 1))
        self.buffers.append(Buffer(self.core_id, self.topLeftCorner, "CORE", 1))

    def paintEvent(self, event):
        painter = QtGui.QPainter()
        painter.begin(self)
        self.draw_core(painter)
        painter.end()

    def update_core_exploded(self):
        pass
