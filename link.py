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
        # Graphics Size in Pixels
        self.size = QtCore.QSizeF()
        # Pixel Position
        self.topLeftCorner = QtCore.QPointF()
        # Setting up Graphics
        self.setupGrapicsPoints()
        self.setMinimumSize(self.size.width(), self.size.height())
        # Link Rectangle Object
        self.rect = QtCore.QRectF(self.topLeftCorner, self.size)

    # Orients Link direction and pixel placement
    def setupGrapicsPoints(self):
        if self.core_send.row == self.core_rec.row and self.core_send.col < self.core_rec.col:
            self.link_dir = "SOUTH"
            self.size.setHeight(drawAttr.DRAW_LINK_LENGTH)
            self.size.setWidth(drawAttr.DRAW_LINK_WIDTH)
            self.topLeftCorner.setX(self.core_send.row * drawAttr.DRAW_CORE_SIZE
                                    + self.core_send.row * drawAttr.DRAW_LINK_LENGTH + drawAttr.DRAW_CORE_SIZE / 2
                                    - drawAttr.DRAW_LINK_WIDTH)
            self.topLeftCorner.setY(self.core_send.col * drawAttr.DRAW_CORE_SIZE
                                    + self.core_send.col * drawAttr.DRAW_LINK_LENGTH + drawAttr.DRAW_CORE_SIZE)
        elif self.core_send.row == self.core_rec.row and self.core_send.col > self.core_rec.col:
            self.link_dir = "NORTH"
            self.size.setHeight(drawAttr.DRAW_LINK_LENGTH)
            self.size.setWidth(drawAttr.DRAW_LINK_WIDTH)
            self.topLeftCorner.setX(self.core_rec.row * drawAttr.DRAW_CORE_SIZE
                                    + self.core_rec.row * drawAttr.DRAW_LINK_LENGTH + drawAttr.DRAW_CORE_SIZE / 2)
            self.topLeftCorner.setY(self.core_rec.col * drawAttr.DRAW_CORE_SIZE
                                    + self.core_rec.col * drawAttr.DRAW_LINK_LENGTH + drawAttr.DRAW_CORE_SIZE)
        elif self.core_send.row > self.core_rec.row and self.core_send.col == self.core_rec.col:
            self.link_dir = "WEST"
            self.size.setHeight(drawAttr.DRAW_LINK_WIDTH)
            self.size.setWidth(drawAttr.DRAW_LINK_LENGTH)
            self.topLeftCorner.setX(self.core_rec.row * drawAttr.DRAW_CORE_SIZE
                                    + self.core_rec.row * drawAttr.DRAW_LINK_LENGTH + drawAttr.DRAW_CORE_SIZE)
            self.topLeftCorner.setY(self.core_rec.col * drawAttr.DRAW_CORE_SIZE
                                    + self.core_rec.col * drawAttr.DRAW_LINK_LENGTH + drawAttr.DRAW_CORE_SIZE / 2
                                    - drawAttr.DRAW_LINK_WIDTH)
        elif self.core_send.row < self.core_rec.row and self.core_send.col == self.core_rec.col:
            self.link_dir = "EAST"
            self.size.setHeight(drawAttr.DRAW_LINK_WIDTH)
            self.size.setWidth(drawAttr.DRAW_LINK_LENGTH)
            self.topLeftCorner.setX(self.core_send.row * drawAttr.DRAW_CORE_SIZE
                                    + self.core_send.row * drawAttr.DRAW_LINK_LENGTH + drawAttr.DRAW_CORE_SIZE)
            self.topLeftCorner.setY(self.core_send.col * drawAttr.DRAW_CORE_SIZE
                                    + self.core_send.col * drawAttr.DRAW_LINK_LENGTH + drawAttr.DRAW_CORE_SIZE / 2)

    def drawLink(self, painter):
        painter.drawRect(self.rect)