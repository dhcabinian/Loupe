from PyQt4 import QtGui
from link import Link
from networkAttr import networkAttr
import math


class duplexLink(QtGui.QWidget):
    def __init__(self, core1, core2, direction):
        super(duplexLink, self).__init__()
        self.core1 = core1
        self.core2 = core2
        self.direction = direction
        self.links = []
        self.link_id = None
        self.updated_link_flits = []
        self.create_links()

    def create_links(self):
        link1 = Link(self.core1, self.core2)
        self.links.append(link1)
        link2 = Link(self.core2, self.core1)
        self.links.append(link2)
        if link1.get_link_id() is link2.get_link_id():
            self.link_id = link1.get_link_id()
            self.core1.add_link_id(self.link_id)
            self.core2.add_link_id(self.link_id)

    def update_duplex_link(self, updated_link_flits):
        self.updated_link_flits = updated_link_flits
        link1_flit = []
        link2_flit = []
        for flit in self.updated_link_flits:
            dest_core = flit.dest
            hop_count_core1 = self.hop_count(self.core1.core_id, dest_core)
            hop_count_core2 = self.hop_count(self.core2.core_id, dest_core)
            if hop_count_core1 < hop_count_core2:
                link2_flit.append(flit)
            else:
                link1_flit.append(flit)
        self.links[0].update_link(link1_flit)
        self.links[1].update_link(link2_flit)
        self.notify_flits_core()

    def draw_duplex_link(self, painter):
        for link in self.links:
            link.draw_link(painter)

    def hop_count(self, src_core, dest_core):
        src_col = src_core % networkAttr.CORE_COLS
        src_row = math.floor(src_core / networkAttr.CORE_COLS)
        dest_col = dest_core % networkAttr.CORE_COLS
        dest_row = math.floor(dest_core / networkAttr.CORE_COLS)
        return abs(src_col - dest_col) + abs(src_row - dest_row)

    def notify_flits_core(self):
        for link in self.links:
            if not link.link_flit:
                pass
            else:
                send_core = link.core_send
                for buffer in send_core.buffers:
                    for flit in buffer.flits:
                        if flit.id == link.get_link_flit().id:
                            flit.set_on_link()
