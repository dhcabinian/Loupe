import csv
import itertools


class Parser(object):
    def __init__(self):
        self.cycle_row_nums = dict()
        self.csv_file_name = None
        self.csv = None
        self.reader = None

    def open_trace(self, csv_file_name):
        self.csv_file_name = csv_file_name
        self.csv = open(csv_file_name, 'r')
        self.reader = csv.reader(self.csv)
        self.preprocess()

    def preprocess(self):
        for row_num, row in enumerate(self.reader):
            if row[1].split("=")[0] == " Cycle":
                if int(row[1].split("=")[1]) in self.cycle_row_nums:
                    pass
                else:
                    self.cycle_row_nums[int(row[1].split("=")[1])] = row_num

    def get_cycle(self, cycle_num):
        updated_router_flits = []
        updated_link_flits = []
        with open(self.csv_file_name, 'r') as f:
            for row in itertools.islice(csv.reader(f), self.cycle_row_nums[cycle_num], self.cycle_row_nums[cycle_num + 1]):
                # insert_flit = Flit(row)
                insert_flit = None
                if insert_flit.location == "Link":
                    updated_link_flits.append(insert_flit)
                elif insert_flit.location == "InUnit":
                    updated_router_flits.append(insert_flit)
        return updated_router_flits, updated_link_flits

    def get_network_info(self):
        with open(self.csv_file_name, 'r') as f:
            reader = csv.reader(f)
            row1 = next(reader)
            if row1[0] is "GarnetNetwork":
                cores = int(row1[1].split("=")[1])
                rows = int(row1[2].split("=")[1])
                vcs = int(row1[3].split("=")[1])
                vnets = int(row1[4].split("=")[1])
                list_of_cycles = list(self.cycle_row_nums.keys())
                totalcycles = max(list_of_cycles)
                return [cores, rows, vcs, vnets, totalcycles]
            else:
                print("Invalid Trace")
                return None