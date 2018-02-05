# coding:utf8
import os
import json
from subprocess import Popen, PIPE

import psutil

def get_cpu():
    sys_cpu = {}
    cpu_time = psutil.cpu_times_percent(interval=1)
    sys_cpu['cpu_num'] = psutil.cpu_count()
    sys_cpu['phyical_cpu_num'] = psutil.cpu_count(logical=False)
    sys_cpu['user_time'] = cpu_time.user
    sys_cpu['nice_time'] = cpu_time.nice
    sys_cpu['system_time'] = cpu_time.system
    sys_cpu['idle_time'] = cpu_time.idle
    sys_cpu['iowait_time'] = cpu_time.iowait
    sys_cpu['irq_time'] = cpu_time.irq
    sys_cpu['softirq_time'] = cpu_time.softirq
    sys_cpu['guest_time'] = cpu_time.guest
    return sys_cpu


#if __name__ == '__main__':
#    system_cpu = get_cpu()
#    system_cpu_info = json.dumps(system_cpu)
#    print(system_cpu_info)
