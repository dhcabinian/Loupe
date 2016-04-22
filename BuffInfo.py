import math

from PyQt4 import QtGui

from networkAttr import networkAttr


class BuffInfo(QtGui.QWidget):
    def __init__(self):
        super(BuffInfo, self).__init__()
        # Core Information
        self.buffers = None
        self.cur_buff_index = None
        self.top_table = None
        self.bottom_table = None
        self.core_num = None

    def update_buff_core(self, core_in, cur_buffer):
        self.buffers = core_in.get_buffers()
        self.cur_buff_index = cur_buffer

    def setup_both_tables(self):
        self.setup_vc_tables(self.top_table, "Top")
        self.setup_vc_tables(self.bottom_table, "Bottom")

    def setup_vc_tables(self, table, table_loc):
        if networkAttr.CORE_VCS > 4 and table_loc is "Top":
            self.top_table = table
            vc_range = math.ceil(networkAttr.CORE_VCS / 2)
            vc_start = 0
            vc_end = vc_range
        elif networkAttr.CORE_VCS > 4 and table_loc is "Bottom":
            self.bottom_table = table
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

    def update_tables(self, buffer):
        print("updating buffer tables")
        flits = self.buffers[buffer].peek_flits()
        for flit in flits:
            flit_table_entries = self.setup_table_items(flit)
            if flit.vc <= self.top_table.columnCount():
                for row, entry in enumerate(flit_table_entries):
                    self.top_table.setItem(row, flit.vc, entry)
            else:
                for row, entry in enumerate(flit_table_entries):
                    self.top_table.setItem(row, flit.vc - self.top_table.columnCount(), entry)
        self.update()

    def setup_table_items(self, flit):
        flit_qwidgets = []
        # flit Id
        flit_qwidgets.append(QtGui.QTableWidgetItem(str(flit.id)))
        # Flit Type
        flit_qwidgets.append(QtGui.QTableWidgetItem(flit.type))
        # flit Route
        string = str(flit.src) + "->" + str(flit.dest)
        flit_qwidgets.append(QtGui.QTableWidgetItem(string))
        # Flit Outport
        flit_qwidgets.append(QtGui.QTableWidgetItem(flit.outport))
        # Flit Source Delay
        flit_qwidgets.append(QtGui.QTableWidgetItem(str(flit.src_delay)))
        return flit_qwidgets

    def set_top_table(self, top_table):
        self.top_table = top_table

    def set_bottom_table(self, bottom_table):
        self.bottom_table = bottom_table

    def set_core_num(self, core_num):
        self.core_num = core_num

    def get_core_num(self):
        return self.core_num

    def get_cur_buff_index(self):
        return self.cur_buff_index
