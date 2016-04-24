from duplexLink import duplexLink
from core import Core
from networkAttr import networkAttr
from drawAttr import drawAttr
from PyQt4 import QtGui
import operator


# Network implementing a mesh
class Network(QtGui.QWidget):
    # The current cycle the network is at
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

    # Creates the cores
    # Allocates the cores ID's based on garnet id scheme
    # Sorts the listing of cores based on new garnet ID
    def create_cores(self):
        for core_id in range(networkAttr.CORE_CORES):
            self.cores.append(Core(core_id))
        new_core_id = networkAttr.CORE_CORES - networkAttr.CORE_COLS
        for core in self.cores:
            core.set_core_id(new_core_id)
            new_core_id += 1
            if new_core_id % networkAttr.CORE_COLS == 0:
                new_core_id -= 2 * networkAttr.CORE_COLS
        self.cores.sort(key=operator.attrgetter("core_id"), reverse=False)

    # Creates links based on mesh topology
    def create_links(self):
        # Create Links
        # Create E/W Links
        for row in range(networkAttr.CORE_ROWS):
            for col in range(networkAttr.CORE_COLS):
                if col + 1 < networkAttr.CORE_COLS:
                    core_id = row * networkAttr.CORE_COLS + col
                    self.links.append(duplexLink(self.cores[core_id], self.cores[core_id + 1], "E/W"))
        # Create N/S links
        for col in range(networkAttr.CORE_COLS):
            for row in range(networkAttr.CORE_ROWS):
                if row + 1 < networkAttr.CORE_ROWS:
                    core_id = row * networkAttr.CORE_COLS + col
                    self.links.append(
                        duplexLink(self.cores[core_id], self.cores[core_id + networkAttr.CORE_COLS], "N/S"))

    # Draws the network
    def draw_network(self, painter):
        for core in self.cores:
            core.draw_core(painter)
        for link in self.links:
            link.draw_duplex_link(painter)

    # Paints the network
    def paintEvent(self, event):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.draw_network(qp)
        qp.end()

    # Returns the next cycle number
    # Checks for out of bounds cycle
    def next_cycle(self):
        if Network.CYCLE_NUMBER == networkAttr.NET_TOTCYCLES:
            return None
        else:
            Network.CYCLE_NUMBER += 1
        return Network.CYCLE_NUMBER

    # Returns the previous cycle number
    # Checks for out of bounds cycle
    def prev_cycle(self):
        if Network.CYCLE_NUMBER == 0:
            return None
        else:
            Network.CYCLE_NUMBER -= 1
        return Network.CYCLE_NUMBER

    # Returns the cycle number
    # Checks for out of bounds cycle
    def go_to_cycle(self, cycle_num):
        if cycle_num < 0:
            return None
        elif cycle_num > networkAttr.NET_TOTCYCLES:
            return None
        else:
            Network.CYCLE_NUMBER = int(cycle_num)
        return Network.CYCLE_NUMBER

    # Updates all graphics objects of the network based on parsed cycle data
    def update_network(self, updated_router_flits, updated_link_flits, updated_exit_flits):
        for core in self.cores:
            flits_per_router = []
            flits_possib_on_link = []
            # Sorts flits from parser by router
            for flit in updated_router_flits:
                if flit.router == core.core_id:
                    flits_per_router.append(flit)
            # Sorts flits from parser by link for use in buffer driving link
            for flit in updated_link_flits:
                if flit.link_id in core.link_ids:
                    flits_possib_on_link.append(flit)
            core.update_core(flits_per_router, flits_possib_on_link, updated_exit_flits)
        # Sorts flits from parser by link using garnet link id scheme
        for duplex_link in self.links:
            flits_per_link = []
            for flit in updated_link_flits:
                if flit.link_id == duplex_link.link_id:
                    flits_per_link.append(flit)
            duplex_link.update_duplex_link(flits_per_link)
        self.update()

    def __str__(self):
        string = "[Network:: "
        string += "Topology: " + self.topology + " | "
        string += "VCs: " + str(networkAttr.CORE_VCS) + " | "
        string += "Total Cycles Simulated: " + str(networkAttr.NET_TOTCYCLES)
        string += "]"
        return string

    def __repr__(self):
        string = "[Network:: "
        string += "Topology: " + self.topology + " | "
        string += "VCs: " + str(networkAttr.CORE_VCS) + " | "
        string += "Total Cycles Simulated: " + str(networkAttr.NET_TOTCYCLES)
        string += "]"
        return string
