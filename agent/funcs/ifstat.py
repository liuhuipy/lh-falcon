# -*- coding: utf-8 -*-


class IfStat:
    def get_if_stat_info(self):
        if_stat_info = {}
        with open('/proc/net/dev') as f:
            lines = f.readlines()
            for line in lines[2:]:
                line = line.split(':')
                addr_name, info = line[0].strip(), line[1].split()
                if_stat_info[addr_name] = info
        return if_stat_info

    def get_if_addrs(self):
        """get host all addrs"""
        return self.get_if_stat_info().keys()

    def get_net_if_in_sizes(self, addr):
        return int(self.get_if_stat_info()[addr][0])

    def get_net_if_in_packets(self, addr):
        return int(self.get_if_stat_info()[addr][1])

    def get_net_if_in_errors(self, addr):
        return int(self.get_if_stat_info()[addr][2])

    def get_net_if_in_dropped(self, addr):
        return int(self.get_if_stat_info()[addr][3])

    def get_net_if_in_fifo_errs(self, addr):
        return int(self.get_if_stat_info()[addr][4])

    def get_net_if_in_frame_errs(self, addr):
        return int(self.get_if_stat_info()[addr][5])

    def get_net_if_in_compressed_errs(self, addr):
        return int(self.get_if_stat_info()[addr][6])

    def get_net_if_in_multicast(self, addr):
        return int(self.get_if_stat_info()[addr][7])

    def get_net_if_out_sizes(self, addr):
        return int(self.get_if_stat_info()[addr][8])

    def get_net_if_out_packets(self, addr):
        return int(self.get_if_stat_info()[addr][9])

    def get_net_if_out_errors(self, addr):
        return int(self.get_if_stat_info()[addr][10])

    def get_net_if_out_dropped(self, addr):
        return int(self.get_if_stat_info()[addr][11])

    def get_net_if_out_fifo_errs(self, addr):
        return int(self.get_if_stat_info()[addr][12])

    def get_net_if_out_frame_errs(self, addr):
        return int(self.get_if_stat_info()[addr][13])

    def get_net_if_out_compressed_errs(self, addr):
        return int(self.get_if_stat_info()[addr][14])

    def get_net_if_out_multicast(self, addr):
        return int(self.get_if_stat_info()[addr][15])

    def get_net_if_total_sizes(self, addr):
        return self.get_net_if_in_sizes(addr) + self.get_net_if_out_sizes(addr)

    def get_net_if_total_dropped(self, addr):
        return self.get_net_if_in_dropped(addr) + self.get_net_if_out_dropped(addr)

    def get_net_if_total_errors(self, addr):
        return self.get_net_if_in_errors(addr) + self.get_net_if_out_errors(addr)

    def get_net_if_total_packets(self, addr):
        return self.get_net_if_in_packets(addr) + self.get_net_if_out_packets(addr)
