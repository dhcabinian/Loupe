from PyQt4 import QtCore, QtGui
from drawAttr import drawAttr


class Link(QtGui.QWidget):
    def __init__(self, core_send, core_rec):
        super(Link, self).__init__()
        # Link Information
        self.core_send = core_send
        self.core_rec = core_rec
        # String indicating link direction
        self.link_dir = ""
        # Flit in Link
        self.current_flit = None
        # Graphics Size in Pixels
        self.size = QtCore.QSizeF()
        # Pixel Position
        self.top_left_corner = QtCore.QPointF()
        # Setting up Graphics
        self.setup_grapics_points()
        self.setMinimumSize(self.size.width(), self.size.height())
        # Link Rectangle Object
        self.rect = QtCore.QRectF(self.top_left_corner, self.size)

    # Orients Link direction and pixel placement
    def setup_grapics_points(self):
        if self.core_send.row == self.core_rec.row and self.core_send.col < self.core_rec.col:
            self.link_dir = "SOUTH"
            self.setup_graphics_link_attr()
        elif self.core_send.row == self.core_rec.row and self.core_send.col > self.core_rec.col:
            self.link_dir = "NORTH"
            self.setup_graphics_link_attr()
        elif self.core_send.row > self.core_rec.row and self.core_send.col == self.core_rec.col:
            self.link_dir = "WEST"
            self.setup_graphics_link_attr()
        elif self.core_send.row < self.core_rec.row and self.core_send.col == self.core_rec.col:
            self.link_dir = "EAST"
            self.setup_graphics_link_attr()

    def setup_graphics_link_attr(self):
        #Set Link Orientation
        if self.link_dir is "NORTH" or self.link_dir is "SOUTH":
            self.size.setHeight(drawAttr.LINK_LENGTH)
            self.size.setWidth(drawAttr.LINK_WIDTH)
        elif self.link_dir is "EAST" or self.link_dir is "WEST":
            self.size.setHeight(drawAttr.LINK_WIDTH)
            self.size.setWidth(drawAttr.LINK_LENGTH)

        #Set Link Position
        link_gen_xoffset = None
        link_gen_yoffset = None
        if self.link_dir is "EAST" or self.link_dir is "SOUTH":
            link_gen_xoffset = self.core_send.row * drawAttr.CORE_SIZE + self.core_send.row * drawAttr.LINK_LENGTH
            link_gen_yoffset = self.core_send.col * drawAttr.CORE_SIZE + self.core_send.col * drawAttr.LINK_LENGTH
        elif self.link_dir is "NORTH" or self.link_dir is "WEST":
            link_gen_xoffset = self.core_rec.row * drawAttr.CORE_SIZE + self.core_rec.row * drawAttr.LINK_LENGTH
            link_gen_yoffset = self.core_rec.col * drawAttr.CORE_SIZE + self.core_rec.col * drawAttr.LINK_LENGTH

        if self.link_dir is "NORTH":
            link_gen_xoffset += drawAttr.CORE_SIZE / 2
            link_gen_yoffset += drawAttr.CORE_SIZE
        elif self.link_dir is "EAST":
            link_gen_xoffset += drawAttr.CORE_SIZE
            link_gen_yoffset += drawAttr.CORE_SIZE / 2
        elif self.link_dir is "SOUTH":
            link_gen_xoffset += drawAttr.CORE_SIZE / 2 - drawAttr.LINK_WIDTH
            link_gen_yoffset += drawAttr.CORE_SIZE
        elif self.link_dir is "WEST":
            link_gen_xoffset += drawAttr.CORE_SIZE
            link_gen_yoffset += drawAttr.CORE_SIZE / 2 - drawAttr.LINK_WIDTH

        self.top_left_corner.setX(link_gen_xoffset)
        self.top_left_corner.setY(link_gen_yoffset)

    def draw_link(self, painter):
        painter.drawRect(self.rect)

    def update_link(self):
        pass
