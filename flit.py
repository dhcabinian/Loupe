# Flit Implementation
from PyQt4 import QtGui


class Flit(QtGui.QWidget):
    def __init__(self, f_id, f_vnet, f_vc, f_outport, f_src_delay):
        super(Flit, self).__init__()
        self.f_id = f_id
        self.f_vnet = f_vnet
        self.f_vc = f_vc
        self.f_outport = f_outport
        self.f_src_delay = f_src_delay

    def updateVC(self, newVC):
        self.f_vc = newVC
        return self.f_vc

    def updateOutport(self, newOutport):
        self.f_outport = newOutport
        return self.f_outport

    def drawFlit(self, painter):
        pass