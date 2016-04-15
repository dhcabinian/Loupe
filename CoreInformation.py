from PyQt4 import QtGui, QtCore


class CoreInfo(QtGui.QWidget):
    def __init__(self, parent_widget, core_in):
        super(CoreInfo, self).__init__()
        self.setParent(parent_widget)
        # Core Information
        self.core_id = None
        self.buffers = []
        self.text_info = []
        self.text_info_pos = []
        self.create_text_info_positions()
        self.update_core_info(core_in)

    def update_core_info(self, core_in):
        self.buffers = core_in.get_buffers()
        self.core_id = core_in.core_id
        self.update_text()

    def update_text(self):
        self.text_info = []
        for buf in self.buffers:
            self.text_info.append(str(buf))

    def create_text_info_positions(self):
        # Position for each buffer
        for ypos in range(10, 110, 20):
            self.text_info_pos.append(QtCore.QPointF(0, ypos))

    def paintEvent(self, event):
        painter = QtGui.QPainter()
        painter.begin(self)
        self.draw_core_info(painter)
        painter.end()

    def draw_core_info(self, painter):
        for index, text in enumerate(self.text_info):
            painter.drawText(self.text_info_pos[index], self.text_info[index])
