import csv
import itertools
from flit import Flit
from networkAttr import networkAttr


#Parser developed with garnet2.0 parser
#Reads in CSV file for each cycle
#Cycle counts larger than 5000 not recommended due to delay
class traceParser(object):
    def __init__(self):
        self.cycle_row_nums = dict()
        self.csv_file_name = None
        self.csv = None
        self.reader = None
        self.flit_tracker = dict()

    #opens the trace
    def open_trace(self, csv_file_name):
        self.csv_file_name = csv_file_name
        self.csv = open(csv_file_name, 'r')
        self.reader = csv.reader(self.csv)
        self.preprocess()

    #creates a dictionary with key = cycle number and value = row the cycle begins at
    def preprocess(self):
        for row_num, row in enumerate(self.reader):
            if 'GarnetNetwork' not in row[0]:
                if int(row[0]) in self.cycle_row_nums:
                    pass
                else:
                    self.cycle_row_nums[int(row[0])] = row_num

    #Returns cycle data based on cycle number using the dictionary lookup
    #Returns empty list if cycle does not exist
    def get_cycle(self, cycle_num):
        updated_router_flits = []
        updated_link_flits = []
        updated_exit_flits = []
        with open(self.csv_file_name, 'r') as f:
            if cycle_num in self.cycle_row_nums:
                # find next cycle
                next_cycle = cycle_num + 1
                while next_cycle not in self.cycle_row_nums:
                    next_cycle += 1
                for row in itertools.islice(csv.reader(f), self.cycle_row_nums[cycle_num],
                                            self.cycle_row_nums[cycle_num + 1]):
                    insert_flit = Flit(row)
                    # color assignment
                    if insert_flit.id in self.flit_tracker:
                        insert_flit.set_flit_color(self.flit_tracker[insert_flit.id])
                        # remove color entry if flit has entered the exit link
                        if insert_flit.location is "Link":
                            if networkAttr.CORE_CORES <= insert_flit.link_id < networkAttr.CORE_CORES * 2:
                                self.flit_tracker.pop(insert_flit.id)
                    else:
                        self.flit_tracker[insert_flit.id] = insert_flit.get_flit_color()

                    if insert_flit.location == "Link":
                        updated_link_flits.append(insert_flit)
                    elif insert_flit.location == "InUnit":
                        updated_router_flits.append(insert_flit)

                    # Create list of flits on core interface link
                    if insert_flit.location == "Link":
                        if networkAttr.CORE_CORES <= insert_flit.link_id < networkAttr.CORE_CORES * 2:
                            updated_exit_flits.append(insert_flit.id)

                return updated_router_flits, updated_link_flits, updated_exit_flits
            return [], [], []

    #Takes in first line from CSV and converts to network parameters
    def get_network_info(self):
        with open(self.csv_file_name, 'r') as f:
            reader = csv.reader(f)
            row1 = next(reader)
            if 'GarnetNetwork' in row1[0]:
                net_info = []
                net_info.append(int(row1[1].split("=")[1]))
                net_info.append(int(row1[2].split("=")[1]))
                net_info.append(int(row1[3].split("=")[1]))
                net_info.append(int(row1[4].split("=")[1]))
                list_of_cycles = list(self.cycle_row_nums.keys())
                net_info.append(max(list_of_cycles))
                return net_info
            else:
                print("Invalid Trace")
                return None
