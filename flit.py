# Flit Implementation
from PyQt4 import QtGui


class Flit(QtGui.QWidget):
    def __init__(self, flit_id, vnet, vc, outport, src_delay):
        super(Flit, self).__init__()
        self.id = flit_id
        self.vnet = vnet
        self.vc = vc
        self.outport = outport
        self.src_delay = src_delay

    def update_vc(self, new_vc):
        self.vc = new_vc
        return self.vc

    def update_outport(self, new_outport):
        self.outport = new_outport
        return self.outport

    def draw_flit(self, painter):
        pass
