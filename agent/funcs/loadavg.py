# -*- coding: utf-8 -*-


class LoadAvg:

    def __init__(self):
        self.load_1min = self.get_load_1min()
        self.load_5min = self.get_load_5min()
        self.load_15min = self.get_load_15min()

    def get_load_info(self):
        with open('/proc/loadavg') as f:
            lines = f.readlines()
        return lines

    def get_load_1min(self):
        return float(self.get_load_info()[0].split()[0])

    def get_load_5min(self):
        return float(self.get_load_info()[0].split()[1])

    def get_load_15min(self):
        return float(self.get_load_info()[0].split()[2])