from link import Link
from core import Core
from networkAttr import networkAttr
from drawAttr import drawAttr
from PyQt4 import QtGui


class Network(QtGui.QWidget):
    CYCLE_NUMBER = 0

    def __init__(self, parent_widget, topology, num_cores, num_rows, vcs_per_vnet, net_total_cycle):
        super(Network, self).__init__()
        self.setParent(parent_widget)
        self.topology = topology
        networkAttr(num_rows, num_cores / num_rows, num_cores, vcs_per_vnet, net_total_cycle)
        # Setup QWidget Attributes
        side = drawAttr.CORE_SIZE * networkAttr.CORE_CORES \
               + drawAttr.LINK_LENGTH * (networkAttr.CORE_CORES - 1)
        self.setMinimumSize(side, side)

        # create cores
        self.cores = []
        self.create_cores()
        # create links
        self.links = []
        self.create_links()
        self.show()

    def create_cores(self):
        for core_id in range(networkAttr.CORE_CORES):
            self.cores.append(Core(core_id))

    def create_links(self):
        # Create Links
        for row in range(networkAttr.CORE_ROWS):
            for col in range(networkAttr.CORE_COLS):
                if col + 1 < networkAttr.CORE_COLS:
                    core_id = row * networkAttr.CORE_COLS + col
                    self.links.append(Link(self.cores[core_id], self.cores[core_id + 1]))
                if col - 1 >= 0:
                    core_id = row * networkAttr.CORE_COLS + col
                    self.links.append(Link(self.cores[core_id], self.cores[core_id - 1]))
        for col in range(networkAttr.CORE_COLS):
            for row in range(networkAttr.CORE_ROWS):
                if row + 1 < networkAttr.CORE_ROWS:
                    core_id = row * networkAttr.CORE_COLS + col
                    self.links.append(Link(self.cores[core_id], self.cores[core_id + networkAttr.CORE_COLS]))
                if row - 1 >= 0:
                    core_id = row * networkAttr.CORE_COLS + col
                    self.links.append(Link(self.cores[core_id], self.cores[core_id - networkAttr.CORE_COLS]))

    def draw_network(self, painter):
        for core in self.cores:
            core.draw_core(painter)
        for link in self.links:
            link.draw_link(painter)

    def paintEvent(self, event):
        qp = QtGui.QPainter()

        qp.begin(self)
        # qp.setWindow(0, -21, 750, 750)
        # qp.translate(0, 21)
        self.draw_network(qp)
        qp.end()

    def next_cycle(self):
        if Network.CYCLE_NUMBER == networkAttr.NET_TOTCYCLES:
            return None
        else:
            Network.CYCLE_NUMBER += 1
        return Network.CYCLE_NUMBER

    def prev_cycle(self):
        if Network.CYCLE_NUMBER == 0:
            return None
        else:
            Network.CYCLE_NUMBER -= 1
        return Network.CYCLE_NUMBER

    def go_to_cycle(self, cycle_num):
        if cycle_num < 0:
            return None
        elif cycle_num > networkAttr.NET_TOTCYCLES:
            return None
        else:
            Network.CYCLE_NUMBER = int(cycle_num)
        return Network.CYCLE_NUMBER

    def update_network(self):
        for core in self.cores:
            core.update_core()
        for link in self.links:
            link.update_link()
        self.update()
