from PyQt4 import QtCore, QtGui
from drawAttr import drawAttr
from networkAttr import networkAttr

class Link(QtGui.QWidget):
    def __init__(self, core_send, core_rec):
        super(Link, self).__init__()
        # Link Information
        self.core_send = core_send
        self.core_rec = core_rec
        self.link_id = None
        # String indicating link direction
        self.link_dir = ""
        # Flit in Link
        self.link_flit = None
        # Graphics Size in Pixels
        self.size = QtCore.QSizeF()
        # Pixel Position
        self.top_left_corner = QtCore.QPointF()
        # Setting up Graphics
        self.setup_grapics_points()
        self.setMinimumSize(self.size.width(), self.size.height())
        # Link Rectangle Object
        self.rect = QtCore.QRectF(self.top_left_corner, self.size)
        self.text_id_pos = QtCore.QPointF()
        self.set_link_id()
        self.create_link_id_text()

    # Orients Link direction and pixel placement
    def setup_grapics_points(self):
        if self.core_send.row == self.core_rec.row and self.core_send.col < self.core_rec.col:
            self.link_dir = "East"
            self.setup_graphics_link_attr()
        elif self.core_send.row == self.core_rec.row and self.core_send.col > self.core_rec.col:
            self.link_dir = "West"
            self.setup_graphics_link_attr()
        elif self.core_send.row > self.core_rec.row and self.core_send.col == self.core_rec.col:
            self.link_dir = "South"
            self.setup_graphics_link_attr()
        elif self.core_send.row < self.core_rec.row and self.core_send.col == self.core_rec.col:
            self.link_dir = "North"
            self.setup_graphics_link_attr()

    def setup_graphics_link_attr(self):
        #Set Link Orientation
        if self.link_dir is "North" or self.link_dir is "South":
            self.size.setHeight(drawAttr.LINK_LENGTH)
            self.size.setWidth(drawAttr.LINK_WIDTH)
        elif self.link_dir is "East" or self.link_dir is "West":
            self.size.setHeight(drawAttr.LINK_WIDTH)
            self.size.setWidth(drawAttr.LINK_LENGTH)

        #Set Link Position
        link_gen_xoffset = None
        link_gen_yoffset = None
        if self.link_dir is "East" or self.link_dir is "South":
            link_gen_xoffset = self.core_send.draw_row * drawAttr.CORE_SIZE + self.core_send.draw_row * drawAttr.LINK_LENGTH
            link_gen_yoffset = self.core_send.draw_col * drawAttr.CORE_SIZE + self.core_send.draw_col * drawAttr.LINK_LENGTH
        elif self.link_dir is "North" or self.link_dir is "West":
            link_gen_xoffset = self.core_rec.draw_row * drawAttr.CORE_SIZE + self.core_rec.draw_row * drawAttr.LINK_LENGTH
            link_gen_yoffset = self.core_rec.draw_col * drawAttr.CORE_SIZE + self.core_rec.draw_col * drawAttr.LINK_LENGTH

        if self.link_dir is "North":
            link_gen_xoffset += drawAttr.CORE_SIZE / 2
            link_gen_yoffset += drawAttr.CORE_SIZE
        elif self.link_dir is "East":
            link_gen_xoffset += drawAttr.CORE_SIZE
            link_gen_yoffset += drawAttr.CORE_SIZE / 2
        elif self.link_dir is "South":
            link_gen_xoffset += drawAttr.CORE_SIZE / 2 - drawAttr.LINK_WIDTH
            link_gen_yoffset += drawAttr.CORE_SIZE
        elif self.link_dir is "West":
            link_gen_xoffset += drawAttr.CORE_SIZE
            link_gen_yoffset += drawAttr.CORE_SIZE / 2 - drawAttr.LINK_WIDTH

        self.top_left_corner.setX(link_gen_xoffset)
        self.top_left_corner.setY(link_gen_yoffset)

    def draw_link(self, painter):
        painter.drawRect(self.rect)
        if not self.link_flit:
            pass
        else:
            painter.fillRect(self.rect, self.link_flit[0].color)

    def create_link_id_text(self):
        pos = self.rect.center()
        self.text_id_pos = pos

    def update_link(self, updated_link_flit):
        self.link_flit = updated_link_flit

    def set_link_id(self):
        link_id = 2*networkAttr.CORE_CORES
        if self.link_dir is "East" or self.link_dir is "West":
            link_id += (min(self.core_send.core_id, self.core_rec.core_id) - self.core_send.row)
        if self.link_dir is "North" or self.link_dir is "South":
            offset = min(self.core_send.core_id, self.core_rec.core_id)
            num_e_w_links = (networkAttr.CORE_COLS - 1) * networkAttr.CORE_ROWS
            link_id += num_e_w_links + offset
        self.link_id = link_id

    def get_link_id(self):
        return self.link_id