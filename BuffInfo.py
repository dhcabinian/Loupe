from PyQt4 import QtGui, QtCore
from networkAttr import networkAttr
import math


class BuffInfo(object):
    def __init__(self):
        # Core Information
        self.buffers = None
        self.cur_buff_index = None
        self.top_table = None
        self.bottom_table = None

    def update_buff_core(self, core_in, cur_buffer):
        self.buffers = core_in.get_buffers()
        self.cur_buff_index = cur_buffer

    def setup_both_tables(self):
        self.setup_vc_tables(self.top_table, "Top")
        self.setup_vc_tables(self.bottom_table, "Bottom")

    def setup_vc_tables(self, table, table_loc):
        vc_range = None
        vc_start = None
        vc_end = None
        if networkAttr.CORE_VCS > 4 and table_loc is "Top":
            vc_range = math.ceil(networkAttr.CORE_VCS / 2)
            vc_start = 0
            vc_end = vc_range
        elif networkAttr.CORE_VCS > 4 and table_loc is "Bottom":
            vc_range = math.floor(networkAttr.CORE_VCS / 2)
            vc_start = vc_range
            vc_end = networkAttr.CORE_VCS
        else:
            vc_range = networkAttr.CORE_VCS
            vc_start = 0
            vc_end = networkAttr.CORE_VCS

        table.setColumnCount(vc_range)
        table.setRowCount(5)

        item = QtGui.QTableWidgetItem()
        table.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        table.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        table.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        table.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        table.setVerticalHeaderItem(4, item)
        item = table.verticalHeaderItem(0)
        item.setText("Flit Id")
        item = table.verticalHeaderItem(1)
        item.setText("Flit Type")
        item = table.verticalHeaderItem(2)
        item.setText("Flit Route")
        item = table.verticalHeaderItem(3)
        item.setText("Flit Outport")
        item = table.verticalHeaderItem(4)
        item.setText("Flit Src Delay")

        for index, vc_num in enumerate(range(vc_start, vc_end)):
            item = QtGui.QTableWidgetItem()
            table.setHorizontalHeaderItem(index, item)
            item = table.horizontalHeaderItem(index)
            item.setText("VC " + str(vc_num))

    def update_tables(self, cur_buffer):
        pass

    def set_top_table(self, top_table):
        self.top_table = top_table

    def set_bottom_table(self, bottom_table):
        self.bottom_table = bottom_table