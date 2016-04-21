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
        self.updated_link_flits = []
        # Graphics Size in Pixels
        self.size = QtCore.QSizeF()
        # Pixel Position
        self.top_left_corner = QtCore.QPointF()
        # Setting up Graphics
        self.setup_grapics_points()
        self.setMinimumSize(self.size.width(), self.size.height())
        # Link Rectangle Object
        self.rect = QtCore.QRectF(self.top_left_corner, self.size)
        self.set_link_id()

    # Orients Link direction and pixel placement
    def setup_grapics_points(self):
        if self.core_send.row == self.core_rec.row and self.core_send.col < self.core_rec.col:
            self.link_dir = "South"
            self.setup_graphics_link_attr()
        elif self.core_send.row == self.core_rec.row and self.core_send.col > self.core_rec.col:
            self.link_dir = "North"
            self.setup_graphics_link_attr()
        elif self.core_send.row > self.core_rec.row and self.core_send.col == self.core_rec.col:
            self.link_dir = "West"
            self.setup_graphics_link_attr()
        elif self.core_send.row < self.core_rec.row and self.core_send.col == self.core_rec.col:
            self.link_dir = "East"
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
            link_gen_xoffset = self.core_send.row * drawAttr.CORE_SIZE + self.core_send.row * drawAttr.LINK_LENGTH
            link_gen_yoffset = self.core_send.col * drawAttr.CORE_SIZE + self.core_send.col * drawAttr.LINK_LENGTH
        elif self.link_dir is "North" or self.link_dir is "West":
            link_gen_xoffset = self.core_rec.row * drawAttr.CORE_SIZE + self.core_rec.row * drawAttr.LINK_LENGTH
            link_gen_yoffset = self.core_rec.col * drawAttr.CORE_SIZE + self.core_rec.col * drawAttr.LINK_LENGTH

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

    def update_link(self, updated_link_flits):
        self.updated_link_flits = updated_link_flits

    def set_link_id(self):
        #forumla for number of horizontal links in system
        #   (cols - 1)*num_of_rows
        #formula for number of vertical links in system
        #   (rows - 1)*num_of_cols
        #formula for number of horizontal links up to me
        # (my_row) * (cols - 1) +
        #formula for my link number
        # num_cores + (
        link_id = 2*networkAttr.CORE_CORES
        row = self.core_send.row
        col = self.core_send.col
        if self.link_dir is "East":
            link_id += row * (networkAttr.CORE_COLS - 1) + col
        elif self.link_dir is "West":
            link_id += row * (networkAttr.CORE_COLS - 1) + col - 1
        if self.link_dir is "North":
            link_id += (networkAttr.CORE_COLS - 1) * networkAttr.CORE_ROWS
            link_id += row * networkAttr.CORE_COLS + col - networkAttr.CORE_COLS
        elif self.link_dir is "South":
            link_id += (networkAttr.CORE_COLS - 1) * networkAttr.CORE_ROWS
            link_id += row * networkAttr.CORE_COLS + col
        self.link_id = link_id

    def get_link_id(self):
        return self.link_id