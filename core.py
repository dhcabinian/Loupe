import math
from PyQt4 import QtCore, QtGui
from buffer import Buffer
from networkAttr import networkAttr
from drawAttr import drawAttr


# Core Implementation
class Core(QtGui.QWidget):
    def __init__(self, core_id):
        super(Core, self).__init__()
        # Core Information
        self.core_id = core_id
        self.buffers = []
        self.row = core_id % networkAttr.CORE_COLS
        self.col = math.floor(core_id / networkAttr.CORE_COLS)
        # Graphics Options
        self.size = QtCore.QSizeF(drawAttr.CORE_SIZE, drawAttr.CORE_SIZE)
        self.setMinimumSize(drawAttr.CORE_SIZE, drawAttr.CORE_SIZE)
        # Pixel positions
        self.top_left_corner = QtCore.QPointF(self.row * drawAttr.CORE_SIZE + self.row * drawAttr.LINK_LENGTH,
                                              self.col * drawAttr.CORE_SIZE + self.col * drawAttr.LINK_LENGTH)
        # Core Rectangle Object
        self.rect = QtCore.QRectF(self.top_left_corner, self.size)
        self.text_id = str(self.core_id)
        self.text_id_pos = QtCore.QPointF()
        self.create_buffers()
        self.create_core_id_text()

    def create_core_id_text(self):
        pos = self.rect.center()
        pos.setY(pos.y() + 15)
        self.text_id_pos = pos

    def create_buffers(self):
        # Create Buffers
        if self.col + 1 < networkAttr.CORE_COLS:
            self.buffers.append(Buffer(self.core_id, self.top_left_corner, "South"))
        if self.col - 1 >= 0:
            self.buffers.append(Buffer(self.core_id, self.top_left_corner, "North"))
        if self.row + 1 < networkAttr.CORE_ROWS:
            self.buffers.append(Buffer(self.core_id, self.top_left_corner, "East"))
        if self.row - 1 >= 0:
            self.buffers.append(Buffer(self.core_id, self.top_left_corner, "West"))
        self.buffers.append(Buffer(self.core_id, self.top_left_corner, "Core"))

    def draw_core(self, painter):
        painter.drawRect(self.rect)
        painter.drawText(self.text_id_pos, self.text_id)
        for buf in self.buffers:
            buf.draw_buffer(painter)

    def get_buffers(self):
        return self.buffers

    def update_core(self):
        for buf in self.buffers:
            buf.update_buffer()
