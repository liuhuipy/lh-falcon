# -*- coding:utf-8 -*-


class Meminfo:

    def __init__(self):
        self.mem_memtotal = self.get_mem_memtotal()
        self.mem_memused = self.get_mem_memused()
        self.mem_memused_percent = self.get_mem_memused_percent()
        self.mem_memfree = self.get_mem_memfree()
        self.mem_memfree_percent = self.get_mem_memfree_percent()
        self.mem_swaptotal = self.get_mem_swaptotal()
        self.mem_swapused = self.get_mem_swapused()
        self.mem_swapused_percent = self.get_mem_swapused_percent()
        self.mem_swapfree = self.get_mem_swapfree()
        self.mem_swapfree_percent = self.get_mem_swapfree_percent()

    def get_meminfo(self):
        meminfo = {}
        with open('/proc/meminfo') as f:
            lines = f.readlines()
            for line in lines:
                if line.startswith('MemFree'):
                    meminfo['memfree'] = line.split()[1]
                if line.startswith('MemTotal'):
                    meminfo['memtotal'] = line.split()[1]
                if line.startswith('Buffers'):
                    meminfo['buffers'] = line.split()[1]
                if line.startswith('Cached'):
                    meminfo['cached'] = line.split()[1]
                if line.startswith('SwapFree'):
                    meminfo['swapfree'] = line.split()[1]
                if line.startswith('SwapTotal'):
                    meminfo['swaptotal'] = line.split()[1]
        return meminfo

    def get_mem_memtotal(self):
        return int(self.get_meminfo()['memtotal'])

    def get_mem_memused(self):
        return self.get_mem_memtotal() - self.get_mem_memfree()

    def get_mem_memused_percent(self):
        return int(float('%.2f' % (self.get_mem_memused() / self.get_mem_memtotal())) * 100)

    def get_mem_memfree(self):
        meminfo = self.get_meminfo()
        return int(meminfo['memfree']) + int(meminfo['buffers']) + int(meminfo['cached'])

    def get_mem_memfree_percent(self):
        return int(float('%.2f' % (self.get_mem_memfree() / self.get_mem_memtotal())) * 100)

    def get_mem_swaptotal(self):
        return int(self.get_meminfo()['swaptotal'])

    def get_mem_swapused(self):
        return self.get_mem_swaptotal() - self.get_mem_swapfree()

    def get_mem_swapused_percent(self):
        return int(float('%.2f' % (self.get_mem_swapused() / self.get_mem_swaptotal())) * 100)

    def get_mem_swapfree(self):
        return int(self.get_meminfo()['swapfree'])

    def get_mem_swapfree_percent(self):
        return int(float('%.2f' % (self.get_mem_swapfree() / self.get_mem_swaptotal())) * 100)
