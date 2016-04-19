# Flit Implementation
from PyQt4 import QtGui


class Flit(QtGui.QWidget):
    def __init__(self, trace_row):
        super(Flit, self).__init__()
        self.location = None
        self.in_dir = None
        self.router = None
        self.link_id = None
        self.id = None
        self.vnet = None
        self.vc = None
        self.outport = None
        self.src_delay = None
        self.type = None
        self.src = None
        self.dest = None
        self.enqueue_time = None
        self.parse_trace(trace_row)

    #Format for In Unit
    #[cycle, inunit, router_id, in_dir, [flit], outport]
    #Format for Link
    #[cycle, link, link_id, , [flit], ,]
    #Format for [flit]
    # [flit, id, type, vnet, vc, src, dest, time]

    def parse_trace(self, row):
        cycle = int(row[0])
        self.location = row[1]
        if self.location == "Link":
            self.link_id = int(row[2])
        elif self.location == "InUnit":
            if int(row[3]) == 0:
                self.in_dir = "Core"
            elif int(row[3]) == 1:
                self.in_dir = "West"
            elif int(row[3]) == 2:
                self.in_dir = "South"
            elif int(row[3]) == 3:
                self.in_dir = "East"
            elif int(row[3]) == 4:
                self.in_dir = "North"
            elif int(row[3]) == 5:
                self.in_dir = "Unknown"
            self.router = int(row[2])
        self.id = int(row[5])
        if int(row[6]) == 0:
            self.type = "Head"
        elif int(row[6]) == 1:
            self.type = "Body"
        elif int(row[6]) == 2:
            self.type = "Tail"
        elif int(row[6]) == 3:
            self.type = "Head + Tail"
        self.vnet = int(row[7])
        self.vc = int(row[8])
        self.src = int(row[9])
        self.dest = int(row[10])
        self.enqueue_time = int(row[11])
        if int(row[12]) == 0:
            self.outport = "Core"
        elif int(row[12]) == 1:
            self.outport = "West"
        elif int(row[12]) == 2:
            self.outport = "South"
        elif int(row[12]) == 3:
            self.outport = "East"
        elif int(row[12]) == 4:
            self.outport = "North"
        elif int(row[12]) == 5:
            self.outport = "Unknown"
        self.src_delay = cycle - self.enqueue_time

    def update_vc(self, new_vc):
        self.vc = new_vc
        return self.vc

    def update_outport(self, new_outport):
        self.outport = new_outport
        return self.outport

    def draw_flit(self, painter):
        pass
