from link import Link
from core import Core
from networkAttr import networkAttr
from drawAttr import drawAttr
from PyQt4 import QtGui


class Network(QtGui.QWidget):
    def __init__(self, topology, num_cores, num_rows, vcs_per_vnet):
        super(Network, self).__init__()
        self.topology = topology
        # setup network attributes
        core_size = 150
        link_length = 50
        link_width = 10
        netAttributes = networkAttr(num_rows, num_cores / num_rows, num_cores, vcs_per_vnet)
        drawAttributes = drawAttr(core_size, link_length, link_width)
        # create cores
        self.cores = []
        self.createCores()
        # create links
        self.links = []
        self.createLinks()

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

