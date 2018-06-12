# -*- coding: utf-8 -*-


class Cpustat:
    """get cpu infomations"""
    def __init__(self):
        self.cpu_user = self.get_cpu_user()
        self.cpu_nice = self.get_cpu_nice()
        self.cpu_system = self.get_cpu_system()
        self.cpu_idle = self.get_cpu_idle()
        self.cpu_iowait = self.get_cpu_iowait()
        self.cpu_irq = self.get_cpu_irq()
        self.cpu_softirq = self.get_cpu_softirq()
        self.cpu_steal = self.get_cpu_steal()
        self.cpu_guest = self.get_cpu_guest()
        self.cpu_switches= self.get_cpu_switches()

    def get_cpu_times(self):
        with open('/proc/stat') as f:
            lines = f.readlines()[0]
        return lines.split()

    def get_cpu_user(self):
        return int(self.get_cpu_times()[1])

    def get_cpu_nice(self):
        return int(self.get_cpu_times()[2])

    def get_cpu_system(self):
        return int(self.get_cpu_times()[3])

    def get_cpu_idle(self):
        return int(self.get_cpu_times()[4])

    def get_cpu_iowait(self):
        return int(self.get_cpu_times()[5])

    def get_cpu_irq(self):
        return int(self.get_cpu_times()[6])

    def get_cpu_softirq(self):
        return int(self.get_cpu_times()[7])

    def get_cpu_steal(self):
        return int(self.get_cpu_times()[8])

    def get_cpu_guest(self):
        return int(self.get_cpu_times()[9])

    def get_cpu_switches(self):
        return int(self.get_cpu_times()[10])


