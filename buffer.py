import math
from PyQt4 import QtCore
from networkAttr import networkAttr
from drawAttr import drawAttr


# Buffer Implementation
class Buffer(object):
    # static variables
    ROW_DIV = 4
    # Offsets give the midpoint of each edge of core rectangle
    N_OFFSET = [drawAttr.CORE_SIZE / 2, 0]
    S_OFFSET = [drawAttr.CORE_SIZE / 2, drawAttr.CORE_SIZE]
    E_OFFSET = [drawAttr.CORE_SIZE, drawAttr.CORE_SIZE / 2]
    W_OFFSET = [0, drawAttr.CORE_SIZE / 2]
    C_OFFSET = [drawAttr.CORE_SIZE / 2, drawAttr.CORE_SIZE / 2 - 15]

    def __init__(self, core_id, core_top_left_corner, direction, expanded=0):
        super(Buffer, self).__init__()
        if expanded == 1:
            self.set_to_expanded()
        # Buffer Information
        self.core_id = core_id
        self.link_dir = direction
        # Graphics Size in Pixels
        self.size = QtCore.QSizeF()
        # Pixel Positions
        self.core_top_left_corner = core_top_left_corner
        self.top_left_corners = []
        # Buffer Rectangles List
        self.rects = []
        # Buffer Labels
        self.buffer_vc_Ids_text = []
        self.buffer_vc_ids_text_pos = []
        # Setting up Graphics
        self.setup_grapics()

    def setup_grapics(self):
        if networkAttr.CORE_VCS / Buffer.ROW_DIV >= 1:
            self.set_buffer_size()
            for index, vc in enumerate(range(networkAttr.CORE_VCS)):
                row_num = math.ceil(vc / Buffer.ROW_DIV)
                # from perspective of center of core
                xpos = self.core_top_left_corner.x()
                ypos = self.core_top_left_corner.y()
                if index % Buffer.ROW_DIV == 0:
                    # Middle Left
                    if self.link_dir == "NORTH":
                        xpos += Buffer.N_OFFSET[0] - self.size.height()
                        ypos += Buffer.N_OFFSET[1] + self.size.height() * row_num
                    elif self.link_dir == "SOUTH":
                        xpos += Buffer.S_OFFSET[0]
                        ypos += Buffer.S_OFFSET[1] - self.size.height() * row_num - self.size.height()
                    elif self.link_dir == "EAST":
                        xpos += Buffer.E_OFFSET[0] - self.size.height() * row_num - self.size.height()
                        ypos += Buffer.E_OFFSET[1]
                    elif self.link_dir == "WEST":
                        xpos += Buffer.W_OFFSET[0] + self.size.height() * row_num
                        ypos += Buffer.W_OFFSET[1]
                    elif self.link_dir == "CORE":
                        xpos += Buffer.C_OFFSET[0] - self.size.height()
                        ypos += Buffer.C_OFFSET[1] - self.size.height() * row_num
                elif index % Buffer.ROW_DIV == 1:
                    # Middle Right
                    if self.link_dir == "NORTH":
                        xpos += Buffer.N_OFFSET[0]
                        ypos += Buffer.N_OFFSET[1] + self.size.height() * row_num - self.size.height()
                    elif self.link_dir == "SOUTH":
                        xpos += Buffer.S_OFFSET[0] - self.size.height()
                        ypos += Buffer.S_OFFSET[1] - self.size.height() * row_num
                    elif self.link_dir == "EAST":
                        xpos += Buffer.E_OFFSET[0] - self.size.height() * row_num
                        ypos += Buffer.E_OFFSET[1] - self.size.height()
                    elif self.link_dir == "WEST":
                        xpos += Buffer.W_OFFSET[0] + self.size.height() * row_num - self.size.height()
                        ypos += Buffer.W_OFFSET[1] - self.size.height()
                    elif self.link_dir == "CORE":
                        xpos += Buffer.C_OFFSET[0]
                        ypos += Buffer.C_OFFSET[1] - self.size.height() * row_num + self.size.height()
                elif index % Buffer.ROW_DIV == 2:
                    # Outer Left
                    if self.link_dir == "NORTH":
                        xpos += Buffer.N_OFFSET[0] - 2 * self.size.height()
                        ypos += Buffer.N_OFFSET[1] + self.size.height() * row_num - self.size.height()
                    elif self.link_dir == "SOUTH":
                        xpos += Buffer.S_OFFSET[0] + self.size.height()
                        ypos += Buffer.S_OFFSET[1] - self.size.height() * row_num
                    elif self.link_dir == "EAST":
                        xpos += Buffer.E_OFFSET[0] - self.size.height() * row_num
                        ypos += Buffer.E_OFFSET[1] + 2 * self.size.height() - self.size.height()
                    elif self.link_dir == "WEST":
                        xpos += Buffer.W_OFFSET[0] + self.size.height() * row_num - self.size.height()
                        ypos += Buffer.W_OFFSET[1] + self.size.height()
                    elif self.link_dir == "CORE":
                        xpos += Buffer.C_OFFSET[0] - 2 * self.size.height()
                        ypos += Buffer.C_OFFSET[1] - self.size.height() * row_num + self.size.height()
                elif index % Buffer.ROW_DIV == 3:
                    # Outer Right
                    if self.link_dir == "NORTH":
                        xpos += Buffer.N_OFFSET[0] + self.size.height()
                        ypos += Buffer.N_OFFSET[1] + self.size.height() * row_num - self.size.height()
                    elif self.link_dir == "SOUTH":
                        xpos += Buffer.S_OFFSET[0] - self.size.height() * 2
                        ypos += Buffer.S_OFFSET[1] - self.size.height() * row_num
                    elif self.link_dir == "EAST":
                        xpos += Buffer.E_OFFSET[0] - self.size.height() * row_num
                        ypos += Buffer.E_OFFSET[1] - self.size.height() - self.size.height()
                    elif self.link_dir == "WEST":
                        xpos += Buffer.W_OFFSET[0] + self.size.height() * row_num - self.size.height()
                        ypos += Buffer.W_OFFSET[1] - 2 * self.size.height()
                    elif self.link_dir == "CORE":
                        xpos += Buffer.C_OFFSET[0] + self.size.height()
                        ypos += Buffer.C_OFFSET[1] - self.size.height() * row_num + self.size.height()
                self.top_left_corners.append(QtCore.QPointF(xpos, ypos))
                self.rects.append(QtCore.QRectF(self.top_left_corners[index], self.size))
            self.reorder_buffer()
            self.setup_text_ids()

        else:
            # create single row of VCs
            length = math.floor(drawAttr.CORE_SIZE / (networkAttr.CORE_VCS + 2))
            self.size.setHeight(length)
            self.size.setWidth(length)

    def set_buffer_size(self):
        # create rows of 4 VCs
        length = math.floor(drawAttr.CORE_SIZE / (
            Buffer.ROW_DIV + 2 * math.ceil(networkAttr.CORE_VCS / Buffer.ROW_DIV)))
        self.size.setHeight(length)
        self.size.setWidth(length)

    def reorder_buffer(self):
        # Sort Rects into actual VC ordering
        full_rows = math.floor(networkAttr.CORE_VCS / Buffer.ROW_DIV)
        last_row = networkAttr.CORE_VCS % Buffer.ROW_DIV
        temp_rects = []
        for row in range(full_rows):
            temp_rects.append(self.rects[row * Buffer.ROW_DIV + 2])
            temp_rects.append(self.rects[row * Buffer.ROW_DIV + 0])
            temp_rects.append(self.rects[row * Buffer.ROW_DIV + 1])
            temp_rects.append(self.rects[row * Buffer.ROW_DIV + 3])
        if last_row == 0:
            pass
        elif last_row == 1:
            temp_rects.append(self.rects[full_rows * Buffer.ROW_DIV + 0])
        elif last_row == 2:
            temp_rects.append(self.rects[full_rows * Buffer.ROW_DIV + 0])
            temp_rects.append(self.rects[full_rows * Buffer.ROW_DIV + 1])
        elif last_row == 3:
            temp_rects.append(self.rects[full_rows * Buffer.ROW_DIV + 2])
            temp_rects.append(self.rects[full_rows * Buffer.ROW_DIV + 0])
            temp_rects.append(self.rects[full_rows * Buffer.ROW_DIV + 1])
        self.rects = temp_rects

    def setup_text_ids(self):
        for vc_id, rect in enumerate(self.rects):
            self.buffer_vc_Ids_text.append(str(vc_id))
            pos = rect.center()
            pos.setY(pos.y() + 5)
            pos.setX(pos.x() - 3)
            self.buffer_vc_ids_text_pos.append(pos)

    def draw_buffer(self, painter):
        for index, VC in enumerate(self.rects):
            painter.drawRect(VC)
            painter.drawText(self.buffer_vc_ids_text_pos[index], self.buffer_vc_Ids_text[index])

    @staticmethod
    def set_to_expanded():
        Buffer.N_OFFSET = [drawAttr.CORE_SIZE_EXP / 2, 0]
        Buffer.S_OFFSET = [drawAttr.CORE_SIZE_EXP / 2, drawAttr.CORE_SIZE_EXP]
        Buffer.E_OFFSET = [drawAttr.CORE_SIZE_EXP, drawAttr.CORE_SIZE_EXP / 2]
        Buffer.W_OFFSET = [0, drawAttr.CORE_SIZE_EXP / 2]
        Buffer.C_OFFSET = [drawAttr.CORE_SIZE_EXP / 2, drawAttr.CORE_SIZE_EXP / 2 - 15]

    def __str__(self):
        string = "Buffer Direction:" + self.link_dir + "\n\r"
        string += "Flit Information would go here:"
        return string

    def __repr__(self):
        string = "Buffer Direction:" + self.link_dir + "\n\r"
        string += "Flit Information would go here:"
        return string

    def update_buffer(self):
        pass
