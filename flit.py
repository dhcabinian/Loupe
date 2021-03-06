# Flit Implementation
import random

from PyQt4 import QtGui


class Flit(QtGui.QWidget):

    FLIT_CYCLES_DEADLOCK = None
    FLIT_DEADLOCK_COLOR = QtGui.QColor(255, 0, 0, 200)
    FLIT_DEADLOCK_TEXT_COLOR = QtGui.QColor(0, 0, 0, 255)

    def __init__(self, trace_row):
        super(Flit, self).__init__()
        self.cycle = None
        self.location = None
        self.in_dir = None
        self.router = None
        self.deadlocked = False
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
        self.color = QtGui.QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255), 110)
        self.text_color = None
        self.has_exited = False
        self.cycle_exited = None
        self.parse_trace(trace_row)
        self.create_text_color()

    # Format for In Unit
    # [cycle, inunit, router_id, in_dir, [flit], outport]
    # Format for Link
    # [cycle, link, link_id, , [flit], ,]
    # Format for [flit]
    # [flit, id, type, vnet, vc, src, dest, time]
    def parse_trace(self, row):
        self.cycle = int(row[0])
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
        if row[12] == '':
            self.outport = ""
        elif int(row[12]) == 0:
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
        self.src_delay = self.cycle - self.enqueue_time

    #Sets the flit color
    def set_flit_color(self, color):
        self.color = color
        self.create_text_color()

    #Retreives the flit color
    def get_flit_color(self):
        return self.color

    #Create text color using weighted algorithm
    def create_text_color(self):
        rgb = self.color.getRgb()
        red = rgb[0]
        green = rgb[1]
        blue = rgb[2]
        dark_or_light = ((red * 299) + (green * 587) + (blue * 114)) / 1000
        if dark_or_light >= 128:
            #Black Text
            self.text_color = QtGui.QColor(0, 0, 0, 255)
        else:
            #White Text
            self.text_color = QtGui.QColor(255, 255, 255, 255)

    def __str__(self):
        string = "[Flit::"
        string += " Id:" + str(self.id)
        string += " Location:" + self.location
        if self.location == "Link":
            string += " Link_Id:" + str(self.link_id)
        elif self.location == "InUnit":
            string += " Router:" + str(self.router)
            string += " In_dir:" + self.in_dir
        string += " Type:" + self.type
        string += " Vnet:" + str(self.vnet)
        string += " Vc:" + str(self.vc)
        string += " Src:" + str(self.src)
        string += " Dest:" + str(self.dest)
        string += " Outport:" + self.outport
        string += " Latency:" + str(self.src_delay)
        string += "\n\r"
        return string

    def __repr__(self):
        string = "[Flit::"
        string += " Id:" + str(self.id)
        string += " Location:" + self.location
        if self.location == "Link":
            string += " Link_Id:" + str(self.link_id)
        elif self.location == "InUnit":
            string += " Router:" + str(self.router)
            string += " In_dir:" + self.in_dir
        string += " Type:" + self.type
        string += " Vnet:" + str(self.vnet)
        string += " Vc:" + str(self.vc)
        string += " Src:" + str(self.src)
        string += " Dest:" + str(self.dest)
        string += " Outport:" + self.outport
        string += " Latency:" + str(self.src_delay)
        string += "\n\r"
        return string
