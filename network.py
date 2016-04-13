from link import Link
from core import Core
from networkAttr import networkAttr
from drawAttr import drawAttr
from PyQt4 import QtGui


class Network(QtGui.QWidget):
    CYCLE_NUMBER = 0

    def __init__(self, parent, topology, num_cores, num_rows, vcs_per_vnet, net_cycle):
        super(Network, self).__init__()
        self.setParent(parent)
        self.topology = topology
        networkAttr(num_rows, num_cores / num_rows, num_cores, vcs_per_vnet, net_cycle)
        # Setup QWidget Attributes
        side = drawAttr.DRAW_CORE_SIZE * networkAttr.ATTR_CORE_CORES\
               + drawAttr.DRAW_LINK_LENGTH * (networkAttr.ATTR_CORE_CORES - 1)
        self.setMinimumSize(side, side)

        # create cores
        self.cores = []
        self.createCores()
        # create links
        self.links = []
        self.createLinks()
        self.show()

    def createCores(self):
        for core_id in range(networkAttr.ATTR_CORE_CORES):
            self.cores.append(Core(core_id, networkAttr.ATTR_CORE_VCS, networkAttr.ATTR_CORE_COLS))

    def createLinks(self):
        # Create Links
        for row in range(networkAttr.ATTR_CORE_ROWS):
            for col in range(networkAttr.ATTR_CORE_COLS):
                if col + 1 < networkAttr.ATTR_CORE_COLS:
                    coreId = row * networkAttr.ATTR_CORE_COLS + col
                    self.links.append(Link(self.cores[coreId], self.cores[coreId + 1]))
                if col - 1 >= 0:
                    coreId = row * networkAttr.ATTR_CORE_COLS + col
                    self.links.append(Link(self.cores[coreId], self.cores[coreId - 1]))
        for col in range(networkAttr.ATTR_CORE_COLS):
            for row in range(networkAttr.ATTR_CORE_ROWS):
                if row + 1 < networkAttr.ATTR_CORE_ROWS:
                    coreId = row * networkAttr.ATTR_CORE_COLS + col
                    self.links.append(Link(self.cores[coreId], self.cores[coreId + networkAttr.ATTR_CORE_COLS]))
                if row - 1 >= 0:
                    coreId = row * networkAttr.ATTR_CORE_COLS + col
                    self.links.append(Link(self.cores[coreId], self.cores[coreId - networkAttr.ATTR_CORE_COLS]))

    def drawNetwork(self, painter):
        for core in self.cores:
            core.drawCore(painter)
        for link in self.links:
            link.drawLink(painter)

    def paintEvent(self, event):
        qp = QtGui.QPainter()

        qp.begin(self)
        #qp.setWindow(0, -21, 750, 750)
        #qp.translate(0, 21)
        self.drawNetwork(qp)
        qp.end()

    def nextCycle(self):
        if Network.CYCLE_NUMBER == networkAttr.ATTR_NET_TOTCYCLES:
            return None
        else:
            Network.CYCLE_NUMBER += 1
        return Network.CYCLE_NUMBER

    def prevCycle(self):
        if Network.CYCLE_NUMBER == 0:
            return None
        else:
            Network.CYCLE_NUMBER -= 1
        return Network.CYCLE_NUMBER

    def goToCycle(self, cycleNum):
        if cycleNum < 0:
            return None
        elif cycleNum > networkAttr.ATTR_NET_TOTCYCLES:
            return None
        else:
            Network.CYCLE_NUMBER = int(cycleNum)
        return Network.CYCLE_NUMBER