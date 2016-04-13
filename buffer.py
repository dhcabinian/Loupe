import math
from PyQt4 import QtCore
from networkAttr import networkAttr
from drawAttr import drawAttr


# Buffer Implementation
class Buffer(object):
    # static variables
    ROW_SEPARATION = 4
    # Offsets give the midpoint of each edge of core rectangle
    NORTH_OFFSET = [drawAttr.DRAW_CORE_SIZE / 2, 0]
    SOUTH_OFFSET = [drawAttr.DRAW_CORE_SIZE / 2, drawAttr.DRAW_CORE_SIZE]
    EAST_OFFSET = [drawAttr.DRAW_CORE_SIZE, drawAttr.DRAW_CORE_SIZE / 2]
    WEST_OFFSET = [0, drawAttr.DRAW_CORE_SIZE / 2]
    CORE_OFFSET = [drawAttr.DRAW_CORE_SIZE / 2, drawAttr.DRAW_CORE_SIZE / 2 - 15]

    def __init__(self, core_id, core_topLeftCorner, direction):
        super(Buffer, self).__init__()
        # Buffer Information
        self.core_id = core_id
        self.link_dir = direction
        # Graphics Size in Pixels
        self.size = QtCore.QSizeF()
        # Pixel Positions
        self.core_topLeftCorner = core_topLeftCorner
        self.topLeftCorners = []
        # Buffer Rectangles List
        self.rects = []
        # Buffer Labels
        self.bufferVCIdsText = []
        self.buffervCIdsTextPos = []
        # Setting up Graphics
        self.setupGrapicsPoints()

    def setupGrapicsPoints(self):
        if networkAttr.ATTR_CORE_VCS / Buffer.ROW_SEPARATION >= 1:
            # create rows of 4 VCs
            length = math.floor(drawAttr.DRAW_CORE_SIZE / (
                Buffer.ROW_SEPARATION + 2 * math.ceil(networkAttr.ATTR_CORE_VCS / Buffer.ROW_SEPARATION)))
            self.size.setHeight(length)
            self.size.setWidth(length)
            count = 0
            for vc in range(networkAttr.ATTR_CORE_VCS):
                row_num = math.ceil(vc / Buffer.ROW_SEPARATION)
                # from perspective of center of core
                xpos = 0
                ypos = 0
                if count % Buffer.ROW_SEPARATION == 0:
                    # Middle Left
                    if self.link_dir == "NORTH":
                        xpos = self.core_topLeftCorner.x() + Buffer.NORTH_OFFSET[0] - self.size.height()
                        ypos = self.core_topLeftCorner.y() + Buffer.NORTH_OFFSET[1] + self.size.height() * row_num
                    elif self.link_dir == "SOUTH":
                        xpos = self.core_topLeftCorner.x() + Buffer.SOUTH_OFFSET[0]
                        ypos = self.core_topLeftCorner.y() + Buffer.SOUTH_OFFSET[1] - self.size.height() * row_num \
                               - self.size.height()
                    elif self.link_dir == "EAST":
                        xpos = self.core_topLeftCorner.x() + Buffer.EAST_OFFSET[0] - self.size.height() * row_num \
                               - self.size.height()
                        ypos = self.core_topLeftCorner.y() + Buffer.EAST_OFFSET[1]
                    elif self.link_dir == "WEST":
                        xpos = self.core_topLeftCorner.x() + Buffer.WEST_OFFSET[0] + self.size.height() * row_num
                        ypos = self.core_topLeftCorner.y() + Buffer.WEST_OFFSET[1]
                    elif self.link_dir == "CORE":
                        xpos = self.core_topLeftCorner.x() + Buffer.CORE_OFFSET[0] - self.size.height()
                        ypos = self.core_topLeftCorner.y() + Buffer.CORE_OFFSET[1] - self.size.height() * row_num
                elif count % Buffer.ROW_SEPARATION == 1:
                    # Middle Right
                    if self.link_dir == "NORTH":
                        xpos = self.core_topLeftCorner.x() + Buffer.NORTH_OFFSET[0]
                        ypos = self.core_topLeftCorner.y() + Buffer.NORTH_OFFSET[1] + self.size.height() * row_num \
                               - self.size.height()
                    elif self.link_dir == "SOUTH":
                        xpos = self.core_topLeftCorner.x() + Buffer.SOUTH_OFFSET[0] - self.size.height()
                        ypos = self.core_topLeftCorner.y() + Buffer.SOUTH_OFFSET[1] - self.size.height() * row_num
                    elif self.link_dir == "EAST":
                        xpos = self.core_topLeftCorner.x() + Buffer.EAST_OFFSET[0] - self.size.height() * row_num
                        ypos = self.core_topLeftCorner.y() + Buffer.EAST_OFFSET[1] - self.size.height()
                    elif self.link_dir == "WEST":
                        xpos = self.core_topLeftCorner.x() + Buffer.WEST_OFFSET[0] + self.size.height() * row_num \
                               - self.size.height()
                        ypos = self.core_topLeftCorner.y() + Buffer.WEST_OFFSET[1] - self.size.height()
                    elif self.link_dir == "CORE":
                        xpos = self.core_topLeftCorner.x() + Buffer.CORE_OFFSET[0]
                        ypos = self.core_topLeftCorner.y() + Buffer.CORE_OFFSET[1] - self.size.height() * row_num \
                               + self.size.height()
                elif count % Buffer.ROW_SEPARATION == 2:
                    # Outer Left
                    if self.link_dir == "NORTH":
                        xpos = self.core_topLeftCorner.x() + Buffer.NORTH_OFFSET[0] - 2 * self.size.height()
                        ypos = self.core_topLeftCorner.y() + Buffer.NORTH_OFFSET[1] + self.size.height() * row_num \
                               - self.size.height()
                    elif self.link_dir == "SOUTH":
                        xpos = self.core_topLeftCorner.x() + Buffer.SOUTH_OFFSET[0] + self.size.height()
                        ypos = self.core_topLeftCorner.y() + Buffer.SOUTH_OFFSET[1] - self.size.height() * row_num
                    elif self.link_dir == "EAST":
                        xpos = self.core_topLeftCorner.x() + Buffer.EAST_OFFSET[0] - self.size.height() * row_num
                        ypos = self.core_topLeftCorner.y() + Buffer.EAST_OFFSET[1] + 2 * self.size.height() \
                               - self.size.height()
                    elif self.link_dir == "WEST":
                        xpos = self.core_topLeftCorner.x() + Buffer.WEST_OFFSET[0] + self.size.height() * row_num \
                               - self.size.height()
                        ypos = self.core_topLeftCorner.y() + Buffer.WEST_OFFSET[1] + self.size.height()
                    elif self.link_dir == "CORE":
                        xpos = self.core_topLeftCorner.x() + Buffer.CORE_OFFSET[0] - 2 * self.size.height()
                        ypos = self.core_topLeftCorner.y() + Buffer.CORE_OFFSET[1] - self.size.height() * row_num \
                               + self.size.height()
                elif count % Buffer.ROW_SEPARATION == 3:
                    # Outer Right
                    if self.link_dir == "NORTH":
                        xpos = self.core_topLeftCorner.x() + Buffer.NORTH_OFFSET[0] + self.size.height()
                        ypos = self.core_topLeftCorner.y() + Buffer.NORTH_OFFSET[1] + self.size.height() * row_num \
                               - self.size.height()
                    elif self.link_dir == "SOUTH":
                        xpos = self.core_topLeftCorner.x() + Buffer.SOUTH_OFFSET[0] - self.size.height() * 2
                        ypos = self.core_topLeftCorner.y() + Buffer.SOUTH_OFFSET[1] - self.size.height() * row_num
                    elif self.link_dir == "EAST":
                        xpos = self.core_topLeftCorner.x() + Buffer.EAST_OFFSET[0] - self.size.height() * row_num
                        ypos = self.core_topLeftCorner.y() + Buffer.EAST_OFFSET[1] - self.size.height() \
                               - self.size.height()
                    elif self.link_dir == "WEST":
                        xpos = self.core_topLeftCorner.x() + Buffer.WEST_OFFSET[0] + self.size.height() * row_num \
                               - self.size.height()
                        ypos = self.core_topLeftCorner.y() + Buffer.WEST_OFFSET[1] - 2 * self.size.height()
                    elif self.link_dir == "CORE":
                        xpos = self.core_topLeftCorner.x() + Buffer.CORE_OFFSET[0] + self.size.height()
                        ypos = self.core_topLeftCorner.y() + Buffer.CORE_OFFSET[1] - self.size.height() * row_num \
                               + self.size.height()
                self.topLeftCorners.append(QtCore.QPointF(xpos, ypos))
                self.rects.append(QtCore.QRectF(self.topLeftCorners[count], self.size))
                count += 1
            # Sort Rects into actual VC ordering
            fullRows = math.floor(networkAttr.ATTR_CORE_VCS / Buffer.ROW_SEPARATION)
            lastRow = networkAttr.ATTR_CORE_VCS % Buffer.ROW_SEPARATION
            tempRects = []
            for row in range(fullRows):
                tempRects.append(self.rects[row * Buffer.ROW_SEPARATION + 2])
                tempRects.append(self.rects[row * Buffer.ROW_SEPARATION + 0])
                tempRects.append(self.rects[row * Buffer.ROW_SEPARATION + 1])
                tempRects.append(self.rects[row * Buffer.ROW_SEPARATION + 3])
            if lastRow == 0:
                pass
            elif lastRow == 1:
                tempRects.append(self.rects[fullRows * Buffer.ROW_SEPARATION + 0])
            elif lastRow == 2:
                tempRects.append(self.rects[fullRows * Buffer.ROW_SEPARATION + 0])
                tempRects.append(self.rects[fullRows * Buffer.ROW_SEPARATION + 1])
            elif lastRow == 3:
                tempRects.append(self.rects[fullRows * Buffer.ROW_SEPARATION + 2])
                tempRects.append(self.rects[fullRows * Buffer.ROW_SEPARATION + 0])
                tempRects.append(self.rects[fullRows * Buffer.ROW_SEPARATION + 1])
            self.rects = tempRects
            for vc_id, rect in enumerate(self.rects):
                self.bufferVCIdsText.append(str(vc_id))
                pos = rect.center()
                pos.setY(pos.y() + 5)
                pos.setX(pos.x() - 3)
                self.buffervCIdsTextPos.append(pos)
        else:
            # create single row of VCs
            length = math.floor(drawAttr.DRAW_CORE_SIZE / (networkAttr.ATTR_CORE_VCS + 2))
            self.size.setHeight(length)
            self.size.setWidth(length)

    def drawBuffer(self, painter):
        for index, VC in enumerate(self.rects):
            painter.drawRect(VC)
            painter.drawText(self.buffervCIdsTextPos[index], self.bufferVCIdsText[index])