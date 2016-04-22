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
        self.link_ids = []
        self.draw_row = core_id % networkAttr.CORE_COLS
        self.draw_col = math.floor(core_id / networkAttr.CORE_COLS)
        self.row = None
        self.col = None
        # Graphics Options
        self.size = QtCore.QSizeF(drawAttr.CORE_SIZE, drawAttr.CORE_SIZE)
        self.setMinimumSize(drawAttr.CORE_SIZE, drawAttr.CORE_SIZE)
        # Pixel positions
        self.top_left_corner = QtCore.QPointF(self.draw_row * drawAttr.CORE_SIZE + self.draw_row * drawAttr.LINK_LENGTH,
                                              self.draw_col * drawAttr.CORE_SIZE + self.draw_col * drawAttr.LINK_LENGTH)
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
        if self.draw_col + 1 < networkAttr.CORE_COLS:
            self.buffers.append(Buffer(self.core_id, self.top_left_corner, "South"))
        if self.draw_col - 1 >= 0:
            self.buffers.append(Buffer(self.core_id, self.top_left_corner, "North"))
        if self.draw_row + 1 < networkAttr.CORE_ROWS:
            self.buffers.append(Buffer(self.core_id, self.top_left_corner, "East"))
        if self.draw_row - 1 >= 0:
            self.buffers.append(Buffer(self.core_id, self.top_left_corner, "West"))
        self.buffers.append(Buffer(self.core_id, self.top_left_corner, "Core"))

    def draw_core(self, painter):
        painter.drawRect(self.rect)
        painter.drawText(self.text_id_pos, self.text_id)
        for buf in self.buffers:
            buf.draw_buffer(painter)

    def get_buffers(self):
        return self.buffers

    def update_core(self, updated_router_flits, possible_link_flits):
        for buf in self.buffers:
            flits_per_buffer = []
            for flit in updated_router_flits:
                if flit.in_dir == buf.link_dir:
                    flits_per_buffer.append(flit)
            for link_flit in possible_link_flits:
                for buf_flit in buf.flits:
                    if buf_flit.id == link_flit.id:
                        flits_per_buffer.append(buf_flit)
            # for flit in buf.flits:
            #     if flit.get_on_link() is True:
            #         pass
            #     elif flit.dest == self.core_id:
            #         pass
            #     elif flit.outport == "Core":
            #         pass
            #     else:
            #         flits_per_buffer.append(flit)
            print(self.core_id)
            print (buf.link_dir)
            print (flits_per_buffer)
            buf.update_buffer(flits_per_buffer)

    def set_core_id(self, core_id):
        self.core_id = core_id
        self.text_id = str(self.core_id)
        self.col = core_id % networkAttr.CORE_COLS
        self.row = math.floor(core_id / networkAttr.CORE_COLS)

    def __str__(self):
        string = "[Core::"
        string += " Id:" + str(self.core_id)
        string += " Row:" + str(self.row)
        string += " Col:" + str(self.col)
        string += " Draw_Row:" + str(self.draw_row)
        string += " Draw_Col:" + str(self.draw_col)
        string += "\n\r"
        return string

    def __repr__(self):
        string = "[Core::"
        string += " Id:" + str(self.core_id)
        string += " Row:" + str(self.row)
        string += " Col:" + str(self.col)
        string += " Draw_Row:" + str(self.draw_row)
        string += " Draw_Col:" + str(self.draw_col)
        string += "\n\r"
        return string

    def get_buffer(self, direction):
        for buffer in self.buffers:
            if buffer.link_dir == direction:
                return buffer
        return None

    def add_link_id(self, id):
        self.link_ids.append(id)